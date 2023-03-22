#!/usr/bin/env python3

import time
from ev3dev2.motor import OUTPUT_B, OUTPUT_D, SpeedPercent
from ev3dev2.motor import MoveTank as PickwickCar
from ev3dev2.sensor import INPUT_1
from ev3dev2.sensor.lego import InfraredSensor

# Connect to the car and its engines
pickwickCar = PickwickCar(OUTPUT_B, OUTPUT_D)

# Connect to the cars infrared (distance) sensor
sensor = InfraredSensor(INPUT_1)

# Start car
pickwickCar.on(SpeedPercent(100), SpeedPercent(100))

# Don't do anything as long as there is no obstacle in front of the car
while sensor.proximity > 20:
    ...

# Obstacle in front of car

# Brake smoothly (Todo 2)
for speed in range(100, 0, -10):
    pickwickCar.on(SpeedPercent(speed), SpeedPercent(speed))
    time.sleep(0.03)

# Stop car
pickwickCar.off()
