
import speech_recognition as sr
import os

# INTERFACE DE FUNCIONES A UTILIZAR DENTRO DEL PROYECTO

def write(name):  #  Este metodo sobreescribe el archivo

    ubication = "Archivos/" + name + ".txt"
    with open(ubication, "w", encoding="utf-8") as f:
        f.write("Archivo creado en el convertidor de voz")
        f.write("\n")
        f.write("Hecho por Luis Alejandro Alfaro Quesada")
        f.write("\n")





def append(text, nombre):  # se encarga de agregar texto al archivo

    ubication = "Archivos/" + nombre + ".txt"

    print("El archivo se esta guardando....")
    with open(ubication, "a", encoding="utf-8") as f:
        f.write(text)
        f.write("\n")
    print("El archivo se ha guardado correctamente....")




def read(name):  # se encarga de mostrar el contenido del texto

    ubication = "Archivos/" + name + ".txt"
    numbers = []

    with open(ubication, "r", encoding="utf-8") as f:
        for line in f:
            numbers.append(str(line))
    print("El contenido del archivo es ")
    print(numbers)



def recognition():   # se encarga de reconocer la voz y convertirla en un microfono

    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Di algo...")
        audio = r.listen(source)

        try:
            text = r.recognize_google(audio, language='es-ES')
            print("Lo que dijiste fue : {}".format(text))
            return text

        except:
            print("Lo siento no logro entender....")
            print("No se ha podido continuar ya que no se detecta el audio")



def navigation():  # Se encarga de encontrar nombre y tipo de archivo en un directorio
    dir = "/Users/Aleja/PycharmProjects/VozE/Reconocedor_voz/Archivos"

    with os.scandir(dir) as ficheros:
        ficheros = [fichero.name for fichero in ficheros if fichero.is_file()]
    for i in range(len(ficheros)):
        print(i+1, " = ",  ficheros[i])

    return ficheros



if __name__ == '__main__':
    recognition()