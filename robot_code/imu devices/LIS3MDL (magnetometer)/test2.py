import smbus

bus = smbus.SMBus(1)

# Initialize Accelerometer
#bus.write_byte_data(0x6b, 0x10, 0x58)

# Initialize Gyroscope
#bus.write_byte_data(0x6b, 0x11, 0x58)
# 833Hz, 2000dps, full scale at 125 dps disabled

x = bus.read_byte_data(0x6b, 0x0F)

print(x)
print(bin(x))