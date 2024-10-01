import RPi.GPIO as GPIO
from time import sleep
dac = [8, 11, 7, 1, 0, 5, 12, 6]
leds = [2, 3, 4, 17, 27, 22, 10, 9]
comp = 14
troyka = 13
GPIO.setmode(GPIO.BCM)
GPIO.setup(dac + leds, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT, initial=1)
GPIO.setup(comp, GPIO.IN)
def d2led(x):
    return [int(i) for i in ('1'*((x+1)//32)).zfill(8)]
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
        GPIO.output(leds, d2led(a))
finally:
    GPIO.output(dac+[troyka], 0)
    GPIO.cleanup()