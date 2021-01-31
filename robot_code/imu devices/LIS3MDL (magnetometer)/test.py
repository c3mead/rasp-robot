import smbus
import time
import math

def combineLo_Hi(lo_B, hi_B):
    """Combines and returns combined lo and hi bytes."""
    # Values read are in two's compliment (MSB for the sign and then 15 bits or the value)
    return (lo_B | hi_B << 8)
    
def combineSignedLo_Hi(lo_B, hi_B):
    """ Combine low and high bytes to a signed 16 bit value. """
    combined = combineLo_Hi(lo_B, hi_B)
    return combined if combined < 32768 else (combined - 65536)

bus = smbus.SMBus(1)
bus.write_byte_data(0x1e, 0x20, 0b11011100)
bus.write_byte_data(0x1e, 0x21, 0b01000000)
bus.write_byte_data(0x1e, 0x22, 0b00000000)
bus.write_byte_data(0x1e, 0x23, 0b00001000)
n = 0

for _ in range(1000):
    x_l = bus.read_byte_data(0x1e, 0x28)
    x_h = bus.read_byte_data(0x1e, 0x29)
    y_l = bus.read_byte_data(0x1e, 0x2A)
    y_h = bus.read_byte_data(0x1e, 0x2B)
    z_l = bus.read_byte_data(0x1e, 0x2C)
    z_h = bus.read_byte_data(0x1e, 0x2D)
    
    xc = combineSignedLo_Hi(x_l, x_h)
    yc = combineSignedLo_Hi(y_l, y_h)
    zc = combineSignedLo_Hi(z_l, z_h)
    
    h = 180 * math.atan2(yc, xc) / math.pi
    if h < 0:
        h += 360
        
    n += 1
    print("Data #" + str(n))
    print(zc)
    print()
    #print("Heading:")
    #print(h)
    #print()
    #print([bin(xl), bin(yl), bin(zl)])
    time.sleep(0.2)