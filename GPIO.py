import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
#GPIO.setup(pin, GPIO.OUT)
#GPIO.output(pin,GPIO.HIGH)


GPIO.setup(A, GPIO.OUT) #sol motor
GPIO.setup(A1, GPIO.OUT)
GPIO.setup(B, GPIO.OUT) #sag motor
GPIO.setup(B2, GPIO.OUT)


A=12
B=16
A1=20
B1=21

def ileri():

    GPIO.output(B,GPIO.LOW)
    GPIO.output(B1,GPIO.LOW)
    GPIO.output(A,GPIO.HIGH)
    GPIO.output(A1,GPIO.HIGH)
    

def geri():  
  
    GPIO.output(A,GPIO.LOW)
    GPIO.output(A1,GPIO.LOW)
    GPIO.output(B,GPIO.HIGH)
    GPIO.output(B1,GPIO.HIGH)


def sag():
    
    GPIO.output(A,GPIO.LOW)
    GPIO.output(B1,GPIO.LOW)
    GPIO.output(A1,GPIO.HIGH)
    GPIO.output(B,GPIO.HIGH)


def sol():
    GPIO.output(B1,GPIO.HIGH)   
    GPIO.output(A1,GPIO.LOW)
    GPIO.output(B,GPIO.LOW)
    GPIO.output(A,GPIO.HIGH)
    












GPIO.cleanup()
