
import speech_recognition as sr


def write(name):  # # Este metodo sobreescribe el archivo

    ubication = "Archivos/" + name + ".txt"
    with open(ubication, "w", encoding="utf-8") as f:
        f.write(name)
        f.write("\n")




def append(text, nombre):  # se encarga de agregar texto al archivo

    ubication = "Archivos/" + nombre + ".txt"

    print("El archivo se esta guardando....")
    with open(ubication, "a", encoding="utf-8") as f:
        f.write(text)
        f.write("\n")
    print("El archivo se ha guardado correctamente....")





def read():  # se encarga de mostrar el contenido del texto
    numbers = []

    with open("Archivos/test.txt", "r", encoding="utf-8") as f:
        for line in f:
            numbers.append(str(line))
    print(numbers)



def recognition():   # se encarga de reconocer la voz y convertirla en un microfono

    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Di algo...")
        audio = r.listen(source)

        try:
            text = r.recognize_google(audio, language='es-ES')
            print("Lo que dijiste fue : {}".format(text))
            #append(text)
            return text

        except:
            print("Lo siento no logro entender....")
            print("No se ha podido continuar ya que no se detecta el audio")




if __name__ == '__main__':
    recognition()