import pyautogui as pyx
import time
import serial

serialport = serial.Serial('ttyUSB0', 9600)
x,y = pyx.size()#ekran cozunurlugu

x1=(x/3)*1
x2=(x/3)*2
y1=(y/3)*1
y2=(y/3)*2

zmn=0.001

while True:
        xp,yp = pyx.position()#x mouse y mouse
        if(int(xp)<=x1 and int(xp)>=0 ): 
            if(int(yp)>=0 and int(yp)<=y1):
                print("Sol ust")
                serialport.write(bytes(7, 'utf-8'))#sol ust

        if(int(xp)<=x1 and int(xp)>=0 ): 
            if(int(yp)>=y1 and int(yp)<=y2):
                print("Sol")
                serialport.write(bytes(2, 'utf-8'))#sol

        if(int(xp)<=x1 and int(xp)>=0 ): 
            if(int(yp)>=y2 and int(yp)<=y):
                print("Sol alt")
                serialport.write(bytes(8, 'utf-8'))#sol alt

        if(int(xp)<=x2 and int(xp)>=x1 ): 
            if(int(yp)>=0 and int(yp)<=y1):
                print("Ust")
                serialport.write(bytes(3, 'utf-8'))#ust

        if(int(xp)<=x2 and int(xp)>=x1 ): 
            if(int(yp)>=y1 and int(yp)<=y2):
                print("Dur")
                serialport.write(bytes(0, 'utf-8'))#dur

        if(int(xp)<=x2 and int(xp)>=x1 ): 
            if(int(yp)>=y2 and int(yp)<=y):
                print("Alt")
                serialport.write(bytes(4, 'utf-8'))#alt

        if(int(xp)<=x and int(xp)>=x2 ): 
            if(int(yp)>=0 and int(yp)<=y1):
                print("Sag ust")
                serialport.write(bytes(5, 'utf-8'))#sag ust

        if(int(xp)<=x and int(xp)>=x2 ): 
            if(int(yp)>=y1 and int(yp)<=y2):
                print("Sag")
                serialport.write(bytes(1, 'utf-8'))#sag

        if(int(xp)<=x and int(xp)>=x2 ): 
            if(int(yp)>=y2 and int(yp)<=y):
                print("Sag alt")
                serialport.write(bytes(6, 'utf-8'))#sag alt
        
        print(yon)
        
        
