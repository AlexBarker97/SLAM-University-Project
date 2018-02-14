import initio, time, RPi.GPIO as gpio, sys, tty, termios

#Motors
pan = 22
tilt = 18

initio.init()

#def doServos():
#    initio.setServo(pan, pVal)
#    initio.setServo(tilt, tVal)
  
gpio.setmode(gpio.BOARD)
gpio.setup(pan, gpio.OUT)
p = gpio.PWM(pan, 500)   # frequency is 500Hz, so each pulse is 2ms wide
p.start(61)
gpio.setup(tilt, gpio.OUT)
t = gpio.PWM(tilt, 500)   # frequency is 500Hz, so each pulse is 2ms wide
t.start(61)

tilt = 61
duty = 61

while True:
    key = input("Use W=Up, S-Down, A-Left, D-Right, Space=Centre, 'quit','L','R'")
    if key == ' ':
        duty = 61
        p.ChangeDutyCycle(duty)
        print ("Centre: 61")
    elif key.upper() == 'R':
        duty = 0
        p.ChangeDutyCycle(duty)
        print ("Right 25")
    elif key.upper() == 'L':
        duty = 100
        p.ChangeDutyCycle(duty)
        print ("Left 90")
    elif ((key == 'd') and (duty >= 5)):
        duty -= 5
        p.ChangeDutyCycle(duty)
        print ("Right", duty)
    elif ((key == 'a') and (duty <= 95)):
        duty += 5
        p.ChangeDutyCycle(duty)
        print ("Left", duty)
    elif key == 'quit':
        initio.cleanup()
        break
    else:
        print("incorrect input")
