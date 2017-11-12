#!/usr/bin/python
# servoTest.py

import initio, time, RPi.GPIO as gpio

#Motors
L1 = 19
L2 = 21
R1 = 24
R2 = 26
pan = 0

gpio.setmode(gpio.BOARD)
gpio.setup(L1, gpio.OUT)
gpio.setup(L2, gpio.OUT)
gpio.setup(R1, gpio.OUT)
gpio.setup(R2, gpio.OUT)
gpio.setup(pan, gpio.OUT)

p = gpio.PWM(pan, 500)   # frequency is 500Hz, so each pulse is 2ms wide
p.start(50) # start it at 50% - should be centre of servo
#p.ChangeDutyCycle(100)

# main loop
try:
    while True:
        print ("Use Arrows or W-Up, Z-Down, A-Left, S-Right Space=Centre, ^C=Exit:")
        key = input("Use W=Up, S-Down, A-Left, D-Right, Space=Centre, ^C=Exit,'L','R'")
        if key == ' ':
#            tVal = 0
#            pVal = 0
#            doServos()
            p.ChangeDutyCycle(50)
#            print ("Centre", tVal, pVal)
            print ("Centre: 50")
        elif key.upper() == 'L':
#            tVal = -90
#            pVal = -90
#            doServos()
            p.ChangeDutyCycle(25)
#            print ("Left", tVal, pVal)
            print ("Left: 25")
        elif key.upper() == 'R':
#            tVal = 90
#            pVal = 90
#            doServos()
            p.ChangeDutyCycle(75)
#            print ("Right", tVal, pVal)
            print ("Right: 75")
        elif key == 'w':
#            pVal = min(90, pVal+10)
#            doServos()
            print ("Up (unused)")
        elif key == 'a':
#            tVal = max (-90, tVal-10)
#            doServos()
            print ("Left", tVal)
#            p.ChangeDutyCycle(25)
        elif key == 'd':
#            tVal = min(90, tVal+10)
#            doServos()
            print ("Left", tVal)
#            p.ChangeDutyCycle(75)
        elif key == 's':
#            pVal = max(-90, pVal-10)
#            doServos()
            print ("Down (unused)")
        elif ord(key) == 3:
            break
    
        p.ChangeDutyCycle(50)
        print ('Centre')
        time.sleep(3)
        p.ChangeDutyCycle(25)
        print ('Left')
        time.sleep(3)
        p.ChangeDutyCycle(75)
        print ('Right')
        time.sleep(3)

# Define pins for Pan/Tilt
pan = 0
tilt = 1
tVal = 0 # 0 degrees is centre
pVal = 0 # 0 degrees is centre

import sys
import tty
import termios

initio.init()
#print "Initio version: ", initio.version()

def doServos():
    initio.setServo(pan, pVal)
    initio.setServo(tilt, tVal)

print ("Use Arrows or W-Up, Z-Down, A-Left, S-Right Space=Centre, ^C=Exit:")
key = " "

except KeyboardInterrupt:
    print("")

finally:
    initio.cleanup()
