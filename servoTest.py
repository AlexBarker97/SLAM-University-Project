import initio, time, RPi.GPIO as gpio, sys, tty, termios

#pins
pan = 22

initio.init()
  
gpio.setmode(gpio.BOARD)
gpio.setup(pan, gpio.OUT)
p = gpio.PWM(pan, 500)
duty = 50
p.start(duty)

while True:
    key = input("Use W=Up, S-Down, A-Left, D-Right, Space=Centre, 'quit','L','R'")
    if key == ' ':
        duty = 50
        p.ChangeDutyCycle(duty)
        print ("Centre")
    elif key.upper() == 'R':
        duty = 100
        p.ChangeDutyCycle(duty)
        print ("Right")
    elif key.upper() == 'L':
        duty = 0
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
        initio.cleanup()
        break
    else:
        print("incorrect input")
