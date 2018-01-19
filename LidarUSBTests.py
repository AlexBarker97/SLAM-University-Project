import serial

ser = serial.Serial()
ser.port = '/dev/ttyUSB0'
ser.baudrate = 115200
ser.parity = serial.PARITY_NONE
ser.stopbits = serial.STOPBITS_ONE
ser.bytesize = serial.EIGHTBITS
ser.timeout = 10
print(ser)
ser.open()
ser.write(bytes('F', 'UTF-8'))
ser.write(bytes('T', 'UTF-8'))
ser.read(5)
ser.close()
