import tkinter as tk
# import geraSom as gs

class Main():
    def __init__(self):
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
        self.text_freqs.set("""Freq.1: asd
        Freq.2: dasd""")
        # self.text_freqs.set("""Freq.1: {0}
        # freq.2: {1}""".format(gs.freq[0] Hz,gs.freq[1] Hz))

        self.label = tk.Label(self.window)
        self.label.configure(textvariable=self.text_freqs)
        self.label.configure(font="Calibri 11")
        self.label.grid(row=4, column=0, columnspan=5, sticky="nswe")

        alt = 6
        larg = 9

        self.buttonOne = tk.Button(self.window, text = "1", height = alt, width = larg)
        self.buttonOne.grid(row = 0, column = 0)
        # self.buttonOne.configure(command = gs.one)

        self.buttonOne = tk.Button(self.window, text = "2", height = alt, width = larg)
        self.buttonOne.grid(row = 0, column =1)
        # self.buttonOne.configure(command = gs.two)

        self.buttonOne = tk.Button(self.window, text = "3", height = alt, width = larg)
        self.buttonOne.grid(row = 0, column = 2)
        # self.buttonOne.configure(command = gs.three)

        self.buttonOne = tk.Button(self.window, text = "4", height = alt, width = larg)
        self.buttonOne.grid(row = 1, column = 0)
        # self.buttonOne.configure(command = gs.four)

        self.buttonOne = tk.Button(self.window, text = "5", height = alt, width = larg)
        self.buttonOne.grid(row = 1, column = 1)
        # self.buttonOne.configure(command = gs.five)

        self.buttonOne = tk.Button(self.window, text = "6", height = alt, width = larg)
        self.buttonOne.grid(row = 1, column = 2)
        # self.buttonOne.configure(command = gs.six)

        self.buttonOne = tk.Button(self.window, text = "7", height = alt, width = larg)
        self.buttonOne.grid(row = 2, column = 0)
        # self.buttonOne.configure(command = gs.seven)
        
        self.buttonOne = tk.Button(self.window, text = "8", height = alt, width = larg)
        self.buttonOne.grid(row = 2, column = 1)
        # self.buttonOne.configure(command = gs.eight)
        
        self.buttonOne = tk.Button(self.window, text = "9", height = alt, width = larg)
        self.buttonOne.grid(row = 2, column = 2)
        # self.buttonOne.configure(command = gs.nine)
        
        self.buttonOne = tk.Button(self.window, text = "0", height = alt, width = larg)
        self.buttonOne.grid(row = 3, column = 1)
        # self.buttonOne.configure(command = gs.zero)
        
        
    def iniciar(self):
        self.window.mainloop()



app = Main()
app.iniciar()