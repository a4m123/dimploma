#!/usr/bin/env python3
import serial
import subprocess

def main():  
    ser = serial.Serial('/dev/ttyACM0',9600) 
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