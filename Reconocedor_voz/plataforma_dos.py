from tkinter import *
from plataforma_txt import *
from plataforma_doc import *


#Trabajando aca
class Apertura_dos():
    def __init__(self):
        self.root = root = Tk()
        self.root.title("Voz a texto")
        self.root.resizable(0, 0)

        # FramePrincipal
        frame = Frame(self.root, width=420, height=280)
        frame.pack()
        frame.config(bg="gray20", bd=25)

        # Etiquetas
        label_1 = Label(frame, text="Deseas crear un archivo nuevo o usar uno existente?")
        label_1.place(x=45, y=1)
        label_1.config(bg="peachpuff", relief="groove")

        # Botones
        button_0 = Button(frame, text="Nuevo", width=20, height=2, command=lambda : self.nuevo())
        button_0.place(x=100, y=100)
        button_0.config(bg="gray50")

        button_1 = Button(frame, text="Existente", width=20, height=2, command=lambda: self.exitente())
        button_1.place(x=100, y=150)
        button_1.config(bg="gray50")


        self.root.mainloop()

    def nuevo(self):
        pass

    def exitente(self):
        pass

if __name__ == '__main__':
    menu = Apertura_dos()
