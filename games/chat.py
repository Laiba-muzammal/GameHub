import nltk
from nltk.chat.util import Chat, reflections
import random

conversation=[ 
        [r"hello|hi|hy",["Hello! How are you?","Hi, how can I help you?","Hy! What's up"]],
        [r"What's your name?",["I am an AI assistant , You may call me Chatbot."]],
        [r"Tell me a fact",["Dolphins can hold their breath underwater for eight to ten minutes.","A baby kangaroo is called a joey.",
        "A group of hyenas is called a cackle.","Like fingerprints, everyone's tongue print is unique.",
        "An ostrich's eye is bigger than its brain.","Octopuses have three hearts."]],
        [r"Tell me a joke",["Why don't skeletons fight each other? Because they don't have the guts!",
        "Why don’t eggs tell jokes? Because they might crack up!","Why was the math book sad? Because it had too many problems!",
        "Why did the scarecrow win an award? Because he was outstanding in his field!","What do you call fake spaghetti? An impasta!"]],
        [r"What can you do?",["I can answer questions, tell jokes, and assist you with basic tasks!"]],
        [r"Where are you from?",["I exist in the digital world, so I don't have a specific place like you!"]],
        [r"Can you help me?",["Of course! Just tell me what you need help with."]],
        [r"What is the meaning of life?",["That's a deep question! Many people say the meaning of life is to find happiness and purpose"]],
        [r"What is the weather like today?",["I'm not connected to the internet, but I suggest checking a weather app!"]],
        [r"Bye|Thanks|Can you say goodbye?",["Bye! Have a nice day","Glad you find it helping, ask anything else if needed.","GoodBye."]]
]

default=["I'm not sure about that. Can you ask something else?","Sorry! I have not been trained according to this yet.",
        "Sorry, I didn't understand that. Can you rephrase?"]

basic_chatbot = Chat(conversation, reflections)

print("************CHATBOT*************")
print("Chatbot: Hello! I am your Chatbot. Ask me anything.")
print("(Note: Enter exit to end the conversation.)")

while True:
    user = input("You: ").lower()
    if user == "exit":
        print(random.choice(["Goodbye! Have a great day!","Bye, feel free to ask anything whenever needed."]))
        break

    chatbot = basic_chatbot.respond(user)
    if chatbot:
        print(f"Chatbot: {chatbot}\n")
    else:
        print(f"Chatbot: {random.choice(default)}\n")