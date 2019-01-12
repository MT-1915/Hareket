import pyautogui as pyx
import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)

xx= 31 
yonx=33
zz=35
yonz=37

GPIO.setup(xx, GPIO.OUT)
GPIO.setup(zz, GPIO.OUT)

GPIO.setup(yonx, GPIO.OUT)
GPIO.setup(yonz, GPIO.OUT)

def hrkt(pin,yon,yonp,zaman):#step pin,yon,yon pin,zaman
        
        if(zaman==0):
            GPIO.output(yonp,GPIO.LOW)
            GPIO.output(pin,GPIO.LOW)
        else:
            if(yon==1):
                GPIO.output(yonp,GPIO.HIGH)
            if(yon==0):
                GPIO.output(yonp,GPIO.LOW)

            GPIO.output(pin,GPIO.HIGH)
            time.sleep(zaman)
            GPIO.output(pin,GPIO.LOW)
            time.sleep(zaman)




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
                yon ="sol_ust"

        if(int(xp)<=x1 and int(xp)>=0 ): 
            if(int(yp)>=y1 and int(yp)<=y2):
                print("Sol")
                yon ="sol"

        if(int(xp)<=x1 and int(xp)>=0 ): 
            if(int(yp)>=y2 and int(yp)<=y):
                print("Sol alt")
                yon ="sol_alt"

        if(int(xp)<=x2 and int(xp)>=x1 ): 
            if(int(yp)>=0 and int(yp)<=y1):
                print("Ust")
                yon ="ust"

        if(int(xp)<=x2 and int(xp)>=x1 ): 
            if(int(yp)>=y1 and int(yp)<=y2):
                print("Dur")
                yon ="dur"

        if(int(xp)<=x2 and int(xp)>=x1 ): 
            if(int(yp)>=y2 and int(yp)<=y):
                print("Alt")
                yon ="alt"

        if(int(xp)<=x and int(xp)>=x2 ): 
            if(int(yp)>=0 and int(yp)<=y1):
                print("Sag ust")
                yon ="sag_ust"

        if(int(xp)<=x and int(xp)>=x2 ): 
            if(int(yp)>=y1 and int(yp)<=y2):
                print("Sag")
                yon ="sag"

        if(int(xp)<=x and int(xp)>=x2 ): 
            if(int(yp)>=y2 and int(yp)<=y):
                print("Sag alt")
                yon ="sag_alt"
        
        print(yon)
        time.sleep(0.005)


        if(yon=="sol_ust"):
                hrkt(xx ,0,yonx,zmn) 
                hrkt(zz ,1,yonz,zmn)

        if(yon=="sol"):
                hrkt(xx , 0,yonx ,zmn)

        if(yon=="sol_alt"):
                hrkt(xx ,0,yonx,zmn) 
                hrkt(zz ,0,yonz,zmn)

        if(yon=="ust "):
                hrkt(zz,1,yonz,zmn)

        if(yon=="dur"):
                hrkt(zz,0,yonx,0)

        if(yon=="alt"):
                hrkt(zz,0 ,yonz ,zmn)

        if(yon=="sag_ust"):
                hrkt(xx ,1,yonx,zmn) 
                hrkt(zz ,1,yonz,zmn)

        if(yon=="sag"):
                hrkt(xx ,1 ,yonx ,zmn)

        if(yon=="sag_alt"):
                hrkt(xx ,0,yonx,zmn) 
                hrkt(zz ,0,yonz,zmn)
        time.sleep(0.005)

