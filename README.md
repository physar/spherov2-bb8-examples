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

## finding the MAC-address of the Sphero robot

The MAC-address is a ID-string used in all example scripts to connect to the right robots. There are are several methods to find the MAC-address of the Sphero robot.

A very visual way to do it is to download [the Sphero Edu app](https://sphero.com/pages/apps) from the Android store (not tested on other platforms). Once in the main screen, on the top right (next to settings) you see a small Sphero ball. There you can select your Robot Types. The BB-8, together with the other legacy robots, becomes visible when hit '+ show more robots'. When you bring your phone close to the robot, you can connect. Once connected you can click again on the Sphero ball to get the Connection screen, where you can see details like the firmware version and Mac Address.

A more direct textual way is to make use of the functionality of the bleak library. In the usage section of the [bleak github page](https://github.com/hbldh/bleak/) a python script is given. This script is mirrored in this repository and can be called with 

`python3 discover_bluetooth.py`

