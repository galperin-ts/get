import RPi.GPIO as gpio
import time
import numpy as np
import matplotlib.pyplot as plt
dT=0.01
gpio.setmode(gpio.BCM)
dac = [8, 11, 7, 1, 8, 5, 12, 6]
led = [2, 3, 4, 17, 27, 22, 10, 9]
comp = 14
tro = 13
gpio.setup(comp, gpio.IN)
gpio.setup(dac+ led + [tro], gpio.OUT)
def d2bl(x):
    return [int(i) for i in bin(x)[2:].zfill(8)]
def adc ():
    s = [1,0,0,0,0,0,0,0]
    gpio.output(dac,s)
    for i in range(1,8):
        time.sleep(dT)
        if gpio.input(comp):
            s[i-1] = 0
        s[i] = 1
        gpio.output(dac,s)
    return sum([s[i]*2**(7-i) for i in range(8)])
#on my board 8 pin dont work. then adapt discr to 128 not 256 parts
def adapt():
    a = adc()
    if a < 128:
        return 1
    return 2*(a - 128)
data = np.zeros(100000)
try:
    i = 0
    gpio.output(tro, 1)
    input()
    T = time.time()
    x = adapt()
    T = time.time() - T
    while(True):
        x=adapt()
        if (x<250 and x>6):
            data[i]= x
            i+=1
finally:
    gpio.output(tro,0)
    try:
        while(True):
            x = adapt()
            if (x < 250 and x > 6):
                data[i]=x
                i+=1
    finally:

        res = np.array(data.tolist()[:i] + data.tolist()[:i][::-1])
        rest = np.array([j*T for j in range(i*2)])
        print(T, rest[-1])
        with open('data.txt', 'w') as f:
            f.write(np.array2string(res))
        with open('settings.txt', 'w') as f:
            s= str(rest[-1]) + ' ' + str(T) + ' ' + str(1./T) + ' ' + '2'
            f.write(s)
        plt.scatter(rest, res)
        plt.show()
        gpio.cleanup()


