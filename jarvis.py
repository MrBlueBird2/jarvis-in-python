import pyttsx3 as py3
import speech_recognition as sr
import webbrowser as wb
import wikipedia
import pyjokes as pyj
import datetime

r = sr.Recognizer()

engine = py3.init()


def nowTime():
    ctime = datetime.datetime.now().strftime("%H:%M")
    hour = int(datetime.datetime.now().hour())
    if hour > 1 and hour < 12:
        speak("It's {} A M".format(ctime))
    elif hour >= 12 and hour <= 24:
        print("It's {} P M".format(ctime))

def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        engine.say("Good Morning Sir !")
        print("Good Morning Sir !")
        engine.runAndWait()
    elif hour >= 12 and hour < 18:
        engine.say("Good Afternoon Sir !")  
        print("Good Afternoon Sir !")
        engine.runAndWait()
    else:
        engine.say("Good Evening Sir !") 
        print("Good Evening Sir !")
        engine.runAndWait()
  
    assname = ("Jarvis 1 point o")
    engine.say("I am your Assistant")
    print("I am your Assistant")
    engine.runAndWait()
    engine.say(assname)
    print(assname.replace("point", "."))
    engine.runAndWait()



while True:
    
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
    
        speak("Say something!")
    
    
        audio = r.listen(source)
    
    
    engine.say("Listening...")
    print("Listening...")
    engine.say("Done!")
    print("Done!")
    engine.runAndWait()
    
    print("You said: " + r.recognize_google(audio))


    try:
        a = r.recognize_google(audio)
        b = str(a).lower()
        if "hello" in a:
            engine.say("Hello, How Can I Help You?")


            print("Hello, How Can I Help You?")


            engine.runAndWait()


        elif "how are you" in a:
            engine.say("Hmm, I am Fine")


            print("Hmm, I am Fine")


            engine.runAndWait()


        elif "google" in a:
            engine.say("Searching Google...")
            engine.runAndWait()


            a = str(a).replace("google", "")
            results = wikipedia.summary(a, sentences = 3)
            
            
            engine.say("According to Google")
            print(results)


            engine.say(results)
            engine.runAndWait()


        elif "Google" in a:
            engine.say("Searching Google...")
            engine.runAndWait()


            a = str(a).replace("Google", "")
            results = wikipedia.summary(a, sentences = 3)
            
            
            engine.say("According to Google")
            print(results)
            
            
            engine.say(results)
            engine.runAndWait()


        elif "open youtube" in str(a).lower():
            engine.say("Opening YouTube...")
            print("Opening YouTube...")
            
            
            engine.runAndWait()
            wb.open("https://youtube.com")


        elif "what is the time" in a:
            nowTime()


        elif "sleep jarvis" in str(a).lower():
            engine.say("As you wish!")
            print("As you wish!")
            
            
            engine.runAndWait()
            exit()


        elif "wish me" in str(a).lower():
            wishMe()

        elif "joke" in str(a).lower():
            engine.say(pyj.get_joke())
            engine.runAndWait()
            print(pyj.get_joke())


        elif "what can you do" in b:
            speak("I can Tell you a joke, Open YouTube, Google Something, Wish You")
            speak("I can Tell you the time, chat with you, and much more.")
        
        elif "send email" in b:
            speak("Sorry!, I can't do that!")

        elif "can you chat with me" in b:
            speak("Yeah!, Sure, But Speak in english only")
            
        elif "I am bored" in b:
            speak("U Can listen music or Chat with me")

        else:
            engine.say("It's hard to understand")
            
            
            print("It's hard to understand")
            
            
            engine.runAndWait()
            
            
    
    
    except sr.UnknownValueError():
        b = "Could not understand audio"
        
        
        engine.say(b)
        
        
        print(b)
        engine.runAndWait()