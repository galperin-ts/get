import RPi.GPIO as GPIO
dac = [8, 11, 7, 1, 0, 5, 12, 6]
GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)
def d2b (x):
    return [int(i) for i in bin(x)[2:].zfill(8)]
try:
    while(True):
        x = input("from 0 to 255: ")
        if x == 'q':
            break
        elif '.' in x:
            print("Is float!")
            continue
        elif '-' in x:
            print("Less zero!")
            continue
        elif not(x.isdigit()):
            print("Not int!")
            continue
        elif int(x) > 255:
            print("Bigger than 255!")
            continue
        GPIO.output(dac, d2b(int(x)))
        print(int(x) / 256. * 3.3)
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()
