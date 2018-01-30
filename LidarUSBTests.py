import serial
import binascii

hex = {"0":0,  "1":1,  "2":2,  "3":3,
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

res1 = "5"
res2 = "4"
       while ((str(res1) == "5") and (str(res2) == "4")):
              value = 0
              result = binascii.hexlify(ser.read())
              print(ser.read())
              print(result)
              result = str(result)
              result = result.replace("'", "")
              print(result[1:9])
              res0 = hex[result[1]]
              res1 = hex[result[2]]
              res2 = hex[result[3]]
              res3 = hex[result[4]]
              res4 = hex[result[5]]
              res5 = hex[result[6]]
              res6 = hex[result[7]]
              res7 = hex[result[8]]
              if ((str(res1) == "5") and (str(res2) == "4")):
                     value = value + (res2*(16**6)) + (res3*(16**5)) + (res4*(16**4)) + (res5*(16**3)) + (res6*(16**2)) + (res7*(16**1)) + (res8*(16**0))
                     print(value/760)
              else:
                     StartSer()
