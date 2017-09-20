import sounddevice as sd
import matplotlib.pyplot as plt
import numpy as np
import freq as fq


f1=1209
f2=697

fs = 44100
t=1
tempo = np.linspace(0, t, fs*t)

frequencia = fq.Freq()

def geraSom(fList, num):
    
    
    f1 = fList[0]
    f2 = fList[1]
    
    omega1=(2 * np.pi *f1)
    omega2=(2 * np.pi *f2)

    y1 = np.sin(tempo*omega1)
    y2 = np.sin(tempo*omega2)

    y=y1+y2

    x = tempo

    plt.close("all")
    plt.plot(x, y)
    plt.xlim(0,0.015)
    plt.title(num)
    plt.xlabel('tempo')
    plt.ylabel('onda')
    

    sd.play(y, fs)
    plt.show()
    sd.wait()



    
       






