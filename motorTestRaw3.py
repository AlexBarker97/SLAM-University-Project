# Writes directly to motors without using the library
# To check wiring is correct ensure the order of movement as above is correct
# Run using: sudo python motorTesta.py

import time, RPi.GPIO as gpio, initio

#Motors
L1 = 19
L2 = 21
R1 = 24
R2 = 26
#S1 = 16

gpio.setmode(gpio.BOARD)
gpio.setup(L1, gpio.OUT)
gpio.setup(L2, gpio.OUT)
gpio.setup(R1, gpio.OUT)
gpio.setup(R2, gpio.OUT)
#gpio.setup(S1, gpio.OUT)


p = gpio.PWM(L1, 20)
p.start(0)
p.ChangeDutyCycle(100)

l1 = ""
while l1 != "quit":
    l1=input('l1: ')
    if l1 != "quit":
        l2=input('l2: ')
        r1=input('r1: ')
        r2=input('r1: ')
        try:
            while True:
                gpio.output(L1, int(l1))
                gpio.output(L2, int(l2))
                gpio.output(R1, int(r1))
                gpio.output(R2, int(r2))
                print("running")
        except KeyboardInterrupt:
                print()
    else:
        gpio.cleanup()

#l1 = ""
#while l1 != "quit":
#    l1=input('servo1: ')
#    l2=input('servo2: ')
#    initio.startServos()
#    initio.setServo(1,90)

