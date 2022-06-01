#!/usr/bin/env python3
import imp
import serial
import subprocess
import RDefinePort

def main():  
    serString = '/dev/ttyACM' + str(RDefinePort.main(100))
    ser = serial.Serial(serString, 9600, timeout=1)
    waterLeakage = 0
    while True:
        try:
          waterLeakage = int(ser.readline(),10) # извлекаем из строки все символы, кроме служебных (по типу /r)
          print(waterLeakage)
          if (waterLeakage > 610):
            print("WATER LEAKAGE!")
            return(1)
        except:
            pass
    
if __name__ == "__main__":
    main()