#!/usr/bin/env python3
import serial
import subprocess

ser = serial.Serial('/dev/ttyACM0',9600) # устанавливаем соединение с портом ttyACM0 и скоростью обмена 9600 бит в секунду
s = [0,1]
while True:
  read_serial=ser.readline() # чтение символов строки до появления символа "новая строка"
  s[0] = str(int (ser.readline(),16)) # извлекаем из строки все символы, кроме служебных (по типу /r)
  print (s[0])
  print (read_serial)
  if (s[0] == 11):
    subprocess.Popen(['python3', 'RSendValve.py'])
    break
