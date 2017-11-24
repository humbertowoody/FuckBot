#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Fuck Bot

import tweepy, time, sys

# DATOS DE LA API
CONSUMER_KEY =		"7XLGopH54FPOfoMPxdH5Qg90z" 							# ID de la App
CONSUMER_SECRET =	"soZdEPWv3jQWPUGZ5xrtFfabm4ZuWvfeVjR4rkMia0cw9B1dfP" 	# AUTH de la App

# DATOS DE LA CUENTA FUCKBOT
ACCESS_KEY =		"4761171228-Wmnh5ShphTobwmpgGexNd60h0xInh2H7XlmMnZq" 	# Llave de la cuenta
ACCESS_SECRET =		"Mg4UAdRd04OkuUShLZETMtBMMNRt3SoQcuHLXE4HgBbOa" 		# Autorización de la cuenta

print 'Inicia proceso de verificación'
auth = tweepy.OAuthHandler(CONSUMER_KEY,CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY,ACCESS_SECRET)

api = tweepy.API(auth)
print 'Autenticado (con el servidor)'

print 'Enviando mensaje...'
api.send_direct_message(screen_name='humbertowoody',text='Valió verga, de nuevo.')
print 'Mensaje enviado!'

#End of Program
