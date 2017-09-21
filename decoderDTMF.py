import sounddevice as sd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import animation 

fs = 44100
duration = 1

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)
plt.xlabel('Tempo')
plt.ylabel('Sinal')

def animate(i):
    t=1
    tempo=np.linspace(0, t, fs*t)
    x = tempo

    audio = sd.rec(int(duration*fs), fs, channels=1)
    sd.wait()

    y = audio[:,0]

    ax1.clear()
    plt.xlim(0,0.015)
    ax1.plot(x[0:1000], y[0:1000])

# plotagem do gráfico com animação 
anim = animation.FuncAnimation(fig, animate, interval=1000)
    
plt.show()

