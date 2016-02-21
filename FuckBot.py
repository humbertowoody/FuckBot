#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Fuck Bot

import tweepy, time, sys

ID_FILE = "id.txt"

# DATOS DE LA API
CONSUMER_KEY =		"7XLGopH54FPOfoMPxdH5Qg90z" 							# ID de la App
CONSUMER_SECRET =	"soZdEPWv3jQWPUGZ5xrtFfabm4ZuWvfeVjR4rkMia0cw9B1dfP" 	# AUTH de la App

# DATOS DE LA CUENTA FUCKBOT
ACCESS_KEY =		"4761171228-Wmnh5ShphTobwmpgGexNd60h0xInh2H7XlmMnZq" 	# Llave de la cuenta
ACCESS_SECRET =		"Mg4UAdRd04OkuUShLZETMtBMMNRt3SoQcuHLXE4HgBbOa" 		# Autorización de la cuenta

def refresh_id(text):
	f = open(ID_FILE, 'r+')
	lala = f.read()
	f.seek(0)
	f.write(str(text))
	f.truncate()
	f.close()
	return 

def last_id():
	last = 0
	with open(ID_FILE,'r+') as ar:
		last = int(ar.read())
	return last

print 'Iniciando FuckBot...'
print 'Leyendo el id del ultimo nombre...'
last_name_id = last_id()
print 'El id es '+str(last_name_id)

print 'Inicia proceso de verificación'
auth = tweepy.OAuthHandler(CONSUMER_KEY,CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY,ACCESS_SECRET)

api = tweepy.API(auth)
print 'Autenticado, inicia tuiteo'


with open('Names.txt') as f:
	i = 0
	for line in f:
		if(i < last_name_id):
			i += 1
		else:
			line = str(line).replace("\n","")
			message = 'Fuck you '+str(line)+'!'
			api.update_status(message)
			i += 1
			refresh_id(i)
			print 'Status #'+str(i)+': '+message
			time.sleep(900) # Sleep for 15 Minutes (Let's keep it realistic boys!)

#End of Program