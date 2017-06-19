import serial

fileName = input('File Name: ')
comportName = input('COM Port: ')

file = open(fileName, 'r')  
ser = serial.Serial(comportName)

while True:
    s = file.read()
    ser.write(s)


