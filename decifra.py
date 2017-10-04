import tkinter as tk



class Main():
    def __init__(self):

        self.window = tk.Tk()
        self.window.title("Qual o tom?")
        self.window.geometry("300x50")
        # self.window.configure(background = 'dim gray')
        self.window.resizable(False, False)


        self.window.rowconfigure(0)
        
        self.window.columnconfigure(0)


        self.text_tom = tk.StringVar()
        self.text_tom.set("askdnjnaskdm") # decifra e plota o som

        self.label = tk.Label(self.window)
        self.label.configure(textvariable=self.text_tom)
        self.label.configure(font="Monospace 24")
        self.label.grid(row=0, column=0, columnspan = 4, sticky="nswe")


    def iniciar(self):
        self.window.mainloop()



app = Main()
app.iniciar()