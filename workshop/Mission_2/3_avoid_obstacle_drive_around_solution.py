#!/usr/bin/env python3

from ev3dev2.motor import OUTPUT_B, OUTPUT_D, SpeedPercent
from ev3dev2.motor import MoveTank as PickwickCar
from ev3dev2.sensor import INPUT_1
from ev3dev2.sensor.lego import InfraredSensor
from Data.constants import QUARTER_TURN

# Connect to the car and its engines
pickwickCar = PickwickCar(OUTPUT_B, OUTPUT_D)

# Connect to the cars infrared (distance) sensor
sensor = InfraredSensor(INPUT_1)

while True:
    # Start car
    pickwickCar.on(SpeedPercent(100), SpeedPercent(100))

    # Don't do anything as long as there is no obstacle in front of the car
    while sensor.proximity > 20:
        ...

    while True:
        pickwickCar.on_for_degrees(SpeedPercent(100), SpeedPercent(-100), QUARTER_TURN)

        pickwickCar.on_for_rotations(SpeedPercent(60), SpeedPercent(60), 2)

        pickwickCar.on_for_degrees(SpeedPercent(-100), SpeedPercent(100), QUARTER_TURN)

        if sensor.proximity:
            break
