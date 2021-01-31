import gpiozero
import time

robot = gpiozero.Robot(left=(17,18), right=(27,22))

robot.forward(0.5)
time.sleep(5)
robot.stop