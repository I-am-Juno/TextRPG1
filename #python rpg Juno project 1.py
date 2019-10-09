#python rpg Juno project 1

import cmd
import textwrap
import sys
import os
import time
import random

screen_width = 100


#### Player Setup ####
class player:
	def__init__(self):
	   self.name= 'Juno'
	   self.hp = 0
	   self.ap = 0
	   self.status_effect= []
MyPlayer= player()

#### Title Screen ####
def title_screen_selections():
    option = input("> ")
    if option.lower() == ("play"):
   		 start_game() #placeholder until written
   	elif option.lower() == ("help"):
   		help_menu()
   	elif option.lower() == ("quit"):
   		sys.exit() 
   	while option.lower() not in ['play','help','quit']:
   		  print("please enter a vallid command.")
   			  option = input("> ")
    	if option.lower() == ("play"):
   			 start_game() #placeholder until written
   		elif option.lower() == ("help"):
   			help_menu()
   		elif option.lower() == ("quit"):
   			sys.exit() 
   			
def title_screen():
	os.system('clear')
	print(#####################)
	print('Welcome to Text RPG')
	print(#####################)
	print('    -Play-         ')
	print('    -Help-         ')
	print('    -Quit-         ')

	print('Copyright 2017 I-am-Juno') #and whoever else helps
	titles_screen_selections()

def help_menu():
	print(#####################)
	print('Welcome to Text RPG')
	print(#####################)
	print('-Use up, down, left, right to move')
	print('-Type your comands to do them')
	print('-Use look to inspect something')
	print('-Good luck Have fun')
	title_screen_selections()

def start_game():
