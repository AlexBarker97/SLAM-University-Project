import initio, time, RPi.GPIO as gpio, sys, tty, termios

#Motors
pan = 22
tilt = 18

initio.init()

def setServoPos(angle):
    p.ChangeDutyCycle((((angle+90)/180)+1)/20)
    print((((angle+90)/180)+1))

#def doServos():
    #initio.setServo((((pan+90)/180)+1), pVal)
    #initio.setServo(tilt, tVal)

gpio.setmode(gpio.BOARD)
gpio.setup(pan, gpio.OUT)
p = gpio.PWM(pan, 50)   # frequency is 500Hz, so each pulse is 2ms wide
p.start(0)
gpio.setup(tilt, gpio.OUT)
t = gpio.PWM(tilt, 50)   # frequency is 500Hz, so each pulse is 2ms wide
t.start(0)

duty = 0
angle = 0

while True:
    key = input("Use W=Up, S-Down, A-Left, D-Right, Space=Centre, 'quit','L','R'")
    if key == ' ':
        angle = 0
        setServoPos(angle)
        #p.ChangeDutyCycle(duty)
        print ("Centre")
    elif key.upper() == 'R':
        angle = 1000
        setServoPos(angle)
        #p.ChangeDutyCycle(duty)
        print ("Right")
    elif key.upper() == 'L':
        angle = -90
        setServoPos(angle)
        #p.ChangeDutyCycle(duty)
        print ("Left")
    elif key == 'w':
        #tilt += 5
        print ("Up (commented)", tilt)
        #t.ChangeDutyCycle(tilt)
    elif key == 'd':
        angle += 5
        print ("Right")
        setServoPos(angle)
        #p.ChangeDutyCycle(duty)
    elif key == 'a':
        angle -= 5
        print ("Left")
        setServoPos(angle)
        #p.ChangeDutyCycle(duty)
    elif key == 's':
        #tilt -= 5
        print ("Down, commented", tilt)
        #t.ChangeDutyCycle(tilt)
    elif key == 'quit':
        initio.cleanup()
        break
    else:
        print("incorrect input")
