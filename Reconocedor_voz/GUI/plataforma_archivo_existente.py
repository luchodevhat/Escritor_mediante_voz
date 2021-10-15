from plataforma_txt import *

class Apertura_archivo_existente():
    def __init__(self):
        self.root = root = Tk()
        self.root.title("Voz a texto")
        self.root.resizable(0, 0)
        self.text = Entry()
        self.n2 = StringVar()
        self.files = Text()

        # FramePrincipal
        frame = Frame(self.root, width=420, height=420)
        frame.pack()
        frame.config(bg="gray20", bd=25)

        # Etiquetas
        label_1 = Label(frame, text="Cual archivo deseas escoger?")
        label_1.place(x=105, y=1)
        label_1.config(bg="peachpuff", relief="groove")

        # nombre archivos
        self.files = Text()
        self.files.place(x=70, y=60)
        self.files.config(width=30, height=10, padx=15, pady=15, bg="light cyan")


        # entrada de texto
        text = Entry(frame, width="40")
        text.place(x=60, y=260)
        text.config(bg="peachpuff", justify="center", relief="sunken", textvariable=self.n2)

        # Botones

        button_1 = Button(frame, text="Buscar", width=20, height=2, command=lambda: self.agregar_nombres())
        button_1.place(x=100, y=300)
        button_1.config(bg="Blue")

        button_2 = Button(frame, text="Escoger", width=20, height=2, command=lambda: self.escoger())
        button_2.place(x=100, y=350)
        button_2.config(bg="green")

        self.root.mainloop()


    def agregar_nombres(self):
        elements = navigation()
        for i in range(len(elements)):
          self.files.insert(END, elements[i])
          self.files.insert(END, "  ")


    def escoger(self):
        nombre = self.n2.get()
        read(nombre)
        self.root.destroy()
        menu2 = Apertura_txt(texto='', nombre=nombre)

if __name__ == '__main__':
    menu = Apertura_archivo_existente()