#!/usr/bin/env python3
import serial
import time
import subprocess

def main():
    ser = serial.Serial('/dev/ttyACM2', 9600, timeout=1)
    ser.reset_input_buffer()
    
    line = ""
    control = 0
    while ((line != "3") or (control != 5)): #3-confirmaton of recieved code by Arduino to close valve 
        ser.write(b"1\n")
        line = ser.readline().decode('utf-8').rstrip()
        print(line)
        control = control + 1
        time.sleep(1)
        if (line == "3"):
            return (1)
        if control == 1000:
            return (-1)

    

if __name__=='__main__':
    main()

    