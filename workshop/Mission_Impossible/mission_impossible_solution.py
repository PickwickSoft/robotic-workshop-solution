#!/usr/bin/env python3

import time
from ev3dev2.motor import OUTPUT_B, OUTPUT_D, SpeedPercent
from ev3dev2.motor import MoveSteering as PickwickCar
from ev3dev2.sensor import INPUT_1
from ev3dev2.sensor.lego import InfraredSensor
from ev3dev2.sensor import INPUT_4
from ev3dev2.sensor.lego import ColorSensor

pickwickCar = PickwickCar(OUTPUT_B, OUTPUT_D)
color_sensor = ColorSensor(INPUT_4)
infrared_sensor = InfraredSensor(INPUT_1)

MEAN_REFLECTION = 55

def stop_at_red():
    # Brake smoothly
    for speed in range(30, 0, -5):
        pickwickCar.on(calculate_steering(), SpeedPercent(speed))
        time.sleep(0.03)

    # Stop car
    pickwickCar.off()


def follow_line():
    pickwickCar.on(calculate_steering(), SpeedPercent(calculate_speed()))


def calculate_speed():
    speed = infrared_sensor.proximity - 10
    if speed < 0:
        speed = 0
    if speed > 30:
        speed = 30
    return speed


def calculate_steering():
    # Read the reflection value
    reflection = color_sensor.reflected_light_intensity

    # Calculate the steering value
    difference = MEAN_REFLECTION - reflection
    steering = difference * 4
    if steering > 100:
        steering = 100
    if steering < -100:
        steering = -100
    return steering
        

while True:
    while color_sensor.color is not ColorSensor.COLOR_GREEN:
        ...

    while True:
        follow_line()
        if color_sensor.color == ColorSensor.COLOR_RED:
            stop_at_red()
            break
    