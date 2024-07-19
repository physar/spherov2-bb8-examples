# spherov2-bb8-examples
Some additional examples and documentation of the Spereo V2 API for the legacy BB8 robot.

## the Sphero family

Sphero have created several robots that look like balls, but can be controlled to roll around, based on the sensor readings from a gyroscope. The examples on this pages are tested on the legacy model BB-8, inspired by the Star Wars movie

<html><img src=https://cdn.shopify.com/s/files/1/0306/6419/6141/files/photo-bb8-b_w.jpg?v=1713374234 height=500><br><i>The BB8-robot from Sphero</i></html>

But in principal, it should work for each of all the [legacy](https://sphero.com/pages/legacy-products) and [current](https://sphero.com/collections/coding-robots/type_robot) Sphero robots.

## the Sphero v2 library

The installation instructions for the Sphero v2 library can found on [Sphero v2 main page](https://spherov2.readthedocs.io/en/latest/index.html) by Hanbang Wang and Elionardo Feliciano. 
To install this library for a specific version of python, instead of all versions (the requirement is >> python3.7) you could use:

`python3 -m pip install spherov2 bleak`

Note that next to the library also the bleak-library is installed; this library is used for to communicate via Bluetooth.

## finding the MAC-address of the Sphero robot

The MAC-address is a ID-string used in all example scripts to connect to the right robots. There are are several methods to find the MAC-address of the Sphero robot.
