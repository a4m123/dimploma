#!/usr/bin/env python3
import serial
import time
import subprocess
import RDefinePort

def main(mustOpenValve): #0 - false (будем закрывать кран), 1 - true (будем открывать кран) 
    serString = '/dev/ttyACM0'
    ser = serial.Serial(serString, 9600, timeout=1)
    ser.reset_input_buffer()
    
    line = ""
    control = 0
    if (mustOpenValve == 0):
        print("RCV - I'm here - mOV = 0")
        while ((line != "3") or (control != 5)): #3-confirmaton of recieved code by Arduino to close valve 
            ser.write(b"1\n")
            line = ser.readline().decode('utf-8').rstrip()
            print(line)
            control = control + 1
            time.sleep(1)
            if (line == "3"):
                #ser.close()
                print ("return 1")
                return (1)
            if control == 5:
                #ser.close()
                print("return -1")
                return (-1)
            

    elif (mustOpenValve == 1):
        print("RCV - I'm here - mOV = 1")
        while ((line != "5") or (control != 5)): #4-confirmaton of recieved code by Arduino to open valve
            ser.write(b"2\n")
            line = ser.readline().decode('utf-8').rstrip()
            print(line)
            control = control + 1
            time.sleep(1)
            if (line == "5"):
                #ser.close()
                print ("return 2")
                return (2)
            if control == 5:
                #ser.close()
                print ("return -2")
                
                return (-2)              

if __name__=='__main__':
    main()
    