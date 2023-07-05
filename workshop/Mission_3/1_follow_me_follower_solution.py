#!/usr/bin/env python3

from ev3dev2.motor import OUTPUT_B, OUTPUT_D, SpeedPercent
from ev3dev2.motor import MoveTank as PickwickCar
from ev3dev2.sensor import INPUT_1
from ev3dev2.sensor.lego import InfraredSensor

# Connect to the car and its engines
pickwickCar = PickwickCar(OUTPUT_B, OUTPUT_D)

# Connect to the cars infrared (distance) sensor
infrared_sensor = InfraredSensor(INPUT_1)

# Follow the object (robot) in front of the robot by adapting your speed. 
# Do not crash into the object
while True:
    speed = infrared_sensor.proximity - 10
    if(speed < 0):
        speed = 0
    pickwickCar.on(SpeedPercent(speed), SpeedPercent(speed))
