
import speech_recognition as sr


def write(names):
    with open("Archivos/test.txt", "w", encoding="utf-8") as f:
        for name in names:
            f.write(name)
            f.write("\n")


def append(text):
    with open("Archivos/test.txt", "a", encoding="utf-8") as f:
        f.write(text)
        f.write("\n")


def recognition():   # se encarga de reconocer la voz y convertirla en un microfono

    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Di algo...")
        audio = r.listen(source)

        try:
            text = r.recognize_google(audio, language='es-ES')
            print("Lo que dijiste fue : {}".format(text))
        except:
            print("Lo siento no logro entender....")







if __name__ == '__main__':
    recognition()