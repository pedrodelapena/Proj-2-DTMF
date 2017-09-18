import sounddevice as sd
import matplotlib.pyplot as plt
import numpy as np

fs = 44100
duration = 3

audio = sd.rec(int(duration*fs), fs, channels=1)
sd.wait()

y = audio[:,0]

# reproduz o som
# sd.play(y, fs)

# aguarda fim da reprodução
# sd.wait()


tempo=np.linspace(0, 1, fs)
# omega1=(2 * np.pi *f1)
# omega2=(2 * np.pi *f2)

# y1 = np.sin(tempo*omega1)
# y2 = np.sin(tempo*omega2)

# y=y1+y2

x = tempo
print (len(x), len(y))
plt.plot(x, y)
plt.xlim(0,0.015)
plt.xlabel('tempo')
plt.ylabel('onda')
plt.show()
