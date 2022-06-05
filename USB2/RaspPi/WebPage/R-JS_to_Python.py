import time
from USB2.RaspPi import RCloseValve

isThereWebInterruptGlobal = 0
with open('info.json') as data:
    isThereWebInterruptGlobal = data[4] 

while True:
    time.sleep(4)
    with open('info.json') as data:
        isThereWaterLeakage = data[4] 
    if (isThereWaterLeakage != isThereWebInterruptGlobal):
        isThereWebInterruptGlobal = isThereWaterLeakage
        with open('info.json') as data:
            wasTheValveClosed = data[1] 
        if (wasTheValveClosed == 1):
            RCloseValve.main(1)
        elif (wasTheValveClosed == 0):
            RCloseValve.main(0)
