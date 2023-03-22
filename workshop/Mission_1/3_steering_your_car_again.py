#!/usr/bin/env python3

from ev3dev2.motor import OUTPUT_B, OUTPUT_D, SpeedPercent
from ev3dev2.motor import MoveTank as PickwickCar
from Data.constants import HALF_TURN

# Connect to the car and its engines
pickwickCar = PickwickCar(OUTPUT_B, OUTPUT_D)

# TODO: Drive forward for 2 seconds turn the car by 180° and drive to the initial position, 
# where you park it with the original orientation. Try to repeat this n times (n being a number of your choice)
# TODO: Avoid code duplication!