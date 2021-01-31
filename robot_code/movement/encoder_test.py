from gpiozero import DigitalInputDevice
from time import sleep

pin = 26
n = 0
def poop():
    print(n)

encoder = DigitalInputDevice(pin)

while True:
    #encoder.when_deactivated = poop()
    print(encoder.value)