import RPi.GPIO as GPIO
sh = 17 # 17 or 19
GPIO.setmode(GPIO.BCM)
GPIO.setup([sh] + [2, 3, 4], GPIO.OUT)
GPIO.output([2,3,4], 0)
p = GPIO.PWM(sh, 1000)
p.start(0)
try:
    while(True):
        d = int(input("Duty cycle: "))
        p.ChangeDutyCycle(d)
        print(3.3*d/100)
finally:
    p.stop()
    GPIO.cleanup()