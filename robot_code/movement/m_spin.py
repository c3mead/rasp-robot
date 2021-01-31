import time
import gpiozero

robot = gpiozero.Robot(left=(17,18), right=(27,22))

for i in range(4):
    robot.forward(0.5)
    time.sleep(2)
    robot.right(0.5)
    time.sleep(1)