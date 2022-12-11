# potentiometer.py

import serial
import time

# make sure the 'dev/USB0' is set according list of your devices
ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1, stopbits=2)
time.sleep(2)

for i in range(50):
    line = ser.readline()    # read a byte
    if line:
        string = line.decode()   # convert the byte string to a unicode string
        stripped_string = string.strip()
        num = int(stripped_string)   # convert the unicode string to an int
        print(num)

ser.close()
