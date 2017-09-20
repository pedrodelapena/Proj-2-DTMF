import tkinter as tk
import encoderDTMF
import freq as fq


class Main():
    def __init__(self):
        self.frequencia = fq.Freq()

        self.window = tk.Tk()
        self.window.geometry("300x450")
        self.window.title("Keypad")
        self.window.configure(background = 'dim gray')
        self.window.resizable(False, False)


        self.window.rowconfigure(0, minsize = 100)
        self.window.rowconfigure(1, minsize = 100)
        self.window.rowconfigure(2, minsize = 100)
        self.window.rowconfigure(3, minsize = 100)
        self.window.rowconfigure(4, minsize = 5)


        self.window.columnconfigure(0, minsize = 100)
        self.window.columnconfigure(1, minsize = 100)
        self.window.columnconfigure(2, minsize = 100)

        self.text_freqs = tk.StringVar()
        self.text_freqs.set("")
        # self.text_freqs.set("""Freq.1: {0} Hz
        # freq.2: {1} Hz""".format(self.frequencia.f1a ,self.frequencia.f1b))

        self.label = tk.Label(self.window)
        self.label.configure(textvariable=self.text_freqs)
        self.label.configure(font="Calibri 11")
        self.label.grid(row=4, column=0, columnspan=5, sticky="nswe")

        alt = 6
        larg = 9

        self.buttonOne = tk.Button(self.window, text = "1", height = alt, width = larg)
        self.buttonOne.grid(row = 0, column = 0)
        self.buttonOne.configure(command = self.tom1)

        self.buttonOne = tk.Button(self.window, text = "2", height = alt, width = larg)
        self.buttonOne.grid(row = 0, column =1)
        self.buttonOne.configure(command = self.tom2)

        self.buttonOne = tk.Button(self.window, text = "3", height = alt, width = larg)
        self.buttonOne.grid(row = 0, column = 2)
        self.buttonOne.configure(command = self.tom3)

        self.buttonOne = tk.Button(self.window, text = "4", height = alt, width = larg)
        self.buttonOne.grid(row = 1, column = 0)
        self.buttonOne.configure(command = self.tom4)

        self.buttonOne = tk.Button(self.window, text = "5", height = alt, width = larg)
        self.buttonOne.grid(row = 1, column = 1)
        self.buttonOne.configure(command = self.tom5)

        self.buttonOne = tk.Button(self.window, text = "6", height = alt, width = larg)
        self.buttonOne.grid(row = 1, column = 2)
        self.buttonOne.configure(command = self.tom6)

        self.buttonOne = tk.Button(self.window, text = "7", height = alt, width = larg)
        self.buttonOne.grid(row = 2, column = 0)
        self.buttonOne.configure(command = self.tom7)
        
        self.buttonOne = tk.Button(self.window, text = "8", height = alt, width = larg)
        self.buttonOne.grid(row = 2, column = 1)
        self.buttonOne.configure(command = self.tom8)
        
        self.buttonOne = tk.Button(self.window, text = "9", height = alt, width = larg)
        self.buttonOne.grid(row = 2, column = 2)
        self.buttonOne.configure(command = self.tom9)
        
        self.buttonOne = tk.Button(self.window, text = "0", height = alt, width = larg)
        self.buttonOne.grid(row = 3, column = 1)
        self.buttonOne.configure(command = self.tom0)

    def tom1(self):
        encoderDTMF.geraSom(self.frequencia.f1a, self.frequencia.f1b)

        self.text_freqs = tk.StringVar()
        self.text_freqs.set("""Freq.1: {0} Hz
        freq.2: {1} Hz""".format(self.frequencia.f1a ,self.frequencia.f1b))

        self.label = tk.Label(self.window)
        self.label.configure(textvariable=self.text_freqs)
        self.label.configure(font="Calibri 11")
        self.label.grid(row=4, column=0, columnspan=5, sticky="nswe")

    def tom2(self):
        encoderDTMF.geraSom(self.frequencia.f2a, self.frequencia.f2b)
    
    def tom3(self):
        encoderDTMF.geraSom(self.frequencia.f3a, self.frequencia.f3b)

    def tom4(self):
        encoderDTMF.geraSom(self.frequencia.f4a, self.frequencia.f4b)

    def tom5(self):
        encoderDTMF.geraSom(self.frequencia.f5a, self.frequencia.f5b)

    def tom6(self):
        encoderDTMF.geraSom(self.frequencia.f6a, self.frequencia.f6b)

    def tom7(self):
        encoderDTMF.geraSom(self.frequencia.f7a, self.frequencia.f7b)

    def tom8(self):
        encoderDTMF.geraSom(self.frequencia.f8a, self.frequencia.f8b)

    def tom9(self):
        encoderDTMF.geraSom(self.frequencia.f9a, self.frequencia.f9b)

    def tom0(self):
        encoderDTMF.geraSom(self.frequencia.f0a, self.frequencia.f0b)
        
        
    def iniciar(self):
        self.window.mainloop()



app = Main()
app.iniciar()