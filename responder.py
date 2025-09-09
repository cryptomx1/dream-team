import time
import requests
import subprocess

MIDDLEWARE_URL = "http://localhost:5000"
AI_NAME = "VoiceCore"  # Change to "Claude" for other instance

def query_ai(prompt, ai_type):
    if ai_type == "VoiceCore":
        # Assuming voice_core.py can be imported or run; for simplicity, simulate
        # In real, import the generate function
        return "VoiceCore response to: " + prompt + " [aye]"
    elif ai_type == "Claude":
        proc = subprocess.Popen(["claude", prompt], stdout=subprocess.PIPE)
        response, _ = proc.communicate()
        return response.decode().strip() + " [aye]"
    return "Response [aye]"

while True:
    messages = requests.get(f"{MIDDLEWARE_URL}/get_messages").json()
    if messages and messages[-1]["from"] == "User":
        prompt = messages[-1]["content"]
        response = query_ai(prompt, AI_NAME)
        requests.post(f"{MIDDLEWARE_URL}/post_message", json={"from": AI_NAME, "content": response})
    time.sleep(5)