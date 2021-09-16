from tkinter import *
from speech import *

class Apertura_txt():
    def __init__(self, texto = '', nombre=''):
        self.root = root = Tk()
        self.root.title("TXT")
        self.root.resizable(0, 0)
        self.frame = frame = Frame()
        self.texto = texto
        self.nombre = nombre

        # FramePrincipal
        frame = Frame(self.root, width=420, height=280)
        frame.pack()
        frame.config(bg="gray20", bd=25)

        button_0 = Button(frame, text="Grabar", width=40, height=2, command=lambda: self.grabar())
        button_0.place(x=35, y=50)
        button_0.config(bg="red")

        button_2 = Button(frame, text="Guardar", width=20, height=2, command=lambda: append(self.texto, self.nombre))
        button_2.place(x=100, y=200)
        button_2.config(bg="green")

        self.root.mainloop()


    def grabar(self):
        print("Se comenzara a grabar....")
        self.texto = recognition()
        print("Presiona el boton de guardar si quieres guardar")


if __name__ == '__main__':
    menu = Apertura_txt()