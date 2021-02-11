import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening..')
            talk('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'sai' in command:
                command = command.replace('sai', '')
                print(command)

    except:
        pass
    return command


def run_sai():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('Current time is ' + time)
    elif 'who is'  in command:
        person = command.replace('who is', '')
        wiki = wikipedia.summary(person, 1)
        print(wiki)
        talk(wiki)
    elif 'thank you' in command:
        talk("It's my duty")
    elif 'your awesome' in command:
        talk('Not more than you')
    elif 'joke' in command:
        joke = pyjokes.get_joke()
        print(joke)
        talk(joke)
    elif 'what is your name' in command:
    	talk('My name is sai')
    elif 'search' in command:
        require = command.replace('search', '')
        question = pywhatkit.search(require)
        print(require)
        talk('searching' + require)
    else:
        talk('Please say the command again.')
run_sai()
