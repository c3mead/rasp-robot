from gpiozero import Robot, DigitalInputDevice
from time import sleep

samp_t = 0.5

class Encoder(object):
    def __init__(self, pin_a, pin_b):
        self._value = 0
        
        encoder_a = DigitalInputDevice(pin_a)
        encoder_a.when_activated = self._increment
        encoder_a.when_deactivated = self._increment

        encoder_b = DigitalInputDevice(pin_b)
        encoder_b.when_activated = self._increment
        encoder_b.when_deactivated = self._increment

    def reset(self):
        self._value = 0

    def _increment(self):
        self._value += 1

    @property
    def value(self):
        return self._value

#robot = Robot(left=(17,18), right=(27,22))
e1 = Encoder(5, 6) # Left Motor
e2 = Encoder(19, 26) # Right Motor

n = 0
while True:
    print("N " + str(n))
    print("e1 {} e2 {}".format(e1.value, e2.value))
    print()
    n += 1
    sleep(samp_t)