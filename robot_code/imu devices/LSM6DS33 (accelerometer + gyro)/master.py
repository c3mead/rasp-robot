import smbus
from datetime import datetime
import time
from LSM6DS33 import LSM6DS33
from bus_works import I2C

imu = LSM6DS33()
i2c = I2C()
bus = smbus.SMBus(1)

t = 0.105

gyroAngles = [0, 0, 0]

accl_regs = [
        0x28,
        0x29,
        0x2A,
        0x2B,
        0x2C,
        0x2D,
    ]

gyro_regs = [
        0x22,
        0x23,
        0x24,
        0x25,
        0x26,
        0x27,
    ]

# Make sure Accelerometer and Gyroscope are off.
i2c.write_reg(imu.addr, 0x10, 0) # Accel
i2c.write_reg(imu.addr, 0x11, 0) # Gyro
#time.sleep(0.02)

# Initialize Accelerometer
i2c.write_reg(imu.addr, 0x10, 0x58)
# 833Hz, +-4g, 400Hz filter
a_gain = 0.122 / 1000 #g/LBS
time.sleep(0.001)

# Initialize Gyroscope
i2c.write_reg(imu.addr, 0x11, 0b01111100)
# 833Hz, 2000dps, full scale at 125 dps disabled
g_gain = 70 / 1000 #dps/LBS
time.sleep(0.001)

blah = 0
a = datetime.now()

while True:
    blah += 1
    # Read Raw Data Data
    raw_accl = i2c.RawDataGrab(imu.addr, accl_regs)
    raw_gyro = i2c.RawDataGrab(imu.addr, gyro_regs)
    time.sleep(0.1)
    b = datetime.now()
    
    #time = .005 # need to convert this to an inerger

    # convert raw accelerometer data
    #Gs = i2c.raw_conv(a_gain, raw_accl)
    
    # Grab Accelerometer Angles
    acclAngles = i2c.acclAngles(raw_accl)

    # Grab Gyroscope Angles
    #gyroAngles = i2c.gyro_conv(g_gain, raw_gyro, t) # Rotation rate of gyroscope
    
    # Complementary Filter
    CFAng = i2c.combinedAng(raw_gyro, acclAngles, g_gain, t)

    #print("Data Collection Time: " + str(b-a) + " seconds")
    #print("Raw Accel: " + str(raw_accl))
    #print("Gs: " + str(Gs))
    #print("Accel Angles: " + str(acclAngles))
    #print("Gyro Angles: " + str(gyroAngles))
    print("CF Angles: " + str(CFAng))
    if blah >= 100:
        break
    
#while True:
    # Each loop should be at least 20ms
#    i2c.RawDataGrab(imu.addr, g_temp)

#    time.sleep(0.1)
#    t += 1
#    if t >= 100:
#        break


# Turn off accelormeter and gyroscope
#time.sleep(0.02)
i2c.write_reg(imu.addr, 0x10, 0) # Accel
i2c.write_reg(imu.addr, 0x11, 0) # Gyro
#print(b - a)