import serial
import time

ser = serial.Serial("/dev/ttyACM1", 9600)

a = []

ser.flush()

#while True:
x = 1
while 1:
    #ans = "5"

    ans = input("Enter a number to send: ")
    ans = ans.encode("utf-8")
    ser.write(ans)
    time.sleep(.02)
    #while ser.in_waiting > 0:
    s = ser.read().decode('utf-8')#.rstrip()
    #if(s.isdigit())
    if(s != '\r' and s != '\n' and s != ''):
        a.append(int(s))

    s = ser.read().decode('utf-8')#.rstrip()
    #if(s.isdigit())
    if(s != '\r' and s != '\n' and s != ''):
        a.append(int(s))
    print("We got: ", s, "\n")
    print("We currently have list ", a[:], "\n")
    s = ser.read().decode('utf-8')
    s = ser.read().decode('utf-8')


    if(len(a) == 4):
        firstNum = int(str(a[0]) + str(a[1]))
        secondNum = int(str(a[2]) + str(a[3]))
        a = []
        print("The first number is ", firstNum, "\n")
        print("The second number is ", secondNum, "\n")
#     input.append(s)

#print(input, "\n")