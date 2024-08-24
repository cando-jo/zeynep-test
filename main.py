import speech_recognition as speech_recog


def main():
    print(speech_en())
    
    
def speech_tr():
    mic = speech_recog.Microphone()
    recog = speech_recog.Recognizer()
    print("Konuşmaya başlayabilirsiniz...")
    
    with mic as audio_file:

        recog.adjust_for_ambient_noise(audio_file)
        audio = recog.listen(audio_file)
        return recog.recognize_google(audio, language="tr-TR")

def speech_en():
    mic = speech_recog.Microphone()
    recog = speech_recog.Recognizer()
    print("You can speak now...")
    with mic as audio_file:

        recog.adjust_for_ambient_noise(audio_file)
        audio = recog.listen(audio_file)
        return recog.recognize_google(audio, language="en-GB")
      
if __name__ == "__main__":
    main()