#!/usr/bin/env python3

import time
from ev3dev2.motor import OUTPUT_B, OUTPUT_D, SpeedPercent
from ev3dev2.motor import MoveSteering as PickwickCar
from ev3dev2.sensor import INPUT_1
from ev3dev2.sensor.lego import InfraredSensor
from ev3dev2.sensor import INPUT_4
from ev3dev2.sensor.lego import ColorSensor

pickwickCar = PickwickCar(OUTPUT_B, OUTPUT_D)
reflection_sensor = ColorSensor(INPUT_4, mode='COL-REFLECT')
color_sensor = ColorSensor(INPUT_4)
infrared_sensor = InfraredSensor(INPUT_1)


def stop_at_obstacle():
    # Don't do anything as long as there is no obstacle in front of the car
    while infrared_sensor.proximity > 20:
        ...

    # Brake smoothly
    for speed in range(100, 0, -10):
        pickwickCar.on(SpeedPercent(speed), SpeedPercent(speed))
        time.sleep(0.03)

    # Stop car
    pickwickCar.off()


def stop_at_red():
    while color_sensor.color != ColorSensor.COLOR_RED:
        ...

    # Brake smoothly
    for speed in range(100, 0, -10):
        pickwickCar.on(SpeedPercent(speed), SpeedPercent(speed))
        time.sleep(0.03)

    # Stop car
    pickwickCar.off()


def start_at_green():
    while color_sensor.color != ColorSensor.COLOR_GREEN:
        ...

    # Accelerate gradually
    for speed in range(0, 100, 10):
        pickwickCar.on(SpeedPercent(speed), SpeedPercent(speed))
        time.sleep(0.03)


def follow_line():
    while True:
        # Read the reflection value
        reflection = reflection_sensor.reflected_light_intensity

        # Calculate the steering value
        steering = (reflection - 50) / 2

        # Drive the car
        pickwickCar.on(steering, SpeedPercent(100))


def follow_front_car():
    while True:
        pickwickCar.on(SpeedPercent(infrared_sensor.proximity), SpeedPercent(infrared_sensor.proximity))
        

pickwickCar.on(SpeedPercent(100), SpeedPercent(100))
stop_at_obstacle()
stop_at_red()
start_at_green()
follow_line()
follow_front_car()
