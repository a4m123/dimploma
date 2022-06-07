import serial

def main(code):
    for i in range(10):
        trySerial = '/dev/ttyACM' + str(i)
        try:
            ser = serial.Serial(trySerial, 9600)
            controlStr = str(code) + "\n"
            ser.write(bytes(controlStr, 'utf-8'))
            line = ""
            while (line == ""):
                line = ser.readline().decode('utf-8').rstrip()
            ser.close()
            if (line == "1"):
                return i
        except:
            pass


if __name__ == "__main__":
    main()