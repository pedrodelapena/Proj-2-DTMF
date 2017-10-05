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

    indexes = peakutils.indexes(array_y, thres=0.86, min_dist=0)#min_dist = diferença entre as duas frequencia
    #peaks_x = peakutils.interpolate(X, new_y, ind=indexes)

    peaks_list = []
    for e in indexes:
        peaks_list.append(e)
        
    max1 = max(peaks_list)
    peaks_list.remove(max1)
    max2 = max(peaks_list)



    return(max2, max1, X, new_y)

def ouveAudio(y):
    fs = 44100
    # Cacula a trasformada de Fourier do sinal
    X, Y = calcFFT(y, fs)

    ymax = 20000
    new_y =[]
    for y in Y:
        new_y.append(10*math.log(np.abs(y)/ymax))

    array_y = np.array(new_y)

    indexes = peakutils.indexes(array_y, thres=0.86, min_dist=0)#min_dist = diferença entre as duas frequencia
    #peaks_x = peakutils.interpolate(X, new_y, ind=indexes)

    peaks_list = []
    for e in indexes:
        peaks_list.append(e)
        
    max1 = max(peaks_list)
    peaks_list.remove(max1)
    max2 = max(peaks_list)



    return(max2, max1, X, new_y)

def achaTom(f1, f2):
    if f1 == 697:
        if f2 == 1209:
            return "1"
        elif f2 == 1336:
            return "2"
        elif f2 == 1477:
            return "3"
        elif f2 == 1633:
            return "A"
    elif f1 == 770:
        if f2 == 1209:
            return "4"
        elif f2 == 1336:
            return "5"
        elif f2 == 1477:
            return "6"
        elif f2 == 1633:
            return "B"
    elif f1 == 852:
        if f2 == 1209:
            return "7"
        elif f2 == 1336:
            return "8"
        elif f2 == 1477:
            return "9"
        elif f2 == 1633:
            return "C"
    elif f1 == 941:
        if f2 == 1209:
            return "*"
        elif f2 == 1336:
            return "0"
        elif f2 == 1477:
            return "#"
        elif f2 == 1633:
            return "D"
    else:
        return "Tom não encontrado"




# plt.figure("db abs(Y[k])")
# #plt.stem(X[0:10000], np.abs(Y[0:10000]), linefmt='b-', markerfmt='bo', basefmt='r-')
# plt.plot(X,new_y)
# plt.grid()
# plt.title('DB')

# plt.figure("abs(Y[k])")
# #plt.stem(X[0:10000], np.abs(Y[0:10000]), linefmt='b-', markerfmt='bo', basefmt='r-')
# plt.plot(X,np.abs(Y))
# plt.grid()
# plt.title('Modulo Fourier audio')

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
