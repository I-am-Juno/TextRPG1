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
	   self.location = 'starting zone'
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


## Game Functionality ##
def start_game():


#### Map ####
#player starts at b2#
   
------------- 			----
|a1|a2|a3|a4|//////////	|f1|
------------- 			----
|b1|b2|b3|b4|
------------- 
#need railroad to accesss these parts
------------
|c1|c2|c3|c4| 
-------------  
|d1|d2|d3|d4| 
------------- 

ZONENAME = ''
Description = 'Description'
Examination = 'examine'
Solved = False
UP = 'up', 'north'
DOWN ='down', 'south'
LEFT = 'left', 'west'
RIGHT = 'right', "east"

solved_places = {'a1': False, 'a2': False, 'a3': False, 'a4': False,
                 'b1': False, 'b2': False, 'b3': False, 'b4': False,
                 }

zonemap = {
	'a1': {
		ZONENAME: "Cattle Ranch".	
		Description = 'Description'
		Examination = 'examine'
		Solved = False
		UP = 'up', 'north'
		DOWN = 'down', 'south'
		LEFT = 'left', 'west'
		RIGHT = 'right', "east"
	},
		'a2': {
		ZONENAME: "Old World Blues".	#bar
		Description = 'Description'
		Examination = 'examine'
		Solved = False
		UP = 'up', 'north'
		DOWN = 'down', 'south'
		LEFT = 'left', 'west'
		RIGHT = 'right', "east"

	},
		'a3': {
		ZONENAME: "Goliath National Bank".	
		Description = 'Description'
		Examination = 'examine'
		Solved = False
		UP = 'up', 'north'
		DOWN = 'down', 'south'
		LEFT = 'left', 'west'
		RIGHT = 'right', "east"

	},
		'a4': {
		ZONENAME: "RailRoad".	
		Description = 'Description'
		Examination = 'examine'
		Solved = False
		UP = 'up', 'north'
		DOWN = 'down', 'south'
		LEFT = 'left', 'west'
		RIGHT = 'right', "east"

	},
		'b1': {
		ZONENAME: "Town Hall".	
		Description = 'Description'
		Examination = 'examine'
		Solved = False
		UP = 'up', 'north'
		DOWN = 'down', 'south'
		LEFT = 'left', 'west'
		RIGHT = 'right', "east"

	},
	'b2': {
		ZONENAME: "Home",	
		Description = 'This is your home!'
		Examination = 'You live here, do you not remember your own house?'
		Solved = False
		UP = 'a2', 'north'
		DOWN = 'c2', 'south'
		LEFT = 'b1', 'west'
		RIGHT = 'b3', "east"

	},
	'b3': {
		ZONENAME: "Damian's Market".	
		Description = 'Description'
		Examination = 'examine'
		Solved = False
		UP = 'up', 'north'
		DOWN = 'down', 'south'
		LEFT = 'left', 'west'
		RIGHT = 'right', "east"

	},
	'b4': {
		ZONENAME: "Lake sunset".	
		Description = 'You can see the reflection of the sun in the morning'
		Examination = 'examine'
		Solved = False
		UP = 'up', 'north'
		DOWN = 'down', 'south'
		LEFT = 'left', 'west'
		RIGHT = 'right', "east"

	},
	'c1': {
		ZONENAME: "".	
		Description = 'Description'
		Examination = 'examine'
		Solved = False
		UP = 'up', 'north'
		DOWN = 'down', 'south'
		LEFT = 'left', 'west'
		RIGHT = 'right', "east"

	},
	'c2': {
		ZONENAME: "".	
		Description = 'Description'
		Examination = 'examine'
		Solved = False
		UP = 'up', 'north'
		DOWN = 'down', 'south'
		LEFT = 'left', 'west'
		RIGHT = 'right', "east"

	},
	'c3': {
		ZONENAME: "".	
		Description = 'Description'
		Examination = 'examine'
		Solved = False
		UP = 'up', 'north'
		DOWN = 'down', 'south'
		LEFT = 'left', 'west'
		RIGHT = 'right', "east"

	},
	'c4': {
		ZONENAME: "".	
		Description = 'Description'
		Examination = 'examine'
		Solved = False
		UP = 'up', 'north'
		DOWN = 'down', 'south'
		LEFT = 'left', 'west'
		RIGHT = 'right', "east"

	},
	'd1': {
		ZONENAME: "".	
		Description = 'Description'
		Examination = 'examine'
		Solved = False
		UP = 'up', 'north'
		DOWN = 'down', 'south'
		LEFT = 'left', 'west'
		RIGHT = 'right', "east"

	},
	'd2': {
		ZONENAME: "".	
		Description = 'Description'
		Examination = 'examine'
		Solved = False
		UP = 'up', 'north'
		DOWN = 'down', 'south'
		LEFT = 'left', 'west'
		RIGHT = 'right', "east"

	},
	'd3': {
		ZONENAME: "".	
		Description = 'Description'
		Examination = 'examine'
		Solved = False
		UP = 'up', 'north'
		DOWN = 'down', 'south'
		LEFT = 'left', 'west'
		RIGHT = 'right', "east"

	},
	'd4': {
		ZONENAME: "".	
		Description = 'Description'
		Examination = 'examine'
		Solved = False
		UP = 'up', 'north'
		DOWN = 'down', 'south'
		LEFT = 'left', 'west'
		RIGHT = 'right', "east"

	},
	'f1': {
		ZONENAME: "Shallow grave".	
		Description = 'You woke up in a grave with a bleading head and a missing wallet'
		Examination = 'you notice that you have enough room to move, maybe you can squirm your way out'
		Solved = False
		UP = 'up', 'north'
		DOWN = 'down', 'south'
		LEFT = 'a1', 'west'
		RIGHT = 'right', "east"

	},
}
