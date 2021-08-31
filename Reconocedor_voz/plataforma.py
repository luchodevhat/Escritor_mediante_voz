from tkinter import *

root = Tk()
root.title("Voz a texto")
root.resizable(0, 0)

# FramePrincipal
frame = Frame(root, width=420, height=280)
frame.pack()
frame.config(bg="gray20", bd=25)

#Etiquetas
label_1 = Label(frame, text="Bienvenido escoge con cual archivo de texto deseas trabajar ")
label_1.place(x=25, y=1)
label_1.config(bg="peachpuff", relief="groove")

# Botones
button_0 = Button(frame, text="Archivo word", width=20, height=2)
button_0.place(x=100, y=100)
button_0.config(bg="gray50")

button_1 = Button(frame, text="Archivo .txt", width=20, height=2)
button_1.place(x=100, y=150)
button_1.config(bg="gray50")

root.mainloop()






