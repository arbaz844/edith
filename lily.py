
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
engine=pyttsx3.init("sapi5")
voices=engine.getProperty("voices")
print(voices[1].id)
engine.setProperty("voice",voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    wish=int(datetime.datetime.now().hour)
    if wish>=0 and wish<=12:
        speak("Good morning")
    elif wish>12 and wish<=18:
        speak("good afternoon")
    else:
        speak("Good Evening")
    speak("Natasha here  you are so crazy Arbaz tell me how can i help you.")

def takeinput():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening......")
        r.pause_threshold =1
        audio=r.listen(source)
    try:
        print("recognizing.....")
        query=r.recognize_google(audio,language="en-in")
        print(f"user said:{query}\n")
    except Exception as e:
        #print(e)
        print("say that again")
        return "None"  
    return query

if __name__=="__main__":
    wishme()
    while True:
        query=takeinput().lower()
        if "wikipedia" in query:
            speak("searching wikipedia")
            query=query.replace("wikipedia","")
            output=wikipedia.summary(query,sentences=2)
            speak(output)
            print(output)
    
            
