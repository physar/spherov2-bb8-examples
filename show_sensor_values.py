# Arnoud Visser, July 2024

import time
from math import sqrt, sin, asin, radians, degrees, floor
from spherov2 import scanner
from spherov2.sphero_edu import SpheroEduAPI, EventType
from spherov2.types import Color

toy = scanner.find_toy()
try:
  with SpheroEduAPI(toy) as droid:
    print("Bluetooth connected")
    droid.set_main_led(Color(r=255, g=255, b=255))
    droid.spin(10,1) # sensor reading gives None without spin
    data = droid.get_location() 
    #print("location x: ", data['x'], ", y: ", data['y']) # works
    print("location : ", data)
    data = droid.get_orientation() 
    print("orientation :", data)
    data = droid.get_velocity()
    print("velocity: ", data)
    data = droid.get_acceleration() 
    print("acceleration: ", data)
    data = droid.get_gyroscope()
    print("gyroscope: ", data)
    data = droid.get_heading()
    print("heading: ", data)
    data = droid.get_speed()
    print("speed: ", data)
    data = droid.get_distance()
    print("distance: ", data)
    data = droid.get_vertical_acceleration() 
    print("vertical acceleration: ", data)
    data = droid.get_main_led()
    print("main-led: ", data)
except Exception:
  print("Making a Bluetooth failed. Try again or run 'python3 find_mac_by_name.py'")
  pass

