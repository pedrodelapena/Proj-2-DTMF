import sounddevice as sd
import matplotlib.pyplot as plt
import numpy as np
import freq as fq
import fourier as fr
import math


f1=1209
f2=697

fs = 44100
t=2
tempo = np.linspace(0, t, fs*t)

frequencia = fq.Freq()

def geraSom(fList, num):
    
    
    f1 = fList[0]
    f2 = fList[1]
    
    omega1=(2 * np.pi *f1)
    omega2=(2 * np.pi *f2)

    # gera senos da duas frequencias
    y1 = np.sin(tempo*omega1)
    y2 = np.sin(tempo*omega2)

    y=y1+y2

    x = tempo

    X, Y = fr.calcFFT(y, fs)
    ymax = 20000
    new_y =[]
    for e in Y:
        new_y.append(10*math.log(np.abs(e)/ymax))

    plt.close("all")
    fig = plt.figure(figsize = (10,4), facecolor="w")
    fig.canvas.set_window_title("Gráfico original")

    #gráfco em função do tempo
    ax1 = fig.add_subplot(1,2,1)
    ax1.set_xlim(0,0.015)
    ax1.set_xlabel('tempo')
    ax1.set_ylabel('onda')
    ax1.set_title(num)
    ax1.plot(x,y)

    # gráfico das frequencias em decibeis (utilizando fourier)
    ax2 = fig.add_subplot(1,2,2)
    ax2.set_xlabel('frequencia(Hz)')
    ax2.set_ylabel('DB')
    ax2.set_title('frequencia por decibel')
    ax2.plot(X, new_y)
    

    # repoduz som 
    sd.play(y, fs)
    plt.show()
    sd.wait()



    
       






