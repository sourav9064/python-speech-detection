import speech_recognition as sr
import sys, time

r = sr.Recognizer()

mic = sr.Microphone()

with mic as source:
    r.adjust_for_ambient_noise(source)
    audio = r.listen(source)

    try:
        text = print(r.recognize_google(audio))
        break
    except:
        print('Voice not detected')
        break
        
