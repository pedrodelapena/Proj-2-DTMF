import tkinter as tk
import fourier
import matplotlib.pyplot as plt
#import decoderDTMF
import sounddevice as sd
from matplotlib import animation 
import numpy as np



class Main():
    def __init__(self):


        self.window = tk.Tk()
        self.window.title("Qual o tom?")
        # self.window.geometry("300x200")
        # self.window.configure(background = 'dim gray')
        self.window.resizable(False, False)


        self.window.rowconfigure(0)
        self.window.rowconfigure(1)
        self.window.rowconfigure(2)
        
        
        
        self.window.columnconfigure(0)
        self.window.columnconfigure(1)
        self.window.columnconfigure(2)
        

        self.e1 = tk.Entry(self.window)

        self.e1.grid(row=0, column=0)
        
        self.button_manda = tk.Button(self.window, text = "ok",font = ("Monospace",12))
        self.button_manda.grid(row = 0, column = 1)
        self.button_manda.configure(command = self.escolhe_arquivo)

        self.button_manda = tk.Button(self.window, text = "escuta",font = ("Monospace",12))
        self.button_manda.grid(row = 0, column = 2)
        self.button_manda.configure(command = self.escuta)

        self.text_tom = tk.StringVar()
        self.text_tom.set("tom: ") # decifra e plota o som

        self.label = tk.Label(self.window)
        self.label.configure(textvariable=self.text_tom)
        self.label.configure(font="Monospace 12")
        self.label.grid(row=1, column=0, sticky="nswe")

        self.text_freq = tk.StringVar()
        self.text_freq.set("frequncias: ")
    
        self.label = tk.Label(self.window)
        self.label.configure(textvariable=self.text_freq)
        self.label.configure(font="Monospace 12")
        self.label.grid(row=2, column=0, sticky="nswe")

    def escolhe_arquivo(self):
        # fourier.recebeArquivo(str(texto))
        texto = self.e1.get()
        a=fourier.recebeArquivo(str(texto))
        a0 = str(a[0])
        a1 = str(a[1])
        b=fourier.achaTom(a[0], a[1])
        self.text_freq.set("frequencias: {0} Hz, {1}Hz".format(a0,a1))
        self.text_tom.set("tom: {}".format(b))

        plt.close("all")
        fig = plt.figure()
        ax1 = fig.add_subplot(1,1,1)
        
        plt.xlabel('Frequência')
        plt.ylabel('Decibel')
        plt.title('DB')
        ax1.plot(a[2],a[3])
        plt.show()

    def escuta(self):
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

        # audio = sd.rec(int(duration*fs), fs, channels=1)
        # sd.wait()

        # y = audio[:,0]

        def animate(i):
            t=1
            tempo=np.linspace(0, t, fs*t)
            x = tempo

            audio = sd.rec(int(duration*fs), fs, channels=1)
            sd.wait()

            y = audio[:,0]
            #a = fourier.ouveAudio(y)

            a  = fourier.ouveAudio(y)
            a0 = str(a[0])
            a1 = str(a[1])
            b=fourier.achaTom(a[0], a[1])
            self.text_freq.set("frequencias: {0} Hz, {1}Hz".format(a0,a1))
            self.text_tom.set("tom: {}".format(b))

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

        

 
        
        
        

    def iniciar(self):
        self.window.mainloop()



app = Main()
app.iniciar()