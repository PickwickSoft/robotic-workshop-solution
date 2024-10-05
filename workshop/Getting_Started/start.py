#!/usr/bin/env python3
# Here you learn how a Mission is structured and how to control your PickwickCar

import time
from ev3dev2.motor import OUTPUT_B, OUTPUT_D, SpeedPercent
from ev3dev2.motor import MoveTank as PickwickCar

# Connect to the car and its engines
pickwickCar = PickwickCar(OUTPUT_B, OUTPUT_D)

# TODO: Drive forward forever
... # Normally your solution comes here

# You will get the solution for each Mission after trying everything out.
# For this Getting Started Mission you get it directly! Have fun!
pickwickCar.on(SpeedPercent(100), SpeedPercent(100))

# Sleep 1 sec
time.sleep(1)

# TODO: Stop the running car
... # Normally your solution comes here

# You will get the solution for each Mission after trying everything out.
# For this Getting Started Mission you get it directly! Have fun!
pickwickCar.off()

time.sleep(1)

# TODO: Drive forward for 4 seconds at speed 100%
... # Normally your solution comes here

# You will get the solution for each Mission after trying everything out.
# For this Getting Started Mission you get it directly! Have fun!
pickwickCar.on_for_seconds(SpeedPercent(100), SpeedPercent(100), 4)
