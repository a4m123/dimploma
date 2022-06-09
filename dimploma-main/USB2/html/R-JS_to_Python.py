import time
from USB2.RaspPi import RCloseValve

isThereWebInterruptGlobal = 0
with open('info.json') as data:
    isThereWebInterruptGlobal = data[4] 

while True:
    time.sleep(2)
    with open('info.json') as data:
        isThereWebInterrupt = data[4] 
    if (isThereWebInterrupt == isThereWebInterruptGlobal):
        print('no html button pushed')
    elif (isThereWebInterrupt != isThereWebInterruptGlobal):
        print('html button pushed')
        isThereWebInterruptGlobal = isThereWebInterrupt
        with open('info.json') as data:
            isTheValveClosed = data[1] 
        if (isTheValveClosed == 1):
            RCloseValve.main(1)
        elif (isTheValveClosed == 0):
            RCloseValve.main(0)
'''
		let dataLeakeage = JSON.parse('/var/www/html/info.json');
        if (dataLeakeage[0].closedValve == 0){
            dataLeakeage[0].closedValve = 1;
            dataLeakage[0].webInterrupt = 1;
'''