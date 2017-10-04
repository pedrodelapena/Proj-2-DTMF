import tkinter as tk
import fourier



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
        # self.button_manda.configure(command = self.escuta)

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
        a2 = str(a[2])
        self.text_freq.set("frequencias: {0} Hz, {1}Hz".format(a0,a1))
        self.text_tom.set("tom: {}".format(a2))

    # def escuta(self):
        

    def iniciar(self):
        self.window.mainloop()



app = Main()
app.iniciar()