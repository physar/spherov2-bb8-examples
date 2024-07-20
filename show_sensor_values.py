# Arnoud Visser, July 2024
import time
from math import sqrt, sin, asin, radians, degrees, floor
from spherov2 import scanner
from spherov2.sphero_edu import SpheroEduAPI, EventType
from spherov2.types import Color

toy = scanner.find_toy()
with SpheroEduAPI(toy) as droid:
    print("Bluetooth connected")
    droid.set_main_led(Color(r=255, g=255, b=255))
    droid.spin(10,1)
    data = droid.get_location() # gives None
    #print("location x: ", data['x'], ", y: ", data['y']) # works
    print("location : ", data)
    data = droid.get_orientation() # gives None
    print("orientation :", data)
    data = droid.get_velocity()
    print("velocity: ", data)
    data = droid.get_acceleration() # gives None
    print("acceleration: ", data)
    data = droid.get_gyroscope()
    print("gyroscope: ", data)

