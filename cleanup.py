import serial, initio
ser = serial.Serial()
ser.close()
initio.init()
initio.cleanup()
print("Cleanup Complete...")
