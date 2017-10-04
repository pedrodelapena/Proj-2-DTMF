#!/usr/bin/env python3

# sudo pip install PeakUtils

import numpy as np
import matplotlib.pyplot as plt
import math

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

def main():

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

        plt.figure("db abs(Y[k])")
        #plt.stem(X[0:10000], np.abs(Y[0:10000]), linefmt='b-', markerfmt='bo', basefmt='r-')
        plt.plot(X,new_y)
        plt.grid()
        plt.title('DB')

        indexes = peakutils.indexes(new_y, min_dist=30)
        peaks_x = peakutils.interpolate(X, new_y, ind=indexes)
        return(peaks_x)



        ## Exibe sinal no tempo
    # plt.figure("y[n]")
    # plt.plot(y[0:500], 'X')
    # plt.grid()
    # plt.title('Audio no tempo')

    ## Exibe modulo 
    

    plt.figure("abs(Y[k])")
    #plt.stem(X[0:10000], np.abs(Y[0:10000]), linefmt='b-', markerfmt='bo', basefmt='r-')
    plt.plot(X,np.abs(Y))
    plt.grid()
    plt.title('Modulo Fourier audio')

    ## Exibe fases
    plt.figure("Fase(Y[k])")
    plt.plot(X,np.angle(Y))
    plt.grid()
    plt.title('Modulo Fourier audio')

    ## Exibe gráficos
    plt.show()

if __name__ == "__main__":
    main()