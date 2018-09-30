from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os

bot = ChatBot('Jabba')
bot.set_trainer(ListTrainer)

for files in os.listdir('H:/Advanced Projects/chatbot-python\chatbot/chatterbot-corpus-master/chatterbot_corpus/data/english/'):
    data = open('H:/Advanced Projects/chatbot-python/chatbot/chatterbot-corpus-master/chatterbot_corpus/data/english/' + files, 'r').readlines()
    bot.train(data)

while True:
    message = input('You: ')


    
    if message.strip() !=  'Bye':
        
        reply = bot.get_response(message)
        
        print('ChatBot: ', reply)


        
    if message.strip() == 'Bye':

        print('ChatBot: ', 'Alrighty then, till next time.')
        break
