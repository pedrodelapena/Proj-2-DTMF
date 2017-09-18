import sounddevice as sd
import matplotlib.pyplot as plt
import numpy as np

f1=1209
f2=697

fs = 44100
t=1
tempo=np.linspace(0, t, fs*t)
omega1=(2 * np.pi *f1)
omega2=(2 * np.pi *f2)

y1 = np.sin(tempo*omega1)
y2 = np.sin(tempo*omega2)

y=y1+y2

x = tempo
print (len(x), len(y))
plt.plot(x, y)
plt.xlim(0,0.015)
plt.xlabel('tempo')
plt.ylabel('onda')
plt.show()

sd.play(y, fs)
sd.wait()