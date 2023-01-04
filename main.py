import time
import os
# https://www.w3schools.com/python/python_file_handling.asp

shift = 0
alphabet = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz 1234567890.!?&\\@#$%^*(){}[]-_=+;:<>,/?~|"
final = ""
choice = 0
# VARIABLES

def enigma(shift, length, script) :
	message = ""
	for i in range(length):
		char = script[i]
		if char in alphabet:
			temp = alphabet.rfind(char) - shift
			message += alphabet[temp]
		else:
			message += "□"
	return message
#the en operation

def denigma(shift, length, script):
	message = ""
	for i in range(length):
		char = script[i]
		temp = alphabet.rfind(char) + shift
		while temp >= 93:
			temp -= 93
		message += alphabet[temp]
	return message
#the de operation

def load():
	for i in range (4):
		os.system("clear")
		print("loading |.|")
		time.sleep(0.2)
		os.system("clear")
		print("loading |...|")
		time.sleep(0.2)
		os.system("clear")
		print("loading |.....|")
		time.sleep(0.2)
	

def the_full_product(shift, length , script, choice, name):
	
	#makes it less than 26
	while shift >= 91:
		shift -= 91
	if int(choice) == 1:
		make_file(shift, length, script, name)
		load()
		os.system("clear")
		print("")
		print("")
		time.sleep(0.1)
		print("File made.")
		#doing the actual operation
		
	else:
		something = get_message(shift, name)
		if os.path.exists(name):
			os.remove(name)
		load()
		os.system("clear")
		print("")
		print("")
		time.sleep(0.1)
		print("This is the uncensored text: " + something)
		#doing the actual operation
		
def make_file(shift, length, script, file_name):
	f = open(file_name.upper(), 'w')
	print("make file started")
	content = enigma(shift, length, script)
	f.write(content)
	f.close()
	
def get_message(shift, file_name):
	#add file name check
	f = open(file_name.upper(), 'r')
	thing = f.read()
	length = len(thing)
	anotherthing = denigma(shift, length, thing)
	f.close()
	return anotherthing

# MAIN

print("")
print("")
length = 0

while True:
	choice = input("Would you like to enigma (1) or denigma (2) a text? ")
	if choice != "1" and choice != "2":
		print("Thats not a valid input, try again. ")
	else:
		break

#getting de or en/checking if valid

while True:
	try:
		shift = int(input("What would you like to make the key? (insert a number 1 - infinity) "))
		break
	except:
		print("That isn't an integer!!! ")
		continue
#get the shift
		
script = "Nothin here"
if int(choice) == 2:
	while True:
		name = input("What file would you like to denigma??? (¡ctrl + v the file name here!)").upper()
		if os.path.exists(name):
			break
		else:
			print("That doesn't exist!!!")
	#checking if the file exists
			
	the_full_product(shift, length, script, choice, name)
#denigma info
	
else:
	script = input("What would you like enigma??? ")
	length = len(script)
	while True:
		name = input("What would you like to name the message???").upper()
		if os.path.exists(name):
				print("That alread exists!!!")
		else:
			break
	#checking if the file exists
	the_full_product(shift, length, script, choice, name)
#enigma info