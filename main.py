#imports
from random import randint

import pickle, time, os, sys, pygame

# yup this is colours
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

#turn to true to break the game
dev = False

homescreen = True
 
firsttime = True

#home screen (load or new save game)
if homescreen == True:
  
  time.sleep(4)
  
  os.system('clear')
  
  print(red,"===============================")
  
  print(cyan, "")
  
  hello_msg =("Welcome to [Generic Text game]!\n")
  
  for char in hello_msg:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.05) 
    
  print(red, "\n===============================\n")
  
  print(white, "To start a new game type new or to load a save type load\n")
  
  if dev:
    print("Welcome back sir")
    
  new = ("new")
  
  save = ("load")
  
  make_me_a_dev = ("toggle dev")
  
  while homescreen == True:
    
    user_input = input("")
    
    if save == user_input:
      Level = pickle.load(open("Save.dat", "rb"))
      homescreen = False
      
    if new == user_input:
      Level = 0
      
      homescreen = False
      
    if make_me_a_dev == user_input:
      
      if dev == False:
       
        dev = True
        
        print(blue, "\ndev mode on")
        
        print(white,"")
        
      else:
        
        dev = False
       
        print(blue, "\ndev mode off")
        
        print(white,"")

#first level
if Level == 0:
	# gives the backround of the level
	
	os.system('clear')
	
	time.sleep(2)
	
	print(green, "")
	
	level1_msg = ("LEVEL 1\n-------")
	
	for char in level1_msg:
		  sys.stdout.write(char)
		  sys.stdout.flush()
		  time.sleep(0.05) 
	
	time.sleep(2)
	
	print(white, "\nyou wake up in a room.\n")
	
	time.sleep(1)
	
	print("There is a table with a box on it to the left of you. There is also a door to the right of you.\n")
	
	time.sleep(1)
	
	print("write commands in normal English")
	
	print("")

	#functions that get valid input
	openbox = ("open the box")

	opendoor = ("open the door")

	getkey = ("get the key")
	
	if dev: 
	  complete = ("complete")

	while Level == 0:
		# locks the door at the begining of the level
		if firsttime == True:
		
			haskey = False
		
			boxopen = False
		
			firsttime = False

		#checks for an input
		player_input = input("")

		if openbox == player_input:
			print("\nyou open the box. Inside there is a key ")
			
			print("")

			boxopen = True

		if getkey == player_input:
			if boxopen:
				print("\nyou got the key")
				
				print("")

				haskey = True

		#opens the door
		if opendoor == player_input:
			#checks that the player has the key
			if haskey:
				print("\nyou opened the door!")
				
				print("")

				time.sleep(3)

				print("you finished the level!")

				#ends the level and starts the next
				Level = 1
				pickle.dump(Level, open("Save.dat", "wb"))
				break

			else:
				print("\nthe door is locked.")
		
		if dev:		
		  if complete == player_input:
		    Level = 1
		    
		    pickle.dump(Level, open("Save.dat", "wb"))
		    
		    break
		  
#Second Level
if Level == 1:
  
  os.system('clear')
  
  print(magenta, "LEVEL 2\n -------")
  
  print(white, "\nyou are now in a tunnel\n")
  
  time.sleep(2)
  
  print(" the floor is covered in rocks. You see that the tunnel forks\n")
  
  time.sleep(3)
  
  print("Will you turn left or right")
  
  complete = ("complete")
 
  correcttunnel = randint(1, 2)
  
  devnum = str(correcttunnel)
  
  correct_tunnel = int(correcttunnel)
  
  if correct_tunnel == 1:
    
    tunnel = ("left")
    
    wrong_tunnel = ("right")
    
  else:
    tunnel = ("right")
    
    wrong_tunnel = ("left")
    
  if dev:
    print("" + devnum + "")
    
  while Level == 1:
    
    player_input = input("")
    
    if player_input == tunnel:
      
      Level = 1.1
      
      pickle.dump(Level, open("Save.dat", "wb"))
      
      break
      
    elif player_input == wrong_tunnel:
      
      print("\nyou come to another turning")
      
      print("left or right?\n")
      
      
      correcttunnel = randint(1, 2)
      
      devnum = str(correcttunnel)
      
      correct_tunnel = int(correcttunnel)
      
      if correct_tunnel == 1:
        
        tunnel = ("left")
        
        wrong_tunnel = ("right")
        
      else:
        
        tunnel = ("right")
        
        wrong_tunnel = ("left")
        
      if dev:
        print("" + devnum + "")
        
      
      if dev:
        
        if complete == player_input:
          Level = 1.1
          
          pickle.dump(Level, open("Save.dat", "wb"))
        
          break
		  
#Second Level part 2
if Level == 1.1:

	#opening text
	os.system('clear')
	
	print(magenta,"ROOM 2\n ------")
	
	time.sleep(2)
	
	print(white, "You walk down the tunnel and enter another room\n")
	
	time.sleep(3)

	print(
	    "The room you are now in has a high vaulted ceiling and another large door at the end of the room\n"
	)

	time.sleep(3)

	print(
	    "The door has no handle but you see that there are four coloured buttons in the walls: red, yellow, green and blue\n"
	)

	time.sleep(3)

	print("there is also a pannel on the wall displaying the number 0 \n")

	time.sleep(10)

	print("after a while you notice an object in the corner ")
	
	print("")

	# all the actions
	red_button = ("press the red button")

	blue_button = ("press the blue button")

	green_button = ("press the green button")

	yellow_button = ("press the yellow button")

	scroll_pickup = ("get the object")

	scroll_inspect = ("inspect the scroll")

	lever_pull = ("pull the lever")

	check_number = ("check the pannel")

	# stuff to do with the door mechanism
	code_number = 0

	correct_number = randint(3, 45)

	correct_number_print = str(correct_number)

	pannel_showing = str(code_number)

	# tell us that you dont have the scroll
	has_sroll = False

	while Level == 1.1:
		# gets what the user types
		player_input = input("")

		# get the input and give the appropriate responce
		if player_input == red_button:

			print("you press the red button")

			code_number = code_number + 1

		if player_input == blue_button:

			print("you press the blue button")

			code_number = code_number - 1

		if player_input == green_button:

			print("you press the green button")

			code_number = code_number * 2

		if player_input == yellow_button:

			print("you press the yellow button")

			code_number = code_number / 2

		if player_input == scroll_pickup:
			print("you pick the item up it is a srcoll")

			has_scroll = True

		if player_input == scroll_inspect:
			if has_scroll == True:
				print("you inspect the scroll")

				time.sleep(2)

				print( "on it there is some text. It says 'the path unfolds with the number " + correct_number_print + "")
				
		if player_input == check_number:
		  print("The pannel shows the number " + pannel_showing + "")
      
		if code_number == correct_number:
			print("suddenly the door slams open with some force")

			Level = 1.2

			pickle.dump(Level, open("Save.dat", "wb"))

#second Level part 3
if Level == 1.2:
  print ("you walk through the door")
  
quit()

  