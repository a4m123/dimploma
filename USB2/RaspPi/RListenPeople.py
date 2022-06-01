#!/usr/bin/env python3
import serial
import json
import subprocess
import RListenWater, RCloseValve, RSendEMail, RDefinePort

def main():  
    serString = '/dev/ttyACM' + str(RDefinePort.main(200))
    ser = serial.Serial(serString, 9600, timeout=1)
    counterPeople = -1
    resultCloseValve = 0
    resultSendMail = 0
    flag = 0
    while True:
        try:
          counterPeople = int(ser.readline(),10) # извлекаем из строки все символы, кроме служебных (по типу /r)
          print(counterPeople)
          if (counterPeople > 0):
            with open('info.json') as data:
                isThereWaterLeakage = data[1] 
            if (isThereWaterLeakage == 0):
                if (flag == 1):
                    resultCloseValve = RCloseValve.main(1)
                    resultSendMail = RSendEMail.main(20)
                flag == 0
            elif(isThereWaterLeakage == 1):
                pass
          elif (counterPeople == 0):
              if (flag == 0):
                  flag = 1
                  resultCloseValve = RCloseValve.main(0)
                  if (resultCloseValve == 1):
                      resultSendMail = RSendEMail.main(10)
                  elif (resultCloseValve == -1):
                      resultSendMail = RSendEMail.main(11)
          
          information = {'waterLeakage': resultWaterLeakage, 'closedValve': resultCloseValve, 'sendedMail': resultSendMail}
          infoFile = open("info.json", "w")
          json.dump(information, infoFile)
        
            
        except:
            pass
    
if __name__ == "__main__":
    main()