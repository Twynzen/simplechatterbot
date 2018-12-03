# -*- coding:utf-8 -*-

from chatterbot import ChatBot
import os
import sys

chatbot = ChatBot(
      
    "Franzusco",
    trainer = "chatterbot.trainers.ChatterBotCorpusTrainer"
    )

#chatbot.train(
#    "chatterbot.corpus.spanish"
#    )

while True:
      try:
           conversniveldios = raw_input("Tú >")
           respuestniveldios = chatbot.get_response(conversniveldios)
           print ("Franzusco >"+str(respuestniveldios))
           os.system("espeak " + str(respuestniveldios))
                      
      except:
            print "Franzusco >lo siento no te entiendo"
            os.system("espeak " + str("losientonoteentiendo"))
