import serial
import binascii

hex2dec = {"0":0,  "1":1,  "2":2,  "3":3,
       "4":4,  "5":5,  "6":6,  "7":7,
       "8":8,  "9":9,  "a":10, "b":11,
       "c":12, "d":13, "e":14, "f":15}

ser = serial.Serial()
ser.close()
ser.port = '/dev/ttyUSB0'
ser.baudrate = 115200
ser.parity = serial.PARITY_NONE
ser.stopbits = serial.STOPBITS_ONE
ser.bytesize = serial.EIGHTBITS
ser.timeout = 10
ser.open()
ser.write(bytes('P', 'UTF-8'))
ser.write(bytes('T', 'UTF-8'))

While True:
       state1 = 0
       state2 = 0
       value = 0
       result = binascii.hexlify(ser.read())
       result = str(result)
       print(result)
       print(result[2])
       res0 = hex2dec[result[2]]
       print(res0)
       res1 = hex2dec[result[3]]
       res2 = hex2dec[result[4]]
       res3 = hex2dec[result[5]]
       res4 = hex2dec[result[6]]
       res5 = hex2dec[result[7]]
       res6 = hex2dec[result[8]]
       res7 = hex2dec[result[9]]
              if ((str(res0) == "5") and (str(res1) == "4")):
                     value = value + (res2*(16**6)) + (res3*(16**5)) + (res4*(16**4)) + (res5*(16**3)) + (res6*(16**2)) + (res7*(16**1)) + (res8*(16**0))
              else:
                     ser.close()
                     ser.port = '/dev/ttyUSB0'
                     ser.baudrate = 115200
                     ser.parity = serial.PARITY_NONE
                     ser.stopbits = serial.STOPBITS_ONE
                     ser.bytesize = serial.EIGHTBITS
                     ser.timeout = 10
                     ser.open()
                     ser.write(bytes('P', 'UTF-8'))
                     ser.write(bytes('T', 'UTF-8'))
