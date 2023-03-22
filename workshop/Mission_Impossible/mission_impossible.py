#!/usr/bin/env python3

from ev3dev2.motor import OUTPUT_B, OUTPUT_D, SpeedPercent
from ev3dev2.motor import MoveTank as PickwickCar
from ev3dev2.sensor import INPUT_1
from ev3dev2.sensor.lego import InfraredSensor
from ev3dev2.sensor import INPUT_4
from ev3dev2.sensor.lego import ColorSensor

# TODO: Stop smoothly at obstacle (and beep)
# TODO: Stop smoothly on red color
# TODO: Start smoothly on green and accelerate gradualy
# TODO: Follow the line
# TODO: Follow the front car
