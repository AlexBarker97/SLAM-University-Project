#!/usr/bin/python
# servoTest.py

import initio, time, RPi.GPIO as gpio, sys, tty, termios

#Motors
pan = 22
tilt = 18

initio.init()

def doServos():
    initio.setServo(pan, pVal)
    initio.setServo(tilt, tVal)

gpio.setmode(gpio.BOARD)
gpio.setup(pan, gpio.OUT)
p = gpio.PWM(pan, 500)   # frequency is 500Hz, so each pulse is 2ms wide
p.start(61)
gpio.setup(tilt, gpio.OUT)
t = gpio.PWM(tilt, 500)   # frequency is 500Hz, so each pulse is 2ms wide
t.start(61)

tilt = 61
duty = 61

while True:
    key = input("Use W=Up, S-Down, A-Left, D-Right, Space=Centre, 'quit','L','R'")
    if key == ' ':
        pVal = 61
        doServos()
        #duty = 61
        #p.ChangeDutyCycle(duty)
        print ("Centre: 61")
    elif key.upper() == 'R':
        duty = 25
        p.ChangeDutyCycle(duty)
        print ("Right 25")
    elif key.upper() == 'L':
        duty = 90
        p.ChangeDutyCycle(duty)
        print ("Left 90")
    elif key == 'w':
        tilt += 5
        print ("Up", tilt)
        t.ChangeDutyCycle(tilt)
    elif key == 'd':
        duty -= 5
        print ("Right", duty)
        p.ChangeDutyCycle(duty)
    elif key == 'a':
        duty += 5
        print ("Left", duty)
        p.ChangeDutyCycle(duty)
    elif key == 's':
        tilt -= 5
        print ("Down", tilt)
        t.ChangeDutyCycle(tilt)
    elif key == 'quit':
        initio.cleanup()
        break
    else:
        print("incorrect input")
