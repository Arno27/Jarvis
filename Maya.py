import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=4 and hour<12:
     speak("Good Morning Boss!")

    elif hour>=12 and hour<18:
       speak("Good Afternoon Boss!")
    else:
       speak("Good Evening Boss!")
    speak("I am Jarvis. Boss, please tell me how may I help you.")

def takeCommand():
   # it takes command from the microphone

   r = sr.Recognizer()
   with sr.Microphone() as source:
      print("Listening....")
      r.pause_threshold = 1
      audio = r.listen(source)

   try:
      print("Recognizing...")
      query = r.recognize_google(audio, language = 'english')
      print(f"User said:{query}\n")
   
   except Exception as e:
      print("Sir please say that agian ....")
      return "None"
   
   return query

if __name__ == "__main__":
   while True:
      query = takeCommand().lower()

   #Logic for executing task based on query
      if 'wake up' in query:
         wishMe()
      
      elif 'hello' in query:
         speak('hello master!')
      
      elif 'madam' in query:
         speak('hello mam, hello sir!')
      
      elif 'wikipedia' in query:
         speak('Searching for wikipedia ....')
         query = query.replace("wikipedia","")
         results = wikipedia.summary(query,sentences=2)
         print(results)
         speak(results)
         
      elif 'open youtube' in query:
         webbrowser.open("youtube.com")

      elif 'open google' in query:
         webbrowser.open("google.com")

      elif 'the time' in query:
         strTime = datetime.datetime.now().strftime("%H:%M:%S")
         speak(f"Sir, The time is  {strTime}")
      
      elif 'the date' in query:
         strTime = datetime.datetime.now().strftime("%d/%m/%Y")
         speak(f"Sir, today date is  {strTime}")

      elif 'open code' in query:
         codePath = "C:\\Users\\shubh\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
         os.startfile(codePath)

      elif 'thank you' in query:
         speak(f"It's my pleasure to be in your service.")
         print(f"It's my pleasure to be in your service.\n")

      elif 'what is your name' in query:
         speak(f"I am a AI assistant designed to help my Boss.")
         print(f"I am a AI assistant designed to help my Boss.\n")

      elif 'exit' in query:
         exit()
