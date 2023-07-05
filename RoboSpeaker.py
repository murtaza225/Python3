import pyttsx3

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Set the voice and rate of speech
engine.setProperty("voice", "com.apple.speech.synthesis.voice.Alex")
engine.setProperty("rate", 150)

# Function to speak the given text
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Main program loop
while True:
    user_input = input("Enter your text (press 'q' to quit): ")
    if user_input.lower() == "q":
        break
    speak(user_input)
