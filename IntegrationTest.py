import serial, binascii, initio, time

ser = serial.Serial()
ser.port = '/dev/ttyUSB0'
ser.baudrate = 115200
ser.parity = serial.PARITY_NONE
ser.stopbits = serial.STOPBITS_ONE
ser.bytesize = serial.EIGHTBITS
ser.timeout = 10
ser.open()
ser.write(bytes('P', 'UTF-8'))
ser.write(bytes('T', 'UTF-8'))
hex = {"0":0,  "1":1,  "2":2,  "3":3,
       "4":4,  "5":5,  "6":6,  "7":7,
       "8":8,  "9":9,  "a":10, "b":11,
       "c":12, "d":13, "e":14, "f":15}
initio.init()
speed = 50
try:
       while True:
              value = 0
              result = binascii.hexlify(ser.read(8))
              result = str(result)
              result = result.replace("b'", "")
              result = result.replace("'", "")
              #print(result[4:12])
              res1 = hex[result[4]]
              res2 = hex[result[5]]
              res3 = hex[result[6]]
              res4 = hex[result[7]]
              res5 = hex[result[8]]
              res6 = hex[result[9]]
              res7 = hex[result[10]]
              res8 = hex[result[11]]
              if ((str(res1) == "5") and (str(res2) == "4")):
                     value= value + (res3*(16**5)) + (res4*(16**4)) + (res5*(16**3)) + (res6*(16**2)) + (res7*(16**1)) + (res8)
              print(value/760)
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
              if (value/760) < 100:
                     initio.reverse(20)
                     print ('Wall Detected')
            
except KeyboardInterrupt:
    print()

finally:
    initio.cleanup()
