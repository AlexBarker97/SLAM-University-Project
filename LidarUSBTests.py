import serial
import binascii

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
while True:
       result = binascii.hexlify(ser.read(8))
       result = str(result)
       result = result.replace("b'", "")
       result = result.replace("'", "")
       print(result[4:12])
       res1 = hex[result[4]]
       res2 = hex[result[5]]
       res3 = hex[result[6]]
       res4 = hex[result[7]]
       res5 = hex[result[8]]
       res6 = hex[result[9]]
       res7 = hex[result[10]]
       res8 = hex[result[11]]
       if ((str(res1) == "5") and (str(res2) == "4")):
              print(res3,res4,res5,res6,res7,res8)
