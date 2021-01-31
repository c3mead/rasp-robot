import smbus
import time

bus = smbus.SMBus(1)

# Disable gyroscope first by setting control sensor to 0x00
bus.write_byte_data(0x6b, 0x11, 0x00)
time.sleep(0.1)
print(bus.read_byte_data(0x6b, 0x10))

print(bus.read_byte_data(0x6b, 0x11))
print(0x11)
print(0x23)

# Initialize gyro
time.sleep(0.1)
bus.write_byte_data(0x6b, 0x11, 0x58)
time.sleep(0.1)
print(bus.read_byte_data(0x6b, 0x11))


# read x-sensor data
#while True:
    #x_l = bus.read_byte_data(0x6b, 0x22) # - low byte data
    #x_h = bus.read_byte_data(0x6b, 0x23) # - high byte data
    #time.sleep(0.1)
    #print(x_l, x_h)
    # combine the low and high bytes
#    x_c = (x_l | x_h << 8)
#    if x_c > 32768:
#        x_c = x_c - 65536
#    print(x_c)