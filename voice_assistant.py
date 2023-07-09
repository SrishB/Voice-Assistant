#Intially install all these libraries
#Import the libraries 
import speech_recognition as sr 
import pyttsx3
import pywhatkit
import datetime
import pyjokes
import wikipedia


#Need to initiate the system to recognize your voice
listener = sr.Recognizer() #Create a recognizer object
engine = pyttsx3.init() #Initialize the text-to-speech engine from pyttsx3 library

def talk(text):
    engine.say(text) #Convert Speech to Text
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source: #Microphone as the audio source
            listener.adjust_for_ambient_noise(source) #Adjust for ambient noise 
            print("listening....")
            voice = listener.listen(source) #Listen for audio input 
            command = listener.recognize_google(voice) #Use Google Speech Recognizer to convert speech to text
            command = command.lower()
            if 'Friday' in command: #Check if the wake word Friday is present in the command 
                command = command.replace('Friday', '') #Removing the way word when responding 
                print(command)
            

    except:
        pass
    return command

def run_candy():
    command = take_command() #Get command from user
    print(command)
    if 'youtube' in command:
        play = command.replace('youtube', '')
        talk('playing' + play)
        pywhatkit.playonyt(play) #Use the pywhatkit to play the Youtube video

    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time) #Speak the current time 
        print(time) 

    elif 'joke' in command:
        joke = pyjokes.get_joke() #Get a random joke from pyjokes library
        talk(joke) 
        print(joke)


    elif 'who is' in command:
        search_query = command.replace('who is', '')
        results = wikipedia.summary(search_query, sentences=2) #Get a summary from Wikipedia about the search query 
        talk('Here is what I found on Wikipedia: ' + results)
        print(results)


    else:
        talk('Sorry, I didn\'t understand that. Can you please repeat?') #Speak a default message
        print('Sorry, I didn\'t understand that. Can you please repeat?')

run_candy() #Run the main function
