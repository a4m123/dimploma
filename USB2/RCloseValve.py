#!/usr/bin/env python3
import serial
import time
import subprocess

def main():
    ser = serial.Serial('/dev/ttyACM1', 9600, timeout=1)
    ser.reset_input_buffer()
    
    line = ""
    while (line != "3"): #3-confirmaton of recieved code by Arduino to close valve 
        ser.write(b"1\n")
        line = ser.readline().decode('utf-8').rstrip()
        print(line)
        time.sleep(1)
        
    subprocess.Popen(['python3', 'RSendEmail.py'])

if __name__=='__main__':
    main()

    