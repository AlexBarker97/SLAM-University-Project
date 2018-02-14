import RPi.GPIO as gpio, time

#pins
pan = 22

gpio.setmode(gpio.BOARD)
gpio.setup(pan, gpio.OUT)
p = gpio.PWM(pan, 366)
duty = 50
p.start(duty)

while True:
    key = input("Use W=Up, S-Down, A-Left, D-Right, Space=Centre, 'quit','L','R'")
    if key == ' ':
        duty = 50
        p.ChangeDutyCycle(duty)
        print ("Centre")
    elif key.upper() == 'R':
        duty = 75
        p.ChangeDutyCycle(duty)
        print ("Right")
    elif key.upper() == 'L':
        duty = 25
        p.ChangeDutyCycle(duty)
        print ("Left")
    elif ((key == 'a') and (duty >= 5)):
        duty -= 5
        p.ChangeDutyCycle(duty)
        print ("Right", duty)
    elif ((key == 'd') and (duty <= 95)):
        duty += 5
        p.ChangeDutyCycle(duty)
        print ("Left", duty)
    elif key == 'quit':
        p.stop()
        break
    else:
        print("incorrect input")
