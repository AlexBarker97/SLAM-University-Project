# Writes directly to motors without using the library
# To check wiring is correct ensure the order of movement as above is correct
# Run using: sudo python motorTesta.py

import time, RPi.GPIO as gpio, initio

#Motors
L1 = 19

gpio.setmode(gpio.BOARD)
gpio.setup(L1, gpio.OUT)

p = gpio.PWM(L1, 20)
p.start(0)
p.ChangeDutyCycle(100)

try:
    while True:
        gpio.output(L1, 1)
        print("running")
except KeyboardInterrupt:
    gpio.cleanup()
