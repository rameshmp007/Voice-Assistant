
import speech_recognition
import pyttsx3
from pyttsx3 import engine
import datetime
import time
import webbrowser
from googlesearch import search
import subprocess
import pyjokes
import wikipedia
import os
import random
import smtplib
from email.message import EmailMessage
import send_email as se

    

#to listen the query
def record_voice():

	microphone = speech_recognition.Recognizer()	

	with speech_recognition.Microphone() as live_phone:
		microphone.adjust_for_ambient_noise(live_phone)

		print("\nListening...")
		try:
			audio = microphone.listen(live_phone, phrase_time_limit=7)
			phrase = microphone.recognize_google(audio, language='en')
			print(f"query: {phrase}")
			return phrase
		except:
			text_to_speech("I didn't understand what you said")



#converts text to speech
def text_to_speech(phrase):
 
	global output
	output = phrase
	print(phrase) 
	engine.say(phrase) 
	engine.runAndWait()
	



#greets the user when the program runs
def greet():

	hour = int(datetime.datetime.now().hour)
	if hour == 0:
		phrase = f"Good morning Boss. It\'s {12 + hour} AM in the morning. How can I help you?"
	
	elif hour > 0 and hour <= 12:
		phrase = f"Good morning Boss. It\'s {hour} AM in the morning. How can I help you?"
	
	elif hour > 12 and hour <= 16:
		phrase = f"Good afternoon Boss. It\'s {hour - 12} PM in the noon. How can I help you?"
	
	elif hour > 16 and hour <= 20:
		phrase = f"Good evening Boss. It\'s {hour - 12} PM in the evening. How can I help you?"
	
	else:
		phrase = f"Good evening Boss. It\'s {hour - 12} PM in the night. How can I help you?"
	
	text_to_speech(phrase)


#used to search a query in google
def google(query):


	query = query.replace("Google ", "")	
	webbrowser.open(search(query)[0])

	text_to_speech(f"Googling {query}")

	time.sleep(10.0)



#used to open a app using its link
def open_app(link):
	subprocess.Popen(link)
	time.sleep(10.0)



#searches in wikipedia and gives result in voice
def wiki():
	global query
	query = query.lower()
	query = query.replace("wikipedia ", "")
	try:
		return wikipedia.summary(query, sentences = 2)
	except:
		return f"Cannot find {query}"

#used to send email 
def email():
	sender = se.sender
	password = se.password
	receiver = 'pawarramesh2001@gmail.com'
	text_to_speech("mention the message")
	message = record_voice()

	# action
	msg = EmailMessage()
	msg['Subject'] = 'Email sent using Python'   
	msg['from'] = sender
	msg['to'] = receiver
	msg.set_content(message)


	server = smtplib.SMTP('64.233.184.108', 587)
	server.ehlo()
	server.starttls()
	server.login(sender,password)


	server.send_message(msg)
	text_to_speech("Email sent")
	server.quit()

#used to write a note 
def write_note():
	
	content = ""
	note = open("note.txt", 'a')
	text_to_speech("What should I add?")

	while True:

		note.write(content)
		note.write("\n")
		content = record_voice()
		if content == 'no':
			break
		text_to_speech("Anything else?")

	note.close()
	time.sleep(10.0)


#used to create note
def show_note():
	note = open("note.txt", 'r')
	content = note.read()
	text_to_speech(content)
	time.sleep(5.0)


#used to pause the programme
def pause():
	text_to_speech("I am not Listening...\nPress <ENTER> key to continue...")
	input()

#used to open calculator
def calc():
	os.system('calc.exe')

#game to play when the user is bored
def game():
	calc()
	text_to_speech("Choose any whole number")
	time.sleep(8.0)
	text_to_speech("\nmultiply the choosen number with 10")
	time.sleep(8.0)
	text_to_speech("add the resulting number with 10")
	time.sleep(8.0)
	text_to_speech("\nmultiply the resulting number with 5")
	time.sleep(8.0)
	text_to_speech("add the given number with 5")
	time.sleep(8.0)

	text_to_speech("\nEnter the resulting number: ")
	answer = int(input())
	number = int((answer - 55) / 50)
	text_to_speech(f"\nThe number you have choosen is: {number}")

#main function
def main():


		



	greet()

	while True:



		query = record_voice()
			

		if query == None or query == "":
			text_to_speech("I didn't understand what you said")
			
		elif "quit" in query.lower() or "close" in query.lower():
			quit()

		elif "stop" in query.lower():
			quit()

		elif "google" in query.lower():
			google(query)

		elif "calculator" in query.lower():
			calc()

		elif "figma" in query.lower():
			open_app("C:\\Users\\Asus\\AppData\\Local\\Figma\\Figma.exe")

		elif "code" in query.lower():
			open_app("C:\\Users\\Asus\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")

		elif "notepad" in query.lower():
			open_app("C:\\Windows\\notepad.exe") 
			
		elif "joke" in query.lower():
			text_to_speech(pyjokes.get_joke())
				
		elif "wikipedia" in query.lower():
			text_to_speech( wiki() )

		elif "play music" in query.lower() or "play song" in query.lower():
			music_dir = 'D:\\songs'
			songs = os.listdir(music_dir) 
			print(len(songs)) 
			os.startfile(os.path.join(music_dir, songs[random.randrange( len( songs ) )]))

		elif "mail" in query.lower() or "email" in query.lower():
			email()

		elif "write a note" in query.lower():
			write_note()

		elif "show note" in query.lower():
			show_note()

		elif "pause" in query.lower():
			pause()

		elif "bored" in query.lower():
			game()

		elif "smart" in query.lower():
			text_to_speech("It is obviously Aniketh Mahadik")

		elif "silent" in query.lower():
			text_to_speech("It is you Boss")

		elif "thank you" in query.lower():
			text_to_speech("Pleasure is mine")






engine = pyttsx3.init()
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 130)
engine.setProperty('volume', 0.9)


output = ''
query = ''


main()
