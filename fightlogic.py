# from random import randint

import time, sys, pygame

red = "\033[0;31m"
green = "\033[0;32m"
yellow = "\033[0;33m"
blue = "\033[0;34m"
magenta = "\033[0;35m"
cyan = "\033[0;36m"
white = "\033[0;37m"
bright_black = "\033[0;90m"
bright_red = "\033[0;91m"
bright_green = "\033[0;92m"
bright_yellow = "\033[0;93m"
bright_blue = "\033[0;94m"
bright_magenta = "\033[0;95m"
bright_cyan = "\033[0;96m"
bright_white = "\033[0;97m"


def player_move():

	print("\nits your move. will you:\n")
	print(bright_cyan, "")

	move_1 = ("1) attack ")

	move_2 = ("2) defend ")

	move_3 = ("3)heal")

#	move_1_in = str(1)

#	move_2_in = str(2)

#	move_3_in = str(3)
	
#	x = 1 
#	y = 2 
	
#	damage = randint(x, y)
	
#	player_health =(100)
	
#	player_defense = (1)

	for char in move_1:
		sys.stdout.write(char)
		sys.stdout.flush()
		time.sleep(0.05)

	for char in move_2:
		sys.stdout.write(char)
		sys.stdout.flush()
		time.sleep(0.05)

	for char in move_3:
		sys.stdout.write(char)
		sys.stdout.flush()
		time.sleep(0.05)

	while move:
		player_input = input("")
		
		
