import speech_recognition as sr
import gtts 
from playsound import playsound


r= sr.Recognizer()

def get_aud():
    with sr.Microphone()as source:
        print("say something")
        audio=r.listen(source)
        return audio
    
def audio_to_text(audio):
    text=""  
    try:
        text =r.recognize_google(audio)    
    except sr.UnknownValueError():
        print("Speech recongination could not understand audio")
    except sr.RequestError():
        print("Could not request result from API")
    return text


if __name__=="__main__":
    a=get_aud()
    command= audio_to_text(a)
    print(command)        