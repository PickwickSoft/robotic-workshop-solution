#!/usr/bin/env python3

from ev3dev2.motor import OUTPUT_B, OUTPUT_D, SpeedPercent
from ev3dev2.motor import MoveTank as PickwickCar

# Connect to the car and its engines
pickwickCar = PickwickCar(OUTPUT_B, OUTPUT_D)

# Drive forward for 4 seconds and then backward to the initial position
pickwickCar.on_for_seconds(SpeedPercent(100), SpeedPercent(100), 4)

# Driving backwards can be achieved using negative speed values
pickwickCar.on_for_seconds(SpeedPercent(-100), SpeedPercent(-100), 4)
