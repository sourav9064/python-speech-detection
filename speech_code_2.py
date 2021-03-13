import speech_recognition as sr
import sys, time
import numpy as np

r = sr.Recognizer()

mic = sr.Microphone()

while(1):
    try:
        with mic as source:
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)
            text = r.recognize_google(audio)
            print(text)
            if str(text) == 'hello':
                print('true')
                f = open(r'C:\Users\HP\DEASYSOFT Tech Pvt Ltd\3rd Project\Speak_code\speak_output.txt')
                f.write('Voice detected at ' + timestrftime('%H:%M:%S')
                f.close()
                #break

        
    except:
        print('Voice not detected')
        break


#if text == 'hello':
 #           print('Voice detected')
  #          f = open(r'C:\Users\HP\DEASYSOFT Tech Pvt Ltd\3rd Project\Speak_code\speak_output.txt')
    #        f.write('Voice detected at ' + timestrftime('%H:%M:%S')
            #f.close()'''
    #k = sr.waitKey(1)
    #if k == ord('q'):
    #break
