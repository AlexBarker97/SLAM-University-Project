import RPi.GPIO as gpio, time

#pins
pan = 18
tilt = 22

gpio.setmode(gpio.BOARD)
gpio.setup(pan, gpio.OUT)
gpio.setup(tilt, gpio.OUT)
p = gpio.PWM(pan, 366)
t = gpio.PWM(tilt, 366)
vduty = 50
hduty = 50
p.start(hduty)
t.start(vduty)

while True:
    key = input("Use W=Up, S-Down, A-Left, D-Right, Space=Centre, 'quit','L','R'")
    if key == ' ':
        hduty = 50
    elif key.upper() == 'R':
        hduty = 75
        p.ChangeDutyCycle(hduty)
    elif key.upper() == 'L':
        hduty = 25
        p.ChangeDutyCycle(hduty)
    elif ((key == 'a') and (duty >= 5)):
        hduty -= 5
        p.ChangeDutyCycle(hduty)
    elif ((key == 'd') and (duty <= 95)):
        hduty += 5
        p.ChangeDutyCycle(hduty)
    elif ((key == 'w') and (duty >= 5)):
        vduty -= 5
        p.ChangeDutyCycle(vduty)
    elif ((key == 's') and (duty <= 95)):
        vduty += 5
        p.ChangeDutyCycle(vduty)
    elif key == 'quit':
        p.stop()
        break  
    else:
        print("incorrect input")
    print ("pan: ", hduty,"  tilt: ",vduty)   
