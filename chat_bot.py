import random
print("Bot: Hey!, I am pybot")
print("Bot: Whats your name?")
name = input("You: ").strip().title()
print(f"Bot: Nice to meet you, {name}!")  
while True:
    message = input("You: ").lower().strip()

    if message == "bye":
        print("Goodbye bro")
        break
    elif "name" in message:
        print(random.choice(["Nice to meet you", "Thats a nice name"]))
    elif "hello" in message or "hi" in message or "wassup" in message:
        print("Wassup, how are you doing?")
    elif "tired" in message or "sad" in message or "angry" in message or "depressed" in message:
        print(random.choice(["Oh i am so sorry to hear that",
                             "no worries, everything will be fine"]))
    elif "good" in message or "nice" in message or fine in message:
        print(random.choice(["Thats great to hear. Is there anything you wanna talk about today?",
                             "Good, so tell me about your day and how it has been"]))
    elif "dumb" in message or "idiot" in message or "stupid" in message:
        print(random.choice(["Bro, i am just a simple chat bot, i am not able to do comlex things, pardon me",
                             "I was created by a software engineering student of Veritas University named Samuel, so he is still working to add more features"]))

    elif "game" in message:
        print(random.choice(["U wanna play a game?"]))
    elif "football" in message or "basketball" in message or "table tennis" in message or "volleyball" in message or "dance" in message:
        print(random.choice(["Oh, thats nice! so tell me, when did you start",
              "Cool, so what position do you enjoy playing?"]))
    elif "thank you" in message:
        print("You are welcome, anytime man")
    else:
        print("Tell me more about your day")
    

    
