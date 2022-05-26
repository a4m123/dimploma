#!/usr/bin/env python3
import serial
import subprocess
import RListenWater, RCloseValve, RSendEMail

def main():  
    ser = serial.Serial('/dev/ttyACM2',9600) 
    counterPeople = -1
    resultCloseValve = 0
    resultSendMail = 0
    flag = 0
    while True:
        try:
          counterPeople = int(ser.readline(),10) # извлекаем из строки все символы, кроме служебных (по типу /r)
          print(counterPeople)
          if (counterPeople > 0):
            if (flag == 1):
                resultCloseValve = RCloseValve.main(1)
                resultSendMail = RSendEMail.main(20)
            flag == 0
          elif (counterPeople == 0):
              if (flag == 0):
                  flag = 1
                  resultCloseValve = RCloseValve.main(0)
                  if (resultCloseValve == 1):
                      resultSendMail = RSendEMail.main(10)
                  elif (resultCloseValve == -1):
                      resultSendMail = RSendEMail.main(11)

        except:
            pass
    
if __name__ == "__main__":
    main()