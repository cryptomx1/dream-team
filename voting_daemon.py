import time
import requests
from collections import Counter\nimport pyttsx3

MIDDLEWARE_URL = "http://localhost:5000"
POLL_INTERVAL = 5  # seconds

def get_messages():
    try:
        return requests.get(f"{MIDDLEWARE_URL}/get_messages").json()
    except:
        return []

def post_message(from_ai, content):
    requests.post(f"{MIDDLEWARE_URL}/post_message", json={"from": from_ai, "content": content})

def extract_vote(content):
    if content.endswith("[aye]"):
        return "aye"
    elif content.endswith("[nay]"):
        return "nay"
    elif content.endswith("[hold]"):
        return "hold"
    return None

print("Voting Daemon running. Polls middleware for votes.")

seen_messages = set()
while True:
    messages = get_messages()
    current_contents = {msg["content"] for msg in messages}
    new_votes = [extract_vote(content) for content in current_contents - seen_messages if extract_vote(content)]
    if new_votes:
        all_votes = [extract_vote(msg["content"]) for msg in messages if extract_vote(msg["content"])]
        tally = Counter(all_votes)
        total = len(all_votes)
        seen_messages = current_contents.copy()
        if total >= 3:
            consensus_reached = False
            for vote, count in tally.items():
                if count >= (total * 2 / 3):
                    consensus = f"Consensus reached: {vote.upper()} (tally: {tally})"
                    post_message("VotingDaemon", consensus)
                    print(consensus)\n                    engine = pyttsx3.init()\n                    engine.setProperty('rate', 150)\n                    engine.setProperty('voice', 'com.apple.speech.synthesis.voice.samantha')\n                    engine.say(consensus)\n                    engine.runAndWait()
                    requests.post(f"{MIDDLEWARE_URL}/clear_messages")
                    seen_messages.clear()
                    consensus_reached = True
                    break
            if not consensus_reached and len(set(tally.values())) == 1:
                flag = f"Tie detected—flagging for review (tally: {tally})"
                post_message("VotingDaemon", flag)
                print(flag)\n                engine = pyttsx3.init()\n                engine.setProperty('rate', 150)\n                engine.setProperty('voice', 'com.apple.speech.synthesis.voice.samantha')\n                engine.say(flag)\n                engine.runAndWait()
    time.sleep(POLL_INTERVAL)