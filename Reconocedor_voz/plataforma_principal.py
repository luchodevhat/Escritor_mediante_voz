from tkinter import *
from plataforma_txt import *

class Apertura():
    def __init__(self):
        self.root = root = Tk()
        self.root.title("Voz a texto")
        self.root.resizable(0, 0)

        # FramePrincipal
        frame = Frame(self.root, width=420, height=280)
        frame.pack()
        frame.config(bg="gray20", bd=25)

        # Etiquetas
        label_1 = Label(frame, text="Bienvenido escoge con cual archivo de texto deseas trabajar ")
        label_1.place(x=25, y=1)
        label_1.config(bg="peachpuff", relief="groove")

        # Botones
        button_0 = Button(frame, text="Archivo word", width=20, height=2)
        button_0.place(x=100, y=100)
        button_0.config(bg="gray50")

        button_1 = Button(frame, text="Archivo .txt", width=20, height=2, command=lambda: self.opcion_txt_menu())
        button_1.place(x=100, y=150)
        button_1.config(bg="gray50")

        button_2 = Button(frame, text="Varios", width=20, height=2)
        button_2.place(x=100, y=200)
        button_2.config(bg="gray50")

        self.root.mainloop()

    def opcion_txt_menu(self):
        self.root.destroy()
        menu2 = Apertura_txt()



if __name__ == '__main__':
    menu = Apertura()












