#!/usr/bin/env python3

# sudo pip install PeakUtils

import numpy as np
import matplotlib.pyplot as plt
import math
import peakutils

# Calculate de FFT from a signal
# https://docs.scipy.org/doc/scipy/reference/tutorial/fftpack.html
def calcFFT(signal, fs):
        from scipy.fftpack import fft
        from scipy import signal as window

        N  = len(signal)
        T  = 1/fs
        xf = np.linspace(0.0, 1.0/(2.0*T), N//2)
        yf = fft(signal)
        return(xf, yf[0:N//2])

def recebeArquivo(arquivo):
    # Import sound as file
    som = './som{0}.wav'.format(arquivo)
    import soundfile as sf
    y, fs = sf.read(som)

    # Cacula a trasformada de Fourier do sinal
    X, Y = calcFFT(y, fs)

    ymax = 20000
    new_y =[]
    for y in Y:
        new_y.append(10*math.log(np.abs(y)/ymax))

    array_y = np.array(new_y)

    plt.figure("db abs(Y[k])")
    #plt.stem(X[0:10000], np.abs(Y[0:10000]), linefmt='b-', markerfmt='bo', basefmt='r-')
    plt.plot(X,new_y)
    plt.grid()
    plt.title('DB')

    plt.figure("abs(Y[k])")
    #plt.stem(X[0:10000], np.abs(Y[0:10000]), linefmt='b-', markerfmt='bo', basefmt='r-')
    plt.plot(X,np.abs(Y))
    plt.grid()
    plt.title('Modulo Fourier audio')

    # plt.show()

    indexes = peakutils.indexes(array_y, thres=0.86, min_dist=0)#min_dist = diferença entre as duas frequencia
    #peaks_x = peakutils.interpolate(X, new_y, ind=indexes)

    peaks_list = []
    for e in indexes:
        peaks_list.append(e)
        
    max1 = max(peaks_list)
    peaks_list.remove(max1)
    max2 = max(peaks_list)

    return(max1, max2)
print("1",recebeArquivo(1))
print("2",recebeArquivo(2))
print("3",recebeArquivo(3))
print("A",recebeArquivo('A'))
print('4',recebeArquivo(4))
print('5',recebeArquivo(5))
print('6',recebeArquivo(6))
print('B',recebeArquivo('B'))
print('7',recebeArquivo(7))
print('8',recebeArquivo(8))
print('9',recebeArquivo(9))
print('C',recebeArquivo('C'))
print('*',recebeArquivo('Estrela'))
print('0',recebeArquivo(0))
print('#',recebeArquivo('Hash'))
print('D',recebeArquivo('D'))



    ## Exibe sinal no tempo
# plt.figure("y[n]")
# plt.plot(y[0:500], 'X')
# plt.grid()
# plt.title('Audio no tempo')

## Exibe modulo 


# plt.figure("abs(Y[k])")
# #plt.stem(X[0:10000], np.abs(Y[0:10000]), linefmt='b-', markerfmt='bo', basefmt='r-')
# plt.plot(X,np.abs(Y))
# plt.grid()
# plt.title('Modulo Fourier audio')

# ## Exibe fases
# plt.figure("Fase(Y[k])")
# plt.plot(X,np.angle(Y))
# plt.grid()
# plt.title('Modulo Fourier audio')

## Exibe gráficos
