#timer -	Displays a seconds timer with start and stop buttons.
#           Control-c and control-q cause it to exit.
# Selecionar imagem
# Se for RGB
# Selecionar canal da imagem
# Selecionar tipo de conversão em outros espaços de cores
# Selecionar tipo de filtro para remover ruido (gaussiano)
# Selecionar tipo de treshold
# Selecionar grau do treshold
# Selecionar tipo de binarização
# Selecionar extração de caracteristicas

from tkinter import *

class Application(Frame):
    def say_hi(self):
        print("hi there, everyone!")

    def createWidgets(self):
        self.QUIT = Button(self)
        self.QUIT["text"] = "QUIT"
        self.QUIT["fg"]   = "red"
        self.QUIT["command"] =  self.quit

        self.QUIT.pack({"side": "left"})

        self.hi_there = Button(self)
        self.hi_there["text"] = "Hello",
        self.hi_there["command"] = self.say_hi

        self.hi_there.pack({"side": "left"})

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

root = Tk()
app = Application(master=root)
app.mainloop()
root.destroy()