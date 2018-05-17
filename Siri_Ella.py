import win32com.client as wincl
import speech_recognition as sr
import webbrowser as wb

speak = wincl.Dispatch("SAPI.SpVoice")

r = sr.Recognizer()
with sr.Microphone() as source:
    speak.Speak("hi I am Ratannie 2.0. Tell me what video to look for.")
    print("listening...")
    audio = r.listen(source)
    print("thinking...")


try:
    words = r.recognize_google(audio)
    speak.Speak("ok ella, let's find " + r.recognize_google(audio))
    wb.open("https://www.youtube.com/results?search_query=" + words)

except sr.UnknownValueError:
    print("Ratannie 2.0 could not understand audio")
except sr.RequestError as e:
    print("could not request results from Ratannie 2.0; {0}".format(e))
                
