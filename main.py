import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

# Initialize recognizer and TTS engine
listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # Set voice to the second option (usually female)

def talk(text):

    engine.say(text)
    engine.runAndWait()

def take_command():

    try:
        with sr.Microphone() as source:
            print('Listening...')
            listener.adjust_for_ambient_noise(source)  # Adjust for ambient noise
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '').strip()
                print(command)
            else:
                command = ''
    except sr.UnknownValueError:
        print("Sorry, I did not understand that.")
        command = ''
    except sr.RequestError:
        print("Could not request results; check your network connection.")
        command = ''
    except OSError as e:
        print(f"An OS error occurred: {e}")
        command = ''
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        command = ''
    return command

def run_alexa():

    command = take_command()
    if command:
        print(f"Command: {command}")
        if 'play' in command:
            song = command.replace('play', '').strip()
            talk('Playing ' + song)
            pywhatkit.playonyt(song)
        elif 'time' in command:
            time = datetime.datetime.now().strftime('%I:%M %p')
            talk('Current time is ' + time)
        elif 'who the heck is' in command:
            person = command.replace('who the heck is', '').strip()
            info = wikipedia.summary(person, sentences=1)
            print(info)
            talk(info)
        elif 'date' in command:
            talk('Sorry, I have a headache')
        elif 'are you single' in command:
            talk('I am in a relationship with wifi')
        elif 'joke' in command:
            talk(pyjokes.get_joke())
        else:
            talk('Please say the command again.')


while True:
    try:
        run_alexa()
    except KeyboardInterrupt:
        print("Program terminated by user.")

        break
