from gpiozero import DigitalInputDevice, Robot
from gpiozero import Motor
from time import sleep

t = 0.02 # sample time
n = 0
target = 45 # target encoder speed
kp = 0.015 # proportional constant
kd = 0.0025 # deriative constant
ki = 0.0009 # integral constant

e_one = []
e_two = []

class Encoder():
    def __init__(self, pin):
        self.value = 0
        self.encoder = DigitalInputDevice(pin)
        
        self.error = 0
        self.e_prev = 0
        self.e_sum = 0
        
    def _error(self, kp, kd, ki):
        self.p = float(self.error * kp)
        self.d = float(self.e_prev * kd)
        self.i = float(self.e_sum * ki)
        
        return self.p + self.d + self.i
        
    def _increment(self):
        self.value += 1
    
    def _reset(self):
        self.e_prev = self.error
        self.e_sum += self.error
        
        self.value = 0

enc_1 = Encoder(19) # left motor
#l_enc_2 = Value(26)
enc_2 = Encoder(5) # right motor
#r_enc_2 = Value(6)

m1 = Motor(forward=17, backward=18) #Left Motor
m2 = Motor(forward=27, backward=22) #Right Motor

m1_speed = 0.75
m2_speed = 0.75

while True:
    m1.forward(m1_speed)
    m2.forward(m2_speed)
      
    enc_1.encoder.when_activated = enc_1._increment
    enc_2.encoder.when_activated = enc_2._increment

    enc_1.encoder.when_deactivated = enc_1._increment
    enc_2.encoder.when_deactivated = enc_2._increment

    sleep(t)
    
    enc_1.error = target - enc_1.value
    enc_2.error = target - enc_2.value
    
    m1_error = enc_1._error(kp, kd, ki)
    m2_error = enc_2._error(kp, kd, ki)
    
    m1_speed += m1_error
    m2_speed += m2_error
    
    m1_speed = max(min(1, m1_speed), 0)
    m2_speed = max(min(1, m2_speed), 0)
        
    print("e1 {}   e2 {}".format(enc_1.value, enc_2.value))
    #print(enc_2.value)
    #e_one.append(enc_1.value)
    #e_two.append(enc_2.value)
        
    n += 1
    
    enc_1._reset()
    enc_2._reset()
    
    if n > 200:
        m1.stop
        m2.stop
        
        break