from gtts import gTTS 
import sys
import pyttsx3  
    
def tts(text,voice="female",tempo="normal"):
    # initialize Text-to-speech engine  
    engine = pyttsx3.init()  
    voices = engine.getProperty('voices')
    if tempo=="high":
        engine.setProperty("rate", 400)
    elif tempo=="normal":
        engine.setProperty("rate", 180)
    elif tempo=="low":
        engine.setProperty("rate", 10)
    else:
        tts("Voice argument Not Passed Correctly")
        sys.exit(0)
    if voice=="male":
        engine.setProperty('voice', voices[0].id) #changing index changes voices but ony 0 and 1 are working here
    elif voice=="female":
        engine.setProperty('voice', voices[1].id) #changing index changes voices but ony 0 and 1 are working here
    else:
        tts("Voice argument Not Passed Correctly")
        sys.exit(0)
    # convert this text to speech  
    engine.say(text)  
    # play the speech  
    engine.runAndWait()