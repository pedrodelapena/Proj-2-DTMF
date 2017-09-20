import tkinter as tk
import encoderDTMF
import freq as fq


class Main():
    def __init__(self):
        self.frequencia = fq.Freq()

        self.window = tk.Tk()
        self.window.geometry("300x450+10+10")
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
        self.text_freqs.set("""Freq.1:    
        freq.2:    """)
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
        self.text_freqs.set("""Freq.1:   {0} Hz
        freq.2:   {1} Hz""".format(self.frequencia.one[0] ,self.frequencia.one[1]))

        encoderDTMF.geraSom(self.frequencia.one, 'Sinal 1')

    def tom2(self):
        self.text_freqs.set("""Freq.1:   {0} Hz
        freq.2:   {1} Hz""".format(self.frequencia.two[0] ,self.frequencia.two[1]))

        encoderDTMF.geraSom(self.frequencia.two, 'Sinal 2')
    
    def tom3(self):
        self.text_freqs.set("""Freq.1:   {0} Hz
        freq.2:   {1} Hz""".format(self.frequencia.three[0] ,self.frequencia.three[1]))

        encoderDTMF.geraSom(self.frequencia.three, 'Sinal 3')

    def tom4(self):
        self.text_freqs.set("""Freq.1:   {0} Hz
        freq.2:   {1} Hz""".format(self.frequencia.four[0] ,self.frequencia.four[1]))

        encoderDTMF.geraSom(self.frequencia.four, 'Sinal 4')

    def tom5(self):
        self.text_freqs.set("""Freq.1:   {0} Hz
        freq.2:   {1} Hz""".format(self.frequencia.five[0] ,self.frequencia.five[1]))

        encoderDTMF.geraSom(self.frequencia.five, 'Sinal 5')

    def tom6(self):
        self.text_freqs.set("""Freq.1:   {0} Hz
        freq.2:   {1} Hz""".format(self.frequencia.six[0] ,self.frequencia.six[1]))

        encoderDTMF.geraSom(self.frequencia.six, 'Sinal 6')

    def tom7(self):
        self.text_freqs.set("""Freq.1:   {0} Hz
        freq.2:   {1} Hz""".format(self.frequencia.seven[0] ,self.frequencia.seven[1]))

        encoderDTMF.geraSom(self.frequencia.seven, 'Sinal 7')

    def tom8(self):
        self.text_freqs.set("""Freq.1:   {0} Hz
        freq.2:   {1} Hz""".format(self.frequencia.eight[0] ,self.frequencia.eight[1]))

        encoderDTMF.geraSom(self.frequencia.eight, 'Sinal 8')

    def tom9(self):
        self.text_freqs.set("""Freq.1:   {0} Hz
        freq.2:   {1} Hz""".format(self.frequencia.nine[0] ,self.frequencia.nine[1]))

        encoderDTMF.geraSom(self.frequencia.nine, 'Sinal 9')

    def tom0(self):
        self.text_freqs.set("""Freq.1:   {0} Hz
        freq.2:   {1} Hz""".format(self.frequencia.zero[0] ,self.frequencia.zero[1]))

        encoderDTMF.geraSom(self.frequencia.zero, 'Sinal 0')
        
        
    def iniciar(self):
        self.window.mainloop()



app = Main()
app.iniciar()