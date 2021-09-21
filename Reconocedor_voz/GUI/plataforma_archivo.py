
from Reconocedor_voz.speech import *
from plataforma_txt import *



class Apertura_Archivo_nuevo():
    def __init__(self):
        self.root = root = Tk()
        self.root.title("Voz a texto")
        self.root.resizable(0, 0)
        self.text = Entry()
        self.n2 = StringVar()


        # FramePrincipal
        frame = Frame(self.root, width=420, height=280)
        frame.pack()
        frame.config(bg="gray20", bd=25)

        # Etiquetas
        label_1 = Label(frame, text="Digita el nombre del archivo")
        label_1.place(x=105, y=1)
        label_1.config(bg="peachpuff", relief="groove")

        # entrada de texto
        text = Entry(frame, width="40")
        text.place(x=60, y=90)
        text.config(bg="peachpuff", justify="center", relief="sunken", textvariable=self.n2)

        # Botones

        button_1 = Button(frame, text="Crear", width=20, height=2, command=lambda: self.nuevo())
        button_1.place(x=100, y=150)
        button_1.config(bg="green")

        self.root.mainloop()


    def nuevo(self):   # resolver error de aqui
        nombre = self.n2.get()
        write(nombre)
        self.root.destroy()
        menu2 = Apertura_txt(texto='', nombre=nombre)





if __name__ == '__main__':
    menu = Apertura_Archivo_nuevo()
