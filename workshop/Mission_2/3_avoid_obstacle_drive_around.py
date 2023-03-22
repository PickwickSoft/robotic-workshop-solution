#!/usr/bin/env python3

from ev3dev2.motor import OUTPUT_B, OUTPUT_D, SpeedPercent
from ev3dev2.motor import MoveTank as PickwickCar
from ev3dev2.sensor import INPUT_1
from ev3dev2.sensor.lego import InfraredSensor

# Connect to the car and its engines
pickwickCar = PickwickCar(OUTPUT_B, OUTPUT_D)

# TODO: Drive forward until you "see" an obstacle and avoid it by driving around it
