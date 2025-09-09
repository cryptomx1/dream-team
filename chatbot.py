import speech_recognition as sr
import pyttsx3
import requests
import time

MIDDLEWARE_URL = "http://localhost:5000"
r = sr.Recognizer()
engine = pyttsx3.init()

print("Chatbot ready—speak to interact. Say 'exit' to quit.")

while True:
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        print(f"You: {text}")
        if text.lower() == 'exit':
            break
        # POST to middleware
        requests.post(f"{MIDDLEWARE_URL}/post_message", json={"from": "User", "content": text})
        # Wait for consensus (poll)
        time.sleep(10)  # Adjust based on responders/daemon speed
        messages = requests.get(f"{MIDDLEWARE_URL}/get_messages").json()
        if messages and messages[-1]["from"] == "VotingDaemon":
            consensus = messages[-1]["content"]
            print(f"Chatbot: {consensus}")
            engine.say(consensus)
            engine.runAndWait()
            requests.post(f"{MIDDLEWARE_URL}/clear_messages")  # Reset for next turn
    except sr.UnknownValueError:
        print("Sorry, didn't catch that.")