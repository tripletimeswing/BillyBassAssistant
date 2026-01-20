def speechRec():
    import speech_recognition as sr

    try:
        #recognizer object
        r = sr.Recognizer()
        r.dynamic_energy_threshold = True
        r.pause_threshold = 1.5
        heard = None

        with sr.Microphone() as source:
            print("start speaking\n")
            #adjust for ambient noise
            r.adjust_for_ambient_noise(source, duration=0.3)
            audio = r.listen(source)
            print("processing\n")

            try:
                print("heard\n")
            except sr.UnkownValueError:
                print("value error")
            except sr.RequestError:
                print("request error")
    finally:
        heard = r.recognize_google(audio)
    return(heard)