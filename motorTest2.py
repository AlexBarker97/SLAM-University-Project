import initio, time

speed = 30
initio.init()

try:
    while True:
        keyp=input("'w','s','a','d','>','<',' ':")
        if keyp == 'w' or ord(keyp) == 16:
            initio.forward(speed)
            print ('Forward', speed)
        elif keyp == 's' or ord(keyp) == 17:
            initio.reverse(speed)
            print ('Reverse', speed)
        elif keyp == 'd' or ord(keyp) == 18:
            initio.spinRight(speed)
            print ('Spin Right', speed)
        elif keyp == 'a' or ord(keyp) == 19:
            initio.spinLeft(speed)
            print ('Spin Left', speed)
        elif keyp == '.' or keyp == '>':
            speed = min(100, speed+10)
            print ('Speed+', speed)
        elif keyp == ',' or keyp == '<':
            speed = max (0, speed-10)
            print ('Speed-', speed)
        elif keyp == ' ':
            initio.stop()
            print ('Stop')
        elif keyp == "quit":
            break
        else:
            print("invalid input")            
            print("note: 'quit' to quit")
            
except KeyboardInterrupt:
    print()

finally:
    initio.cleanup()
