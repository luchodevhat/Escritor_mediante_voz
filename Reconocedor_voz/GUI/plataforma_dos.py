from plataforma_principal import *
from plataforma_txt import *
from Reconocedor_voz.speech import *
from plataforma_archivo import *
from plataforma_archivo_existente import *


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

        button_1 = Button(frame, text="Existente", width=20, height=2, command=lambda: self.leer())
        button_1.place(x=100, y=150)
        button_1.config(bg="gray50")

        button_2 = Button(frame, text="Volver", width=20, height=2, command=lambda: self.volver())
        button_2.place(x=100, y=200)
        button_2.config(bg="red")

        self.root.mainloop()

    def nuevo(self):
        self.root.destroy()
        menu2 = Apertura_Archivo_nuevo()

    def leer(self):
        self.root.destroy()
        menu2 = Apertura_archivo_existente()


        nombre = input("Digita el nombre del archivo existente a buscar ")
        read(nombre)
        self.root.destroy()
        menu2 = Apertura_txt(texto='', nombre=nombre)


    def volver(self):
        self.root.destroy()
        menu1 = Apertura()


if __name__ == '__main__':
    menu = Apertura_dos()
