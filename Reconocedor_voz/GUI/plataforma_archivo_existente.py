from plataforma_txt import *

class Apertura_archivo_existente():
    def __init__(self):
        self.root = root = Tk()
        self.root.title("Voz a texto")
        self.root.resizable(0, 0)
        self.text = Entry()
        self.n2 = StringVar()

        # FramePrincipal
        frame = Frame(self.root, width=420, height=380)
        frame.pack()
        frame.config(bg="gray20", bd=25)

        # Etiquetas
        label_1 = Label(frame, text="Cual archivo deseas escoger?")
        label_1.place(x=105, y=1)
        label_1.config(bg="peachpuff", relief="groove")

        # nombre archivos

        files = Text()
        files.place(x=70, y=60)
        files.config(width=30, height=10, padx=15, pady=15)
        self.agregar_nombres(files)


        # entrada de texto
        text = Entry(frame, width="40")
        text.place(x=60, y=260)
        text.config(bg="peachpuff", justify="center", relief="sunken", textvariable=self.n2)

        # Botones

        button_1 = Button(frame, text="Escoger", width=20, height=2, command=lambda: self.escoger())
        button_1.place(x=100, y=300)
        button_1.config(bg="green")

        self.root.mainloop()


    def agregar_nombres(self, archivos):  # trabajando desde aqui
        pass


    def escoger(self):
        nombre = self.n2.get()
        read(nombre)
        self.root.destroy()
        menu2 = Apertura_txt(texto='', nombre=nombre)

if __name__ == '__main__':
    menu = Apertura_archivo_existente()