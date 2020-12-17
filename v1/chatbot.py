#!/usr/bin/env python3  # Datei wird automatisch mit Python3 ausgeführt
# -*- coding: utf-8 -*-  # Definiert ...

# Ein einfacher Chatbot
# (c) 2020 by me, Lizenz GPLv3

print("")
print("Willkommen beim Chatbot (v1)")
print("")
print("Worüber wollen Sie sprechen?")
print("Zum Beenden, geben Sie bye ein...")
print("")

nutzereingabe = ""  # Variable wird als String initialisiert
nutzereingabe = input("Ihre Frage oder Antwort: ")

if nutzereingabe == "bye":
    print("Beende Chatbot, schönen Tag....")
    exit()
print("Danke")