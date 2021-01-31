import smbus, math
from LSM6DS33 import LSM6DS33

class I2C():
    """Defines various I2c connection activities."""
    def __init__(self):
        self.bus = smbus.SMBus(1)
        
        # Initialize tracked gyroscope angles
        self.gyrAngleX = 0.0
        self.gyrAngleY = 0.0
        self.gyrAngleZ = 0.0
        self.cf_c = 0.95
        self.CFang = [0, 0, 0]
        self.CFangX = 0
        self.CFangY = 0
        self.CFangZ = 0

    def write_reg(self, addr, regis, value):
        """Write a byte to a specific register."""
        self.bus.write_byte_data(addr, regis, value)

    def read_reg(self, addr, regis):
        """Read a byte from a specific register."""
        self.bus.read_byte_data(addr, regis)

    def RawDataGrab(self, addr, reg):
        """ Returns the combined raw 16-byte values (hi and low bytes."""
        x_l = self.bus.read_byte_data(addr, reg[0])
        x_h = self.bus.read_byte_data(addr, reg[1])
        
        y_l = self.bus.read_byte_data(addr, reg[2])
        y_h = self.bus.read_byte_data(addr, reg[3])
        
        z_l = self.bus.read_byte_data(addr, reg[4])
        z_h = self.bus.read_byte_data(addr, reg[5])
        
        x_com = self.combineSignedLo_Hi(x_l, x_h)
        y_com = self.combineSignedLo_Hi(y_l, y_h)
        z_com = self.combineSignedLo_Hi(z_l, z_h)
        
        return [x_com, y_com, z_com]
        
    def combineLo_Hi(self, lo_B, hi_B):
        """Combines and returns combined lo and hi bytes."""
        # Values read are in two's compliment (MSB for the sign and then 15 bits or the value)
        return (lo_B | hi_B << 8)
    
    def combineSignedLo_Hi(self, lo_B, hi_B):
        """ Combine low and high bytes to a signed 16 bit value. """
        combined = self.combineLo_Hi(lo_B, hi_B)
        return combined if combined < 32768 else (combined - 65536)
    
    def gyro_conv(self, gain, raw, t):
        """Converts raw accel/gyro numbers using sensitivity level."""
        rate = []
        for x in raw:
            rate.append(x * gain)
        p = self.gyroTrack(rate, t)
        return p
    
    def gyroTrack(self, rate, t):
        """Track gyrometer angle change over time delta deltaT.
            deltaT has to be extremely accurate, otherwise the gyroscope
            values will drift.
            The result is returned as a vector (list) of floating
            point numbers representing the angle in degrees.
        """
        
        self.gyrAngleX += (rate[0] * t)
        self.gyrAngleY += (rate[1] * t)
        self.gyrAngleZ += (rate[2] * t)
        
        return [self.gyrAngleX, self.gyrAngleY, self.gyrAngleZ]
    
    def acclAngles(self, raw):
        accX = math.degrees(math.atan2(raw[1], raw[2]) + math.pi)
        accY = math.degrees(math.atan2(raw[0], raw[2]) + math.pi)
        accZ = math.degrees(math.atan2(raw[0], raw[1]) + math.pi)
        
        return [accX, accY, accZ]    
    
    def combinedAng(self, gyroRate, acclAngles, gain, t):
        if self.CFangZ == 0:
            self.CFangZ = acclAngles[2]
        if self.CFangZ == 0:
            self.CFangY = acclAngles[1]
        if self.CFangZ == 0:
            self.CFangX = acclAngles[0]
        
        self.CFangZ = self.cf_c * (self.CFangZ + (gyroRate[2] * gain) * t) + (1-self.cf_c) * acclAngles[2]
        self.CFangY = self.cf_c * (self.CFangY + (gyroRate[1] * gain) * t) + (1-self.cf_c) * acclAngles[1]
        self.CFangX = self.cf_c * (self.CFangZ + (gyroRate[0] * gain) * t) + (1-self.cf_c) * acclAngles[0]

        return [self.CFangX, self.CFangY, self.CFangZ]