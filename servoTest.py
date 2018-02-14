import RPi.GPIO as gpio

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
        p.stop()
    elif key.upper() == 'R':
        duty = 75
        p.ChangeDutyCycle(duty)
        print ("Right")
        p.stop()
    elif key.upper() == 'L':
        duty = 25
        p.ChangeDutyCycle(duty)
        print ("Left")
        p.stop()
    elif ((key == 'a') and (duty >= 5)):
        duty -= 5
        p.ChangeDutyCycle(duty)
        print ("Right", duty)
        p.stop()
    elif ((key == 'd') and (duty <= 95)):
        duty += 5
        p.ChangeDutyCycle(duty)
        print ("Left", duty)
        p.stop()
    elif key == 'quit':
        p.stop()
        break
    else:
        print("incorrect input")
