#!/usr/bin/python
# servoTest.py

import initio, time, RPi.GPIO as gpio, sys, tty, termios

#Motors
L1 = 19
L2 = 21
R1 = 24
R2 = 26
pan = 22
tilt = 23
#tVal = 0 # 0 degrees is centre
#pVal = 0 # 0 degrees is centre

initio.init()

#def doServos():
#    initio.setServo(pan, pVal)
#    initio.setServo(tilt, tVal)

gpio.setmode(gpio.BOARD)
gpio.setup(L1, gpio.OUT)
gpio.setup(L2, gpio.OUT)
gpio.setup(R1, gpio.OUT)
gpio.setup(R2, gpio.OUT)
gpio.setup(pan, gpio.OUT)
p = gpio.PWM(pan, 500)   # frequency is 500Hz, so each pulse is 2ms wide
p.start(61)
gpio.setup(tilt, gpio.OUT)
t = gpio.PWM(tilt, 500)   # frequency is 500Hz, so each pulse is 2ms wide
t.start(61)

tilt = 61
duty = 61

#try:
while True:
    key = input("Use W=Up, S-Down, A-Left, D-Right, Space=Centre, 'quit','L','R'")
    if key == ' ':
#            tVal = 0
#            pVal = 0
#            doServos()
        duty = 61
        p.ChangeDutyCycle(duty)
#            print ("Centre", tVal, pVal)
        print ("Centre: 61")
    elif key.upper() == 'R':
#            tVal = -90
#            pVal = -90
#            doServos()
        duty = 25
        p.ChangeDutyCycle(duty)
#            print ("Right", tVal, pVal)
        print ("Right 25")
    elif key.upper() == 'L':
#            tVal = 90
#            pVal = 90
#            doServos()
        duty = 90
        p.ChangeDutyCycle(duty)
#            print ("Left", tVal, pVal)
        print ("Left 90")
    elif key == 'w':
#            pVal = min(90, pVal+10)
#            doServos()
        tilt += 5
        print ("Up", tilt)
        t.ChangeDutyCycle(tilt)
    elif key == 'd':
#            tVal = max (-90, tVal-10)
#            doServos()
        duty -= 5
        print ("Right", duty)
        p.ChangeDutyCycle(duty)
    elif key == 'a':
#            tVal = min(90, tVal+10)
#            doServos()
        duty += 5
        print ("Left", duty)
        p.ChangeDutyCycle(duty)
    elif key == 's':
#            pVal = max(-90, pVal-10)
#            doServos()
        tilt -= 5
        print ("Down", tilt)
        t.ChangeDutyCycle(tilt)
    elif key == 'quit':
        initio.cleanup()
        break
    else:
        print("incorrect input")
#except KeyboardInterrupt:
#    print("")
#finally:
