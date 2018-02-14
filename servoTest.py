import RPi.GPIO as gpio, time

#pins
pan = 22

gpio.setmode(gpio.BOARD)
gpio.setup(pan, gpio.OUT)
p = gpio.PWM(pan, 366)
duty = 50

while True:
    key = input("Use W=Up, S-Down, A-Left, D-Right, Space=Centre, 'quit','L','R'")
    p.start(50)
    if key == ' ':
        duty = 50
        p.ChangeDutyCycle(duty)
        print ("Centre")
        time.sleep(0.1)
        p.stop()
    elif key.upper() == 'R':
        duty = 75
        p.ChangeDutyCycle(duty)
        print ("Right")
        time.sleep(0.1)
        p.stop()
    elif key.upper() == 'L':
        duty = 25
        p.ChangeDutyCycle(duty)
        print ("Left")
        time.sleep(0.1)
        p.stop()
    elif ((key == 'a') and (duty >= 5)):
        duty -= 5
        p.ChangeDutyCycle(duty)
        print ("Right", duty)
        time.sleep(0.1)
        p.stop()
    elif ((key == 'd') and (duty <= 95)):
        duty += 5
        p.ChangeDutyCycle(duty)
        print ("Left", duty)
        time.sleep(0.1)
        p.stop()
    elif key == 'quit':
        p.stop()
        break
    else:
        print("incorrect input")
