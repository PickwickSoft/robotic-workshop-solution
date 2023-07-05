#!/usr/bin/env python3

import random
import time
from ev3dev2.motor import OUTPUT_B, OUTPUT_D, SpeedPercent
from ev3dev2.motor import MoveTank as PickwickCar

# Connect to the car and its engines
pickwickCar = PickwickCar(OUTPUT_B, OUTPUT_D)


# Front car (Follow-me car). Should change speed to random 
# values at random intervals
while True:
    speed = random.randint(0, 100)
    pickwickCar.on(SpeedPercent(speed), SpeedPercent(speed))
    time.sleep(random.randint(1, 4))
