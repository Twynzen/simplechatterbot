# -*- coding:utf-8 -*-

import os
import sys

os.system("sudo pip install chatterbot")

from chatterbot import ChatBot
 
chatbot = ChatBot(
    "BOTACO",
    trainer = "chatterbot.trainers.ChatterBotCorpusTrainer"
    )

chatbot.train(
    "chatterbot.corpus.spanish"
    )
