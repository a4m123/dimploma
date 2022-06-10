#!/usr/bin/env python3
import serial
import time
import subprocess
import RDefinePort

def main(mustOpenValve): #0 - false (будем закрывать кран), 1 - true (будем открывать кран) 
    serString = '/dev/ttyACM0'
    serialPort = serial.Serial(serString, 9600, timeout=1)
    serialPort.reset_input_buffer()
    
    recievedLine = ""
    control = 0
    if (mustOpenValve == 0):
        print("RCV - I'm here - mOV = 0")
        while ((recievedLine != "3") or (control != 5)): # "3" - подтверждение получения микроконтроллером команды на закрытие крана
            serialPort.write(b"1\n")
            recievedLine = serialPort.readline().decode('utf-8').rstrip()
            print(recievedLine)
            control = control + 1
            time.sleep(1)
            if (recievedLine == "3"):
                serialPort.close()
                print ("return 1")
                return (1)
            if control == 5:
                serialPort.close()
                print("return -1")
                return (-1)
            

    elif (mustOpenValve == 1):
        print("RCV - I'm here - mOV = 1")
        while ((recievedLine != "5") or (control != 5)): # "5" - подтверждение получения микроконтроллером команды на закрытие крана
            serialPort.write(b"2\n")
            recievedLine = serialPort.readline().decode('utf-8').rstrip()
            print(recievedLine)
            control = control + 1
            time.sleep(1)
            if (recievedLine == "5"):
                serialPort.close()
                print ("return 2")
                return (2)
            if control == 5:
                serialPort.close()
                print ("return -2")
                return (-2)              

if __name__=='__main__':
    main()
    