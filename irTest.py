import sys, time
import initio

initio.init()

try:
    lastL = initio.irLeft()
    lastR = initio.irRight()
    print ('Left, Right:', lastL, lastR)
    while True:
        newL = initio.irLeft()
        newR = initio.irRight()
        print ('Left: ', newL, '  Right: ', newR)
        time.sleep(0.1)
                          
except KeyboardInterrupt:
    print('... now quitting')

finally:
    initio.cleanup()
