# Introduction to coding: Autonomous Driving using EV3 PickwickCars

Scientists and engineers have been working on autonomous driving for many years. The goal is to create a vehicle that can drive itself without any human intervention. This is a very challenging task, and it is still far from being achieved. However, we can already see some autonomous vehicles on the road.

In this Workshop, we will build our own self-driving vehicle using LEGO Mindstorms EV3 PickwickCars. We will use the EV3 PickwickCars to explore the basic concepts of autonomous driving. We will also learn the basics of programming in Python.

## Prerequisites

### Software

To get started, you need to have the following installed on your computer:

- Python 3
- Visual Studio Code
- PyPi package `python-ev3dev2`

We have prepared two ZIPs for you to install the prerequisites. They contain the Python 3 and Visual Studio Code installers as well as the PyPi package `python-ev3dev2` installer. You can download them here:

- Windows 10/11 (no other Windows versions): [Windows.zip](https://1drv.ms/u/s!AhoY8RtQx3DkunblHTcVyRmPZrEw?e=CTvI0U)

- MacOS: [MacOS.zip](https://1drv.ms/u/s!AhoY8RtQx3DkuneUDmsVfhwT6bC1?e=kYrBzT)

*__First unzip the ZIP file and install Python, then Visual Studio Code and finally run the `setup.bat`/`setup.sh` file__*

- Linux: We don't have a ZIP for Linux, but you can install the prerequisites using the following commands:

    ```bash
    wget https://code.visualstudio.com/sha/download?build=stable&os=linux-deb-x64

    sudo apt install ./code_*.deb

    rm code_*.deb

    sudo apt install python3-pip

    pip3 install python-ev3dev2
    ```

### VSCode plugins

- Python (by Microsoft)
- Python for EV3 (by EV3Dev)

To install the plugins, open Visual Studio Code and click on the Extensions icon in the left sidebar. You can also open the Extensions by pressing <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>X</kbd> on Windows or <kbd>Cmd</kbd>+<kbd>Shift</kbd>+<kbd>X</kbd> on MacOS

Search for the plugins and install them.

### Code

The code for the workshop is available on GitHub: [Workshop ZIP file](https://github.com/PickwickSoft/robotic-workshop/archive/refs/heads/main.zip)

Unzip the ZIP file.

Go to File -> Open Folder and select the folder `robotic-workshop-main` from the extracted ZIP file.

## Workshop Structure

The workshop is divided into four Missions. Each Mission has a number of Tasks. The Tasks are ordered in a way that you can complete them one after another.

- Getting started
  1. Get to know your PickwickCar
- Mission 1: Hit the road
    1. Drive forward and backward
    2. Steer your PickwickCar
    3. Enhance your driving/steering skills
- Mission 2 Safety systems in PickwickCars
    1. Drive to obstacle and stop
    2. Wait for obstacle to move away
    3. Avoid obstacles by driving around them
- Mission Impossible: Autonomous driving
    1. If you manage this, you are a true PickwickCar master

## Cheatsheet

### Loop

Repeating certain commands a given number of times can be simplified by using a loop.

In Python you can create one like this:

```python
for _ in range(n): # Repeat n times
    ... # Your code to be repeated n times.
```

If you need to know how many times you have already repeated the code, you can use a variable like this:

```python
for i in range(n): # Repeat n times
    print(i) # Prints 0, 1, 2, ..., n-1
    ... # Your code to be repeated n times.
```

*Note: The variable `i` is always starting at 0 and is incremented by 1 after each loop. You can use any other variable name instead of `i`.*

### Infinite loop

Repeating certain commands forever can be achieved using `while-loops` like that:.

```python
while True: # Repeat forever
    ... # Your code to be repeated forever
```

### Conditional expression

To take a decision you have to use an `if-statement`

```python
if condition:
    ... # This will run if condition is True
elif another_condition:
    ...
else:
    ...
```

Replace the conditions by logical checks. For example:

`"Python" == "Python"` is `True` (The code inside the `if` gets executed)

`"Python" == "Java"` is `False` (The code inside the `if` doesn't get executed)

`1 < 5` is `True` (The code inside the `if` gets executed)

`1 > 5` is `True` (The code inside the `if` doesn't get executed)

To make it more concrete:

```python
name = "Java"

if name == "Python":
    print("The name is Python")
elif name == "Java":
    print("The name is Java")
else:
    print("The name is unknown")
```

### Drive car at speed n

```python
# Replace n with the speed
# SpeedPercent(100) is the maximum speed of 100%
pickwickCar.on(SpeedPercent(n), SpeedPercent(n)) 
```

### Drive car for n seconds

```python
# Replace n with the number of seconds
pickwickCar.on_for_seconds(SpeedPercent(80), SpeedPercent(80), n)
```

### Turn car for n degrees

*Note: A full turn is not of __360°__ due to using wheel degrees instead of absolute pickwickCar location degrees. You have to find out yourself how many degrees your pickwickCar needs to make a certain turn*

```python
# You already know everything to turn the PickwickCar
...
```

## Further inspiration

- Acceleration and braking smoothly
- Follow me car
- Line following
- Smart car combining multiple safety features
- Color recognision
