#!/usr/bin/env python3

from ev3dev2.motor import OUTPUT_B, OUTPUT_D, SpeedPercent
from ev3dev2.motor import MoveTank as PickwickCar
from ev3dev2.sensor import INPUT_1
from ev3dev2.sensor.lego import InfraredSensor

# Connect to the car and its engines
pickwickCar = PickwickCar(OUTPUT_B, OUTPUT_D)

# Connect to the cars infrared (distance) sensor
sensor = InfraredSensor(INPUT_1)

# Start the car
pickwickCar.on(SpeedPercent(100), SpeedPercent(100))

# Don't do anything as long as there is no obstacle in front of the car
while sensor.proximity > 20:
    ...

# Obstacle in front of car. Stop car.
pickwickCar.off()

# Don't do anything as long as the obstacle is in front of the car
while sensor.proximity <= 25:
    ...

pickwickCar.on(SpeedPercent(100), SpeedPercent(100))

while True:
    ...
