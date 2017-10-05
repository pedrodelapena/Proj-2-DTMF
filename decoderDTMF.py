import sounddevice as sd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import animation 
import fourier



fs = 44100
duration = 1

fig = plt.figure()
ax1 = fig.add_subplot(2,1,1)
plt.title('Sinais pelo tempo')
plt.xlabel('Tempo')
plt.ylabel('Sinal')

ax2 = fig.add_subplot(2,1,2)
plt.title('energia por frequencia')
plt.xlabel('Frequecia(Hz)')
plt.ylabel('Energia')

def animate(i):
    t=1
    tempo=np.linspace(0, t, fs*t)
    x = tempo

    # audio = sd.rec(int(duration*fs), fs, channels=1)
    # sd.wait()

    # y = audio[:,0]
    a = fourier.ouveAudio(y)

    ax1.clear()
    ax2.clear()

    #plt.xlim(0,0.015)
    ax1.plot(x[0:1000], y[0:1000])
    plt.title('Sinais pelo tempo')
    plt.xlabel('Tempo')
    plt.ylabel('Sinal')

    ax2.plot(a[2],a[3])
    plt.title('energia por frequencia')
    plt.xlabel('Frequecia(Hz)')
    plt.ylabel('Energia')



# plotagem do gráfico com animação 
anim = animation.FuncAnimation(fig, animate, interval=1000)
    
plt.show()


# ymax = 20000
# new_y = 10*math.log(y/ymax)

