# spherov2-bb8-examples
Some additional examples and documentation of the Spereo V2 API for the legacy BB8 robot.

## the Sphero family

Sphero have created several robots that look like balls, but can be controlled to roll around, based on the sensor readings from a gyroscope. The examples on this pages are tested on the legacy model BB-8, inspired by the Star Wars movie

<html><img src=https://cdn.shopify.com/s/files/1/0306/6419/6141/files/photo-bb8-b_w.jpg?v=1713374234 height=500><br><i>The BB-8 robot from Sphero</i></html>

But in principal, it should work for each of all the [legacy](https://sphero.com/pages/legacy-products) and [current](https://sphero.com/collections/coding-robots/type_robot) Sphero robots.

## the Sphero v2 library

The installation instructions for the Sphero v2 library can found on [Sphero v2 main page](https://spherov2.readthedocs.io/en/latest/index.html) by Hanbang Wang and Elionardo Feliciano. 
To install this library for a specific version of python, instead of all versions (the requirement is >> python3.7) you could use:

`python3 -m pip install spherov2 bleak`

Note that next to the library also the bleak-library is installed; this library is used for to communicate via Bluetooth.

## finding the MAC-address of the BB-8 robot

The MAC-address is a ID-string used in all example scripts to connect to the right robots. There are are several methods to find the MAC-address of the Sphero robot.

A very visual way to do it is to download [the Sphero Edu app](https://sphero.com/pages/apps) from the Android store (not tested on other platforms). Once in the main screen, on the top right (next to settings) you see a small Sphero ball. There you can select your Robot Types. The BB-8, together with the other legacy robots, becomes visible when hit '+ show more robots'. When you bring your phone close to the robot, you can connect. Once connected you can click again on the Sphero ball to get the Connection screen, where you can see details like the firmware version and Mac Address.

A more direct textual way is to make use of the functionality of the bleak library. In the usage section of the [bleak github page](https://github.com/hbldh/bleak/) a python script is given. This script is mirrored in this repository and can be called with: 

`python3 discover_bluetooth.py | grep BB-8`

The grep is needed because all bleutooth devices in the neighbourhood are listed, the grep concentrates on the device with a name that starts with BB-8.

Another option is too look directly for bluetooth-devices with a name which start with BB-8:

`python3 find_mac_by_name.py`

Note that the script can also return <code>Device not found</code>, even when your bluetooth is on. That can be temporary, just try again. If it persist, try <code>python3 discover_bluetooth.py</code> to see which bluetooth devices are around.

## reading the sensor-values of the BB-8 robot

In [Sphero v2 API documentation](https://spherov2.readthedocs.io/en/latest/sphero_edu.html) several examples are given of how to drive the robot and control the LEDs, but for there is also functionality to read out the sensors. 
As long as the BB-8 robot has not moved, this functions return Null, but after a spin the sensors can be read out. An example of the usage of those function can be seen with this script:

`python3 show_sensor_values.py`

In this usage-example several sensor-functions are called. This is the documentation that can be found in the code:

**get_location**: Provides the location where the robot is in space (x,y) relative to the origin, in centimeters. This is not
        the distance traveled during the program, it is the offset from the origin (program start). It returns a data dictonary, with two keys:

        get_location()['x'] is the right (+) or left (-) distance from the origin of the program start, in
        centimeters.

        get_location()['y'] is the forward (+) or backward (-) distance from the origin of the program start, in
        centimeters.

**get_orientation**: Provides the tilt angle along a given axis measured by the Gyroscope, in degrees. It returns a data dictonary, with three keys:

        get_orientation()['pitch'] is the forward or backward tilt angle, from -180° to 180°.

        get_orientation()['roll'] is left or right tilt angle, from -90° to 90°.

        get_orientation()['yaw'] is the spin (twist) angle, from -180° to 180°.

**get_velocity**: Provides the velocity along a given axis measured by the motor encoders, in centimeters per second. It returns a data dictonary, with two keys:

        get_velocity()['x'] is the right (+) or left (-) velocity, in centimeters per second.

        get_velocity()['y'] is the forward (+) or back (-) velocity, in centimeters per second.

**get_acceleration**: Provides motion acceleration data along a given axis measured by the Accelerometer, in g's, where g =
        9.80665 m/s^2. It returns a data dictonary, with three keys:

        get_acceleration()['x'] is the left-to-right acceleration, from -8 to 8 g's.

        get_acceleration()['y'] is the forward-to-back acceleration, from of -8 to 8 g's.

        get_acceleration()['z'] is the upward-to-downward acceleration, from -8 to 8 g's.

**get_gyroscope**: Provides the rate of rotation around a given axis measured by the gyroscope, from -2,000° to 2,000°
        per second. It returns a data dictonary, with three keys:

        get_gyroscope().['pitch'] is the rate of forward or backward spin, from -2,000° to 2,000° per second.

        get_gyroscope().['roll'] is the rate of left or right spin, from -2,000° to 2,000° per second.

        get_gyroscope().['yaw'] is the rate of sideways spin, from -2,000° to 2,000° per second.

**get_vertical_acceleration**: This is the upward or downward acceleration regardless of the robot's orientation, from -8 to 8 g's.        

**get_heading**: Provides the target directional angle, in degrees. Assuming you aim the robot with the tail facing you,
        then 0° heading is forward, 90° is right, 180° is backward, and 270° is left.

**get_speed**: Provides the current target speed of the robot, from -255 to 255, where positive is forward, negative is
        backward, and 0 is stopped.

**get_distance**: Provides the total distance traveled in the program, in centimeters.

**get_main_led**: Provides the RGB color of the main LEDs, from 0 to 255 for each color channel.

        get_main_led().r is the red channel, from 0 - 255.

        get_main_led().g is the green channel, from 0 - 255.

        get_main_led().b is the blue channel, from 0 - 255.


        
Note that the script doesn't always connect to bluetooth. Often this is a time-out. Please try again or run script <code>python3 find_mac_by_name.py</code>.

        
