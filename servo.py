# initio Motor Test
# Moves: Forward, Reverse, turn Right, turn Left, Stop - then repeat
# Press Ctrl-C to stop
#
# Writes directly to motors without using the library
#
# To check wiring is correct ensure the order of movement as above is correct
# Run using: sudo python motorTesta.py


import time, RPi.GPIO as gpio

#Motors
L1 = 19
L2 = 21
R1 = 24
R2 = 26

pan = 22

gpio.setmode(gpio.BOARD)
gpio.setup(L1, gpio.OUT)
gpio.setup(L2, gpio.OUT)
gpio.setup(R1, gpio.OUT)
gpio.setup(R2, gpio.OUT)
gpio.setup(pan, gpio.OUT)


p = gpio.PWM(pan, 366)   # frequency is 500Hz, so each pulse is 2ms wide

# main loop
try:
    while True:
        p.ChangeFrequency(366)
        p.start(50)
        print ('Centre')
        time.sleep(1)
        p.stop()
        time.sleep(3)
        p.ChangeFrequency(366)
        p.start(25)
        print ('Left')
        time.sleep(1)
        p.stop()
        time.sleep(3)
        p.ChangeFrequency(366)
        p.start(75)
        print ('Right')
        time.sleep(1)
        p.stop()
        time.sleep(3)
        
except KeyboardInterrupt:
    print()

finally:
    gpio.cleanup()
    
