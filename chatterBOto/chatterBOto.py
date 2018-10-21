# -*- coding:utf-8 -*-

from chatterbot import ChatBot

chatbot = ChatBot(
      
    "BOTACO",
    trainer = "chatterbot.trainers.ChatterBotCorpusTrainer"
    )

#chatbot.train(
#    "chatterbot.corpus.spanish"
#    )

while True:
      try:
           conversniveldios = raw_input("Tú >")
           respuestniveldios = chatbot.get_response(conversniveldios)
           print ("Bot >"+str(respuestniveldios))

      except:
            print "lo siento no te entiendo"
