import speech_recognition as sr
import pyttsx3 as tts
import os, sys, time

# Obiekty
r = sr.Recognizer()
engine = tts.init()
engine.setProperty('voice', engine.getProperty('voices')[0].id)

# Wczytać firefoxa
firefox = 'C:\\"Program Files"\\"Mozilla Firefox"\\firefox.exe'

def speak(text):
	engine.say(text)
	engine.runAndWait()

def getText():
	try:
		with sr.Microphone() as source:
			print("Nasłuchuję...", end='\r')
			audio = r.listen(source)
			text = r.recognize_google(audio, language="pl-PL")
			if text == "":
				return None
			else:
				return text
	except:
		return None

def czy_zawiera(string, slowa):
	return [element for element in slowa if element in string.lower()]

#	for element in slowa:
#		if element in string.lower():
#			lista.append(element)
# return lista

# Stałe listy gestów
WYKRYJ = ['bot', 'robot', 'robocie']
DOWIDZENIA = ['dowidzenia', 'do widzenia', 'papa', 'żegnaj']
SZUKAJ = ['wyszukaj', 'szukaj', 'znajdź', 'google', 'googluj', 'pokaż']

print("Aby wyjść powiedz 'Dowidzenia'")
while True:
	time.sleep(0.5)
	cur = getText()
	print(cur)
	print(" "*50, end="\r")
	if cur != None:
		if len(czy_zawiera(cur, WYKRYJ)):
			if len(czy_zawiera(cur, DOWIDZENIA)):
				speak("Żegnaj.")
				break
			elif len(czy_zawiera(cur, SZUKAJ)):
				linczek = cur.lower().split(' ' + czy_zawiera(cur, SZUKAJ)[0] + ' ')[1]
				speak("Oto co udało mi się znaleźć.")
				url = "https://www.google.com/search?q=" + linczek.replace(" ", "+").replace("?", "%3F")
				os.system(firefox + " " + url)

				# www.google.pl/search?q=jak+zrobić+naleśniki
				# 'Robocie', 'jak zrobić nalesniki'
