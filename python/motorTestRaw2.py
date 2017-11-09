# Writes directly to motors without using the library
# To check wiring is correct ensure the order of movement as above is correct
# Run using: sudo python motorTesta.py

import time, RPi.GPIO as gpio

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

i = "a"
while i != "quit":
    i=input('giff input: ')
    if i == "forward":
        try:
            while True:
                gpio.output(L1, 0)
                gpio.output(L2, 0)
                gpio.output(R1, 1)
                gpio.output(R2, 1)
                print("forward")
        except KeyboardInterrupt:
                print()
    if i == "backward":
        gpio.output(L1, 1)
        gpio.output(L2, 0)
        gpio.output(R1, 0)
        gpio.output(R2, 1)
        print("backward")
    if i == "right":
        gpio.output(L1, 1)
        gpio.output(L2, 0)
        gpio.output(R1, 1)
        gpio.output(R2, 1)
        print("right")
    if i == "left":
        gpio.output(L1, 0)
        gpio.output(L2, 1)
        gpio.output(R1, 0)
        gpio.output(R2, 1)
        print("left")
    if i == "stop":
        gpio.output(L1, 0)
        gpio.output(L2, 1)
        gpio.output(R1, 1)
        gpio.output(R2, 0)
        print("stop")

gpio.cleanup()
    
