import RPi.GPIO as GPIO
from time import sleep
dac = [8, 11, 7, 1, 0, 5, 12, 6]
comp = 14
troyka = 13
GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT, initial=1)
GPIO.setup(comp, GPIO.IN)
def d2bl(x):
    return [int(i) for i in bin(x)[2:].zfill(8)]
def adc ():
    L = 0
    R = 256
    while R - L > 1:
        m = (R + L) // 2
        GPIO.output(dac, d2bl(m))
        sleep(0.001)
        f = GPIO.input(comp)
        if f:
            R = m
        else:
            L = m+1
    return L

try:
    while(True):
        a = adc()
        print(a, 3.3/256*a)
        
finally:
    GPIO.output(dac+[troyka], 0)
    GPIO.cleanup()