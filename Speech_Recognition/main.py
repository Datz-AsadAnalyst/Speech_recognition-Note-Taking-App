import speech_recognition as sr
import gtts 
from playsound import playsound
import os

r= sr.Recognizer()
r.energy_threshold = 300
r.dynamic_energy_threshold = False
ACTIVATION_WORD = "hey sam"
def get_audio():
    with sr.Microphone()as source:
        print("say something")
        audio=r.listen(source)
        return audio
    
def audio_to_text(audio):
    text=""  
    try:
        text =r.recognize_google(audio)    
    except sr.UnknownValueError:
        print("Speech recongination could not understand audio")
    except sr.RequestError:
        print("Could not request result from API")
    return text

def play_audio(text):
    try:
        print("Playing audio...")
        tts = gtts.gTTS(text)
        OutputFile = "output.mp3"
        tts.save(OutputFile)
        playsound(OutputFile)
        os.remove(OutputFile)
    except Exception as e:
        print(f"Error in playing audio: {e}")


if __name__=="__main__":
    while True:
       a=get_audio()
       command= audio_to_text(a)
       print(f"Recognized Text: '{command}'") 

       if ACTIVATION_WORD.lower() in command.lower():
           print("Activation word detected!")
           play_audio("Hello, how can I assist you?")
           note= get_audio()
           note_text = audio_to_text(note)
           if note_text:
               print(f"Note recorded: {note_text}")
               play_audio(f"Note saved: {note_text}")
           else:
               print("No note recorded.")
       else:
           print("Activation word not detected. Please try again.")