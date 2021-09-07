from tkinter import *
from speech import *

# Solucionar error de no responde
class Apertura_txt():
    def __init__(self):
        self.root = root = Tk()
        self.root.title("Voz a texto")
        self.root.resizable(0, 0)

        # FramePrincipal
        frame = Frame(self.root, width=420, height=280)
        frame.pack()
        frame.config(bg="gray20", bd=25)

        button_0 = Button(frame, text="Grabar", width=40, height=2, command=lambda: self.grabar())
        button_0.place(x=35, y=50)
        button_0.config(bg="red")

        button_2 = Button(frame, text="Guardar", width=20, height=2, command=lambda: append(button_0))
        button_2.place(x=100, y=200)
        button_2.config(bg="green")

        self.root.mainloop()


    def grabar(self):
        texto = recognition()

        label_1 = Label(self.frame2, text=texto)
        label_1.place(x=25, y=100)
        label_1.config(bg="peachpuff", relief="groove")














if __name__ == '__main__':
    menu = Apertura_txt()