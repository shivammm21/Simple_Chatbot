import random
import wikipedia
you="YOU :  "
bot="BOT : "
hello=["hi","hi there","hello","hello there","hey"]
howare=["how are you","whats up","how you doing","how r u"]
who=["who are you","who r u"]
hmm=["ok","okk","okay","hm","hmm"]
name=["whats your name","what is your name","what should i call you","name"]
bye=["see you later","goodbye","bye","have a good day","by"]
live=["where are you live","what is your location","location"]
made=["who made you","who invent you"]
thanks=["thanks","thank you","thnx","thank u"]
info=["tell me the information","tell me the info","tell info","tell information","tell me info"]
doing=["what are you doing now","what are you doing"]
print("***************************************")
while True:
    user=input(you).lower()
    if(user in bye):
        botans=["sad to see you go :(","ok bye","miss you"]
        print(bot,""+random.choice(botans))
        print("***************************************")
        break
    elif(user in hello):
        botans=["hello !","hi","hi there","welcome User"]
        print(bot,""+random.choice(botans))
    elif(user in howare):
        botans=["All Well","I am fine, thanks","happy","I am good.."]
        print(bot,""+random.choice(botans))
    elif(user in name):
        botans=["My name is chatbot","You can call me Bot"]
        print(bot,""+random.choice(botans))
    elif(user in live):
        botans=["I live in your system","I live in your pc"]
        print(bot,""+random.choice(botans))
    elif(user in made):
        botans=["Made by Shivam"]
        print(bot,""+random.choice(botans))
    elif(user in doing):
        botans=["I am doing chat with you","Chatting with you"]
        print(bot,""+random.choice(botans))
    elif(user in who):
        botans=["I am a bot I can chat with you","My name is bot I can chat with you."]
        print(bot,""+random.choice(botans))
    elif(user in hmm):
        botans=["yeah","hmm","All right!"]
        print(bot,""+random.choice(botans))
    elif(user in info):
        botans=["okk, Whose information do you want?","okay..?"]
        print(bot,""+random.choice(botans))
        user_info=input(you)
        print(bot,wikipedia.summary(user_info, sentences=1)) 
        print(bot," here the information about",user_info) 
    elif(user in thanks):
        botans=["you are welcome..","Welcome..:)","wlc"]
        print(bot,""+random.choice(botans))
    else:
        botans=["sorry what ?","I can't understand what you say...."]
        print(bot,""+random.choice(botans))
