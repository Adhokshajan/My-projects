import random
#import speech_recognition
import pyttsx3
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

class foodgennonveg:
    #Morning tiffin
    def morning(c):
        speak("Making uupppma is not advicable by the creator , Therefore it is not included in the list of items")

        y=["idili","dosa","POORI","pongal","idiyappam","chappati","kuzhi panniyaram"]
        z=len(y)
        x=random.randrange(0,z)
        return y[x]
    def sambar(b):
        y=["paruppu", "vatha kuzhambu"]
        z=len(y)
        x=random.randrange(0,z)
        f=y[x]+"sambar"
        return f
    def curry(b):
        y=[]
        z=len(y)
        x=random.randrange(0,z)
        f=y[x]+"curry"
        return f
    def rasam(b):
        y=[]
        z=len(y)
        x=random.randrange(0,z)
        f=y[x]+"rasam"
        return f
    def snacks(b):
        y=[]
        z=len(y)
        x=random.randrange(0,z)

        return y[x]
    def dinnner(b):
        y=[]
        z=len(y)
        x=random.randrange(0,z)      
        return y[x]
