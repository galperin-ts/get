import matplotlib.pyplot as plt 
import matplotlib.ticker as ticker
import numpy as np
with open('settings.txt') as f:
    nu, dq = list(map(float,f.read().split()))
with open('data.txt') as f:
    data = list(map(int, f.read().split()))
data = np.array(data)
volts=data*dq
times = np.arange(len(data))*nu
mi = volts.argmax(axis=0)

fig, ax = plt.subplots()
ax.scatter(times[::40],volts[::40],15, color='C0')
ax.plot(times,volts, label='V(t)')
ax.grid(which='major', color='#DDDDDD', linewidth=0.8)
ax.grid(which='minor', color='#EEEEEE', linestyle=':', linewidth=0.5)
ax.yaxis.set_minor_locator(ticker.MultipleLocator(0.1))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(0.4))
ax.set_ylim(np.min(volts), volts[mi] + 0.3)
ax.set_xlim(np.min(times),np.max(times))
ax.set_title('Процесс заряда и разряда конденсатора в RC-цепочке',fontsize=10, loc='center', wrap=True)
ax.text(8, 0.9, f'Время заряда {times[mi]} c', fontsize = 6)
ax.text(8, 0.7, f'Время разрядки {times[-1] - times[mi]} c', fontsize = 6)
ax.set_ylabel('V, В')
ax.set_xlabel('t, c')
ax.legend()
plt.savefig('graph.svg')
plt.show()