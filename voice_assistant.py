import speech_recognition as sr 
import pyttsx3
import pywhatkit
import datetime
import pyjokes
import wikipedia



listener = sr.Recognizer()
engine = pyttsx3.init()

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            listener.adjust_for_ambient_noise(source)
            print("listening....")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'candy' in command:
                command = command.replace('candy', '')
                print(command)
            

    except:
        pass
    return command

def run_candy():
    command = take_command()
    print(command)
    if 'youtube' in command:
        play = command.replace('youtube', '')
        talk('playing' + play)
        pywhatkit.playonyt(play)

    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
        print(time)

    elif 'joke' in command:
        joke = pyjokes.get_joke()
        talk(joke)
        print(joke)


    elif 'who is' in command:
        search_query = command.replace('who is', '')
        results = wikipedia.summary(search_query, sentences=2)
        talk('Here is what I found on Wikipedia: ' + results)
        print(results)


    else:
        talk('Sorry, I didn\'t understand that. Can you please repeat?')
        print('Sorry, I didn\'t understand that. Can you please repeat?')

run_candy()
