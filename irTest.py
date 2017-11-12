import sys, time
import initio

initio.init()

try:
    lastL = initio.irLeft()
    lastR = initio.irRight()
#    lastLineL = initio.irLeftLine()
#    lastLineR = initio.irRightLine()
#    print ('Left, Right, LeftLine, RightLine:', lastL, lastR, lastLineL, lastLineR)
    print ('Left, Right:', lastL, lastR)
    while True:
        newL = initio.irLeft()
        newR = initio.irRight()
        print ('Left: ', newL, '  Right: ', newR)
#        newLineL = initio.irLeftLine()
#        newLineR = initio.irRightLine()
#        if (newL != lastL) or (newR != lastR) or (newLineL != lastLineL) or (newLineR != lastLineR):
#            print ('Left, Right, LeftLine, RightLine:', lastL, lastR, lastLineL, lastLineR)
#            print()
#            lastL = newL
#            lastR = newR
#            lastLineL = newLineL
#            lastLineR = newLineR
        time.sleep(0.1)
                          
except KeyboardInterrupt:
    print('... now quitting')

finally:
    initio.cleanup()
