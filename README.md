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

<p align="center">
  <img src="https://i.imgur.com/4ajpLgW.png">
</p>

## Testing

### Motor Controller
Power to the DC motors is to be controlled by a [L293D motor controller](https://tinyurl.com/y3dsmn47/). This chip contains to H-Bridges which allows one to control two motors though a single chip. An H-bridge is an electrical circuit that allows a voltage to be applied across a load. 

![h_bridge](https://i.imgur.com/GrVV4lF.png) ![l293d](https://i.imgur.com/DjCpbVX.jpg)

When all switches are open, no voltage is applied and the motor doesn't move. When only s1 and s4 are closed, voltage flows in the other direction. The design of the L293D means that s1 and s2 cannot be closed at the same time. Same thing with s3 and s4. The L293D takes this further and requires only two inputs for one motor. The behavior for the motor depends on which inputs are high and which inputs are low. See table below

| Input 1  | Input 2 | Motor Behavior |
| :---: | :---: | :---: |
| Low | Low  | Motor off |
| Low | High | Motor rotates in one direction |
| High | Low | Motor moves in other direction |
| High | High | Motor off |

### Encoder
A two-channel Hall effect encoder was employed to each DC motor. To calculate the counts per revolution, the gear ratio must be multiplied by 25

#### Encoder Wiring

| Color | Function |
| :--- | :--- |
| red | motor power (v+) |
| black | motor power (v-) |
| green | encoder GND |
| blue | encoder Vcc |
| yellow | enc output A |
| white | enc output B |

Encoder test functions can be downloaded in the movement folder.

### Inertial Measurement Unit
#### AltINU-10 v5
The Pololu AltINU-10 v5 combines the following:
  - LSM6DS33: a 3-axis gyroscope and 3-axis accelerometer
  - LIS3MDL: a 3-axis magnetometer
  - LDS25H: a digital barometer and altimeter
  
Each sensor also has a choice of output data rates. The three ICs can be accessed through a shared I2C interface.

##### Gyroscope
Gyros are devices that measure or maintain rotational motion which is a measure of angular velocity - a measurement of speed of rotation. A gyroscope can be used to measure rotation from a balanced position and send corrections to a motor. When things rotate around on an axis, they have angular velocity whhich can be measured as RPMs. When the gyro-sensor is rotated, a small resonating mass is shifted as the angular velocity changes. This movement is converted into very low-current electrical signals. 

Range: maximum angular velocity that a gyro can read
sensitivity: measured in mV/deg/s. Determines how mich the voltage changes for a given angular velocity. For example, is sensitivity is set to 30 mV/deg/s, and you see a 300 mV change, you've rotated at 10 deg/s.

##### Accelerometer
This is a device that measures acceleration - the rate of change of velocity. The units are m/s^2 or g. For example, an accelerometer resting on a table would measure 1g straight upwards due to gravity. Similar to gyroscopes, there is a range and sensitivity level for the accelerometer. Accelerometer outout is shown as mg/LSB and it outputs 16-but values for readings. The raw values from the accelerometer are multiplied by the sensitivity level to get the G value. As an exercise, lets use FD+/- 3g as the sample sensitivity level with a range from -2 to 2. The output is 16 bits; 16 bits = 65,535. This means that there are 65,535 different readings between -2g and 2g (range of 4g). 4,000-mg / 65,535 = 0.061. Each time the LSB changes by one, the value changes by 0.061.

The accelerometer and gyroscope readings are commonly combined to retrieve accurate navigation reasings (this is because the gyroscope and accelerometer readings on their own are not very accurate). A filter is employed that will give the gyroscope greater influence for short periods of time, and the accelerometer influence for longer periods of time. Gyros are measured over time which causes the calculation to drift. A complementary Filter was used in this example:

Current Angle = 0.98 * (current_angle + gyro_rotation) + (0.02 * accel_angle)

NOTE: Accelerometers cannot measure Yaw!! Yaw is when the dewvices in on a flat surface and is rotated clockwise or counter-clockwise. The z-axis readings will not change. A magnetometer can help, however the dc motors on the robot make calibration difficult.

Programs to calculate and read accelerometer and gyroscope readings can be downloaded in the movement folder.

##### Magnetometer
Can measure heading using the earth's magnetic fields as a guide. The most accurate over time, but bad at tracking sharp movements. Not used in this project. 
