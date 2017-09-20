import sounddevice as sd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import animation 

fs = 44100
duration = 1

# audio = sd.rec(int(duration*fs), fs, channels=1)
# sd.wait()

# y = audio[:,0]

# t=1
#     tempo=np.linspace(0, t, fs*t)


# t=1
# tempo=np.linspace(0, t, fs*t)

# while True:
#     audio = sd.rec(int(duration*fs), fs, channels=1)
#     sd.wait()

#     y = audio[:,0]


    
#     x = tempo

#     plt.close()
#     plt.plot(x, y)
#     plt.xlim(0,0.015)
#     plt.xlabel('tempo')
#     plt.ylabel('onda')
#     plt.show(block=False)

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
    
    # line.set_data(x, y)
    # return lin,

    # #reproduz o som
    # sd.play(y, fs)

    # #aguarda fim da reprodução
    # sd.wait()


anim = animation.FuncAnimation(fig, animate, interval=1000)
    

plt.show()



# #reproduz o som
# sd.play(y, fs)

# #aguarda fim da reprodução
# sd.wait()
