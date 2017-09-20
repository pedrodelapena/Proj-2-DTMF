import tkinter as tk
import encoderDTMF
import freq as fq


class Main():
    def __init__(self):
        self.frequencia = fq.Freq()

        self.window = tk.Tk()
        self.window.geometry("400x450+10+10")
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
        self.window.columnconfigure(3, minsize = 100)

        self.text_freqs = tk.StringVar()
        self.text_freqs.set("""Freq.1:    
        freq.2:    """)
        # self.text_freqs.set("""Freq.1: {0} Hz
        # freq.2: {1} Hz""".format(self.frequencia.f1a ,self.frequencia.f1b))

        self.label = tk.Label(self.window)
        self.label.configure(textvariable=self.text_freqs)
        self.label.configure(font="Calibri 11")
        self.label.grid(row=4, column=0, columnspan = 4, sticky="nswe")

        

        alt = 6
        larg = 9

        self.buttonOne = tk.Button(self.window, text = "1", height = alt, width = larg)
        self.buttonOne.grid(row = 0, column = 0)
        self.buttonOne.configure(command = self.tom1)

        self.buttonTwo = tk.Button(self.window, text = "2", height = alt, width = larg)
        self.buttonTwo.grid(row = 0, column =1)
        self.buttonTwo.configure(command = self.tom2)

        self.buttonThree = tk.Button(self.window, text = "3", height = alt, width = larg)
        self.buttonThree.grid(row = 0, column = 2)
        self.buttonThree.configure(command = self.tom3)

        self.buttonFour = tk.Button(self.window, text = "4", height = alt, width = larg)
        self.buttonFour.grid(row = 1, column = 0)
        self.buttonFour.configure(command = self.tom4)

        self.buttonFive = tk.Button(self.window, text = "5", height = alt, width = larg)
        self.buttonFive.grid(row = 1, column = 1)
        self.buttonFive.configure(command = self.tom5)

        self.buttonSix = tk.Button(self.window, text = "6", height = alt, width = larg)
        self.buttonSix.grid(row = 1, column = 2)
        self.buttonSix.configure(command = self.tom6)

        self.buttonSeven = tk.Button(self.window, text = "7", height = alt, width = larg)
        self.buttonSeven.grid(row = 2, column = 0)
        self.buttonSeven.configure(command = self.tom7)
        
        self.buttonEight = tk.Button(self.window, text = "8", height = alt, width = larg)
        self.buttonEight.grid(row = 2, column = 1)
        self.buttonEight.configure(command = self.tom8)
        
        self.buttonNine = tk.Button(self.window, text = "9", height = alt, width = larg)
        self.buttonNine.grid(row = 2, column = 2)
        self.buttonNine.configure(command = self.tom9)
        
        self.buttonZero = tk.Button(self.window, text = "0", height = alt, width = larg)
        self.buttonZero.grid(row = 3, column = 1)
        self.buttonZero.configure(command = self.tom0)
        
        self.buttonHash = tk.Button(self.window, text = "#", height = alt, width = larg)
        self.buttonHash.grid(row = 3, column = 2)
        self.buttonHash.configure(command = self.tomHash)

        self.buttonEstrela = tk.Button(self.window, text = "*", height = alt, width = larg)
        self.buttonEstrela.grid(row = 3, column = 0)
        self.buttonEstrela.configure(command = self.tomEstrela)

        self.buttonA = tk.Button(self.window, text = "A", height = alt, width = larg)
        self.buttonA.grid(row = 0, column = 3)
        self.buttonA.configure(command = self.tomA)

        self.buttonB = tk.Button(self.window, text = "B", height = alt, width = larg)
        self.buttonB.grid(row = 1, column = 3)
        self.buttonB.configure(command = self.tomB)

        self.buttonC = tk.Button(self.window, text = "C", height = alt, width = larg)
        self.buttonC.grid(row = 2, column = 3)
        self.buttonC.configure(command = self.tomC)

        self.buttonD = tk.Button(self.window, text = "D", height = alt, width = larg)
        self.buttonD.grid(row = 3, column = 3)
        self.buttonD.configure(command = self.tomD)


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

    def tomHash(self):
        self.text_freqs.set("""Freq.1:   {0} Hz
        freq.2:   {1} Hz""".format(self.frequencia.hash[0] ,self.frequencia.hash[1]))

        encoderDTMF.geraSom(self.frequencia.hash, 'Sinal #')

    def tomEstrela(self):
        self.text_freqs.set("""Freq.1:   {0} Hz
        freq.2:   {1} Hz""".format(self.frequencia.estrela[0] ,self.frequencia.estrela[1]))

        encoderDTMF.geraSom(self.frequencia.estrela, 'Sinal *')

    def tomA(self):
        self.text_freqs.set("""Freq.1:   {0} Hz
        freq.2:   {1} Hz""".format(self.frequencia.A[0] ,self.frequencia.A[1]))

        encoderDTMF.geraSom(self.frequencia.A, 'Sinal A')

    def tomB(self):
        self.text_freqs.set("""Freq.1:   {0} Hz
        freq.2:   {1} Hz""".format(self.frequencia.B[0] ,self.frequencia.B[1]))

        encoderDTMF.geraSom(self.frequencia.B, 'Sinal B')

    def tomC(self):
        self.text_freqs.set("""Freq.1:   {0} Hz
        freq.2:   {1} Hz""".format(self.frequencia.C[0] ,self.frequencia.C[1]))

        encoderDTMF.geraSom(self.frequencia.C, 'Sinal C')

    def tomD(self):
        self.text_freqs.set("""Freq.1:   {0} Hz
        freq.2:   {1} Hz""".format(self.frequencia.D[0] ,self.frequencia.D[1]))

        encoderDTMF.geraSom(self.frequencia.D, 'Sinal D')



    def iniciar(self):
        self.window.mainloop()



app = Main()
app.iniciar()