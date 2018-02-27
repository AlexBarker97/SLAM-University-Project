import time, RPi.GPIO as gpio, numpy as np, matplotlib, serial, binascii, threading, math
    


        duty -= 1
        p.ChangeDutyCycle(duty)
        if duty >= 10:
            r.append(value)
            theta.append(((duty-10)*180)/80)
            time.sleep(0.1)
        else:
            break

gpio.setwarnings(False)
gpio.setmode(gpio.BOARD)
gpio.setup(18, gpio.OUT) #pin 18 (panservo) set to output
p = gpio.PWM(18, 366)
duty = 90
p.start(duty)

While True:
    out = input('"0" = Min, "1" = Max, "+" = increase, "-" = decrease')
    if out == "0":
        duty = 10
    elif out == "1":
        duty = 90
    elif out == "+":
        duty += 1
    elif out == "-":
        duty -= 1
    elif out == "quit":
        p.stop
        break
    else:
        print("incorrect input")
    p.ChangeDutyCycle(duty)
    print("Angle =",(((duty-10)*180)/80)"
