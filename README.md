# Raspberry-pi Robot
Two-wheel raspberry pi robot with onboard camera and 6-DoF IMU

## Table of Contents
1. Components
2. Creation
3. Testing
  
### Components
- Raspberry Pi 3 Model B+
  - Raspberry Pi Camera Module
  - microSD Card
  - HDMI cable, USB keyboard/mouse
  - 5-volt micro USB power adapter
- Breadboard
- 3D-Printed Chassis
- [Two DC motors (12-volt) w/ Encoders](https://www.pololu.com/product/3052/)
- 12 AA battery holder (w/ batteries)
- [LM2596 buck converter](https://tinyurl.com/y362cs4d/)
- [L293D motor controller](https://tinyurl.com/y3dsmn47/)
- Bluetooth remote (wii-remote)
- HC-SR04 Ultrasonic distance sensor
- [AltIMU-10 Inertial Measurement Unit (IMU) and Altimeter](https://www.pololu.com/product/2739/)

## Creation

### Chassis
First task was to create the robot's body. The planned designed was to create a body with a space for two motors, batteries, breadboard, the raspberry pi and buck. The following chassis was designed using CAD modeling software and was 3D printed using PC-ABS which is a relatively light material. 


![cad_chassis](https://i.imgur.com/lutdLZz.png) ![printed_chassis](https://i.imgur.com/8QxxVse.png) ![shop](https://i.imgur.com/eEUxcHq.png)

### Motors
Two DC-brushed motors were selected to give the motors movement. Motors were chosen based on how much on-board voltage the robot would carry (12-volts). On later designs, each motors was soldered to include an encoder. All wirings were equipped with heat shrink to strengthen the design. 

![motor-1](https://i.imgur.com/nvxclaP.png) ![motor-2](https://i.imgur.com/f29RlTg.png) ![motor-3](https://i.imgur.com/ZcVSjao.png)

### Final Assembly

I will go over the schematics in a later section; however this is an image of what the final assembly looks like once the wiring is complete.

![final](https://i.imgur.com/4ajpLgW.png)

## Testing
TBA...

