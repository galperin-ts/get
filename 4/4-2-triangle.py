import RPi.GPIO as GPIO
import time
dac = [8, 11, 7, 1, 0, 5, 12, 6]
GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)
def d2b (x):
    return [int(i) for i in bin(x)[2:].zfill(8)]
try:
    T=int(input("T = "))
    while(True):
        t = int(time.time()*1000)
        x = abs(255. * 2 *((t % T)/T - 1/2))
        GPIO.output(dac, d2b(int(x)))
        time.sleep(0.01)
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()