import pyttsx3
import webbrowser
import speech_recognition as sr
import datetime
import pyjokes

def spttext():
    recognizer= sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening")
        recognizer.adjust_for_ambient_noise(source)
        audio= recognizer.listen(source)
        try:
            print("recognizing")
            data=recognizer.recognize_google(audio)
            print(data)
            return data
        except sr.UnknownValueError:
            print("kuch bhi samajh nahi aaraha hai")

def speechtxt(x):
    engine=pyttsx3.init()
    voices=engine.getProperty('voices')
    engine.setProperty('voice',voices[1].id)
    rate= engine.getProperty('rate')
    engine.setProperty('rate',150)
    engine.say(x)
    engine.runAndWait()

if __name__=='__main__':
    data1= spttext().lower()
    if "thank you" in data1:
        reply1="Hello How can i help u"
        speechtxt(reply1)
        data2= spttext().lower()
        if "tell me a joke" in data2:
            reply2= pyjokes.get_joke()
            speechtxt(reply2)
        elif 'open text' in data2:
            f=open(r"t.txt","r")
            re=f.read()
            speechtxt(re)
            f.close()
        else:
            speechtxt("couldnt  catch you")
    else:
        speechtxt("couldnt catch you")            
        S