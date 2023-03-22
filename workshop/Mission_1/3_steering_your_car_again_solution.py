#!/usr/bin/env python3

from ev3dev2.motor import OUTPUT_B, OUTPUT_D, SpeedPercent
from ev3dev2.motor import MoveTank as PickwickCar
from Data.constants import HALF_TURN

# Connect to the car and its engines
pickwickCar = PickwickCar(OUTPUT_B, OUTPUT_D)

# Repeat 3 times
for turn in range(4):
    # Drive 4 seconds forward at speed 100%
    pickwickCar.on_for_seconds(SpeedPercent(100), SpeedPercent(100), 2)

    # Turn the car by a half turn
    pickwickCar.on_for_degrees(SpeedPercent(-100), SpeedPercent(100), HALF_TURN)
