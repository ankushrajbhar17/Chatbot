import random

# Define a dictionary of predefined responses
responses = {
#HEY , HI , HEELO
    "hello": ["Hello!", "Hi there!", "Hey!"],
    "Hello": ["Hello!", "Hi there!", "Hey!"],
    "HELLO": ["Hello!", "Hi there!", "Hey!"],
    "He": ["Hello!", "Hi there!", "Hey!"],
    "he": ["Hello!", "Hi there!", "Hey!"],
    "HE": ["Hello!", "Hi there!", "Hey!"],
    "hi bro": ["Hello!", "Hi there!", "Hey!"],
    "Hey": ["Hello!", "Hi there!", "Hey!"],
    "HEY": ["Hello!", "Hi there!", "Hey!"],
    "hey": ["Hello!", "Hi there!", "Hey!"],
    "HI": ["Hello!", "Hi there!", "Hey!"],
    "Hi": ["Hello!", "Hi there!", "Hey!"],
    "hi": ["Hello!", "Hi there!", "Hey!"],
    "hii": ["Hello!", "Hi there!", "Hey!"],
    "HII": ["Hello!", "Hi there!", "Hey!"],
    "Hii": ["Hello!", "Hi there!", "Hey!"],
    "hiii": ["Hello!", "Hi there!", "Hey!"],
    "HIII": ["Hello!", "Hi there!", "Hey!"],
    "Hiii": ["Hello!", "Hi there!", "Hey!"],
    "HI BOT": ["Hello!", "Hi there!", "Hey!"],
    "Hi bot": ["Hello!", "Hi there!", "Hey!"],
    "hi bot": ["Hello!", "Hi there!", "Hey!"],
    "He bot": ["Hello!", "Hi there!", "Hey!"],
    "Hello bot": ["Hello!", "Hi there!", "Hey!"],
    "HELLO BOT": ["Hello!", "Hi there!", "Hey!"],
    "hey bot": ["Hello!", "Hi there!", "Hey!"],
    "He bot": ["Hello!", "Hi there!", "Hey!"],
    "HI CHATBOT": ["Hello!", "Hi there!", "Hey!"],
    "Hi chatbot": ["Hello!", "Hi there!", "Hey!"],
    "hi chatbot": ["Hello!", "Hi there!", "Hey!"],
    "He chatbot": ["Hello!", "Hi there!", "Hey!"],
    "Hello chatbot": ["Hello!", "Hi there!", "Hey!"],
    "HELLO CHATBOT": ["Hello!", "Hi there!", "Hey!"],
    "hey chatbot": ["Hello!", "Hi there!", "Hey!"],
    "He chatbot": ["Hello!", "Hi there!", "Hey!"],
    " ": ["Please type something","Empty Space not allowed"],
#HOW ARE YOU
    "How are you": ["I'm just a computer program, but I'm doing well. How about you?", "I don't have feelings, but thanks for asking!"],
    "how are you": ["I'm just a computer program, but I'm doing well. How about you?", "I don't have feelings, but thanks for asking!"],
    "How are you?": ["I'm just a computer program, but I'm doing well. How about you?", "I don't have feelings, but thanks for asking!"],
    "how are you?": ["I'm just a computer program, but I'm doing well. How about you?", "I don't have feelings, but thanks for asking!"],
    "HOW ARE YOU": ["I'm just a computer program, but I'm doing well. How about you?", "I don't have feelings, but thanks for asking!"],
    "HOW ARE YOU?": ["I'm just a computer program, but I'm doing well. How about you?", "I don't have feelings, but thanks for asking!"],
    "How are you": ["I'm just a computer program, but I'm doing well. How about you?", "I don't have feelings, but thanks for asking!"],
    "how are you": ["I'm just a computer program, but I'm doing well. How about you?", "I don't have feelings, but thanks for asking!"],
    "How are you chatbuddy?": ["I'm just a computer program, but I'm doing well. How about you?", "I don't have feelings, but thanks for asking!"],
    "how are you chatbuddy?": ["I'm just a computer program, but I'm doing well. How about you?", "I don't have feelings, but thanks for asking!"],
    "HOW ARE YOU CHATBUDDY": ["I'm just a computer program, but I'm doing well. How about you?", "I don't have feelings, but thanks for asking!"],
    "HOW ARE YOU CHATBUDDY?": ["I'm just a computer program, but I'm doing well. How about you?", "I don't have feelings, but thanks for asking!"],
    "How are you bot": ["I'm just a computer program, but I'm doing well. How about you?", "I don't have feelings, but thanks for asking!"],
    "how are you bot": ["I'm just a computer program, but I'm doing well. How about you?", "I don't have feelings, but thanks for asking!"],
    "How are you bot?": ["I'm just a computer program, but I'm doing well. How about you?", "I don't have feelings, but thanks for asking!"],
    "how are you bot?": ["I'm just a computer program, but I'm doing well. How about you?", "I don't have feelings, but thanks for asking!"],
    "HOW ARE YOU BOT": ["I'm just a computer program, but I'm doing well. How about you?", "I don't have feelings, but thanks for asking!"],
    "HOW ARE YOU BOT?": ["I'm just a computer program, but I'm doing well. How about you?", "I don't have feelings, but thanks for asking!"],
#WHAT IS YOUR NAME
    "what your name": ["I'm just a chatbot , But You can call me Chatbuddy"],
    "what's your name": ["I'm just a chatbot , But You can call me Chatbuddy"],
    "WHAT'S YOUR NAME": ["I'm just a chatbot , But You can call me Chatbuddy"],
    "YOUR NAME": ["I'm just a chatbot , But You can call me Chatbuddy"],
    "your name": ["I'm just a chatbot , But You can call me Chatbuddy"],
    "name": ["I'm just a chatbot , But You can call me Chatbuddy"],
    "NAME?": ["I'm just a chatbot , But You can call me Chatbuddy"],
    "YOUR NAME": ["I'm just a chatbot , But You can call me Chatbuddy"],
    "your name?": ["I'm just a chatbot , But You can call me Chatbuddy"],
    "YOUR NAME?": ["I'm just a chatbot , But You can call me Chatbuddy"],
    "what your name?": ["I'm just a chatbot , But You can call me Chatbuddy"],
    "what's your name?": ["I'm just a chatbot , But You can call me Chatbuddy"],
    "WHAT'S YOUR NAME?": ["I'm just a chatbot , But You can call me Chatbuddy"],

#OWNER , FOUNDER , CREATED BY ANKUSH RAJBHAR
    "owner name": ["created by Ankush Rajbhar","Mr. Ankush Rajbhar" ,"Created By Ankush Rajbhar","Program By Ankush Rajbhar","Program By Mr. Ankush Rajbhar","Program and Created By Ankush Rajbhar"],
    "OWNER NAME": ["created by Ankush Rajbhar","Mr. Ankush Rajbhar" ,"Created By Ankush Rajbhar","Program By Ankush Rajbhar","Program By Mr. Ankush Rajbhar","Program and Created By Ankush Rajbhar"],
    "Owner Name": ["created by Ankush Rajbhar","Mr. Ankush Rajbhar" ,"Created By Ankush Rajbhar","Program By Ankush Rajbhar","Program By Mr. Ankush Rajbhar","Program and Created By Ankush Rajbhar"],
    "your owner name": ["created by Ankush Rajbhar","Mr. Ankush Rajbhar" ,"Created By Ankush Rajbhar","Program By Ankush Rajbhar","Program By Mr. Ankush Rajbhar","Program and Created By Ankush Rajbhar"],
    "what your owner name": ["created by Ankush Rajbhar","Mr. Ankush Rajbhar" ,"Created By Ankush Rajbhar","Program By Ankush Rajbhar","Program By Mr. Ankush Rajbhar","Program and Created By Ankush Rajbhar"],
    "what's owner name": ["created by Ankush Rajbhar","Mr. Ankush Rajbhar" ,"Created By Ankush Rajbhar","Program By Ankush Rajbhar","Program By Mr. Ankush Rajbhar","Program and Created By Ankush Rajbhar"],
    "WHAT YOUR OWNER NAME": ["created by Ankush Rajbhar","Mr. Ankush Rajbhar" ,"Created By Ankush Rajbhar","Program By Ankush Rajbhar","Program By Mr. Ankush Rajbhar","Program and Created By Ankush Rajbhar"],
    "WHAT'S YOUR OWNER NAME": ["created by Ankush Rajbhar","Mr. Ankush Rajbhar" ,"Created By Ankush Rajbhar","Program By Ankush Rajbhar","Program By Mr. Ankush Rajbhar","Program and Created By Ankush Rajbhar"],
    "WHO PROGRAM YOU?": ["created by Ankush Rajbhar","Mr. Ankush Rajbhar" ,"Created By Ankush Rajbhar","Program By Ankush Rajbhar","Program By Mr. Ankush Rajbhar","Program and Created By Ankush Rajbhar"],
    "who program you?": ["created by Ankush Rajbhar","Mr. Ankush Rajbhar" ,"Created By Ankush Rajbhar","Program By Ankush Rajbhar","Program By Mr. Ankush Rajbhar","Program and Created By Ankush Rajbhar"],
    "who pragram you": ["created by Ankush Rajbhar","Mr. Ankush Rajbhar" ,"Created By Ankush Rajbhar","Program By Ankush Rajbhar","Program By Mr. Ankush Rajbhar","Program and Created By Ankush Rajbhar"],
    "who create you": ["created by Ankush Rajbhar","Mr. Ankush Rajbhar" ,"Created By Ankush Rajbhar","Program By Ankush Rajbhar","Program By Mr. Ankush Rajbhar","Program and Created By Ankush Rajbhar"],
    "WHO CREATE YOU": ["created by Ankush Rajbhar","Mr. Ankush Rajbhar" ,"Created By Ankush Rajbhar","Program By Ankush Rajbhar","Program By Mr. Ankush Rajbhar","Program and Created By Ankush Rajbhar"],
    "WHO CREATE YOU?": ["created by Ankush Rajbhar","Mr. Ankush Rajbhar" ,"Created By Ankush Rajbhar","Program By Ankush Rajbhar","Program By Mr. Ankush Rajbhar","Program and Created By Ankush Rajbhar"],
    "WHO INVENT YOU": ["created by Ankush Rajbhar","Mr. Ankush Rajbhar" ,"Created By Ankush Rajbhar","Program By Ankush Rajbhar","Program By Mr. Ankush Rajbhar","Program and Created By Ankush Rajbhar"],
    "who invent you": ["created by Ankush Rajbhar","Mr. Ankush Rajbhar" ,"Created By Ankush Rajbhar","Program By Ankush Rajbhar","Program By Mr. Ankush Rajbhar","Program and Created By Ankush Rajbhar"],
    "owner name?": ["created by Ankush Rajbhar","Mr. Ankush Rajbhar" ,"Created By Ankush Rajbhar","Program By Ankush Rajbhar","Program By Mr. Ankush Rajbhar","Program and Created By Ankush Rajbhar"],
    "OWNER NAME?": ["created by Ankush Rajbhar","Mr. Ankush Rajbhar" ,"Created By Ankush Rajbhar","Program By Ankush Rajbhar","Program By Mr. Ankush Rajbhar","Program and Created By Ankush Rajbhar"],
    "Owner Name?": ["created by Ankush Rajbhar","Mr. Ankush Rajbhar" ,"Created By Ankush Rajbhar","Program By Ankush Rajbhar","Program By Mr. Ankush Rajbhar","Program and Created By Ankush Rajbhar"],
    "your owner name?": ["created by Ankush Rajbhar","Mr. Ankush Rajbhar" ,"Created By Ankush Rajbhar","Program By Ankush Rajbhar","Program By Mr. Ankush Rajbhar","Program and Created By Ankush Rajbhar"],
    "what your owner name?": ["created by Ankush Rajbhar","Mr. Ankush Rajbhar" ,"Created By Ankush Rajbhar","Program By Ankush Rajbhar","Program By Mr. Ankush Rajbhar","Program and Created By Ankush Rajbhar"],
    "what's owner name?": ["created by Ankush Rajbhar","Mr. Ankush Rajbhar" ,"Created By Ankush Rajbhar","Program By Ankush Rajbhar","Program By Mr. Ankush Rajbhar","Program and Created By Ankush Rajbhar"],
    "WHAT YOUR OWNER NAME?": ["created by Ankush Rajbhar","Mr. Ankush Rajbhar" ,"Created By Ankush Rajbhar","Program By Ankush Rajbhar","Program By Mr. Ankush Rajbhar","Program and Created By Ankush Rajbhar"],
    "WHAT'S YOUR OWNER NAME?": ["created by Ankush Rajbhar","Mr. Ankush Rajbhar" ,"Created By Ankush Rajbhar","Program By Ankush Rajbhar","Program By Mr. Ankush Rajbhar","Program and Created By Ankush Rajbhar"],
#ADDING NEW 
    "ok": ["Yeah !","You can ask me anything freely"],
    "Well": ["I'm just a chatbot.", "You can call me ChatGPT."],
    "what your name": ["I'm just a chatbot.", "You can call me Chatbuddy."],
    "your name": ["I'm just a chatbot.", "You can call me Chatbuddy."],
    "name": ["I'm just a chatbot.", "You can call me Chatbuddy."],
    "goodbye": ["Goodbye!", "See you later!", "Farewell!"]
}

def chatbot_response(user_input):
    user_input = user_input.lower()
    for key in responses:
        if key in user_input:
            return random.choice(responses[key])
    return "I'm not sure how to respond to that."

print("Hello! I'm your chatbuddy. Type 'goodbye' to exit.")
while True:
    user_input = input("Me: ")
    if user_input.lower() == "goodbye":
        print("Chatbuddy: Goodbye!")
        break
    response = chatbot_response(user_input)
    print("Chatbuddy:", response)
