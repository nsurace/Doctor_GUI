'''
Program: doctorGUI.py
Author: Nick Surace
Date: 4/30/2020
Summary: GUI Version that - Conducts an interactive session of nondirective psychotherapy
'''
from breezypythongui import EasyFrame
import random
from tkinter import * 

#Global Variables
hedges = ("Please tell me more.", "Many of my patients tell me the same thing.", "Please continue.")

qualifiers = ("Why do you say that ",  "You seem to think that ", "Can you explain why ")

replacements = {"i":"you", "I":"you", "me":"you", "my":"your", "we":"you", "us":"you", "mine":"yours", "am":"are"}

class DoctorGUI(EasyFrame):
	'''Interactive session psychotherapy'''
	def __init__(self):
		'''Sets up the window and the widgets'''
		EasyFrame.__init__(self, title = "Doctor GUI")
		self.addLabel(text = "Good Morning, I hope you are well today", row = 0 , column = 0, sticky = "NSEW")
		self.addLabel(text = "What can i do for you?", row = 1 , column = 0, sticky = "NSEW")
		self.userText = self.addTextField(text = "", row = 2, column = 0, sticky = "NSEW")
		self.userText.focus_set() #focus cursor on the input field
		#Bind the enter key to the input field
		self.userText.bind("<Return>", lambda event: self.reply())
		self.responseLabel = self.addLabel(text = "", row = 3, column = 0, sticky = "NSEW")
		self.addButton(text = "Submit", row = 4, column = 0, command = self.reply)
		
	def reply(self):
		#Builds and returns a reply to the sentence
		sentence = self.userText.getText()
		probability = random.randint(1, 4)
		if probability == 1:
			self.responseLabel["text"] = random.choice(hedges)
		else:
			self.responseLabel["text"] = random.choice(qualifiers) + changePerson(sentence)
			self.userText.setText("")

#Global Function
def changePerson(sentence):
	#Replaces first person pronouns with second person pronouns
	words = sentence.split()
	replyWords = []
	for word in words:
		replyWords.append(replacements.get(word, word))
	return" ".join(replyWords)

def main():
	'''Instantiates and pops up the window'''
	DoctorGUI().mainloop()		

#Global call to main() function
main()