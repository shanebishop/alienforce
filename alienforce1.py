from SimpleGraphics import *
from time import sleep

# Initialize variables for referencing the width and height of the window
__width  = 420
__height = 420

__dimension = 20

__pixels_per_turn = 5

__shipx = __width  - __dimension
__shipy = __height - __dimension

__direction = None

__delay = 0.05

__turn_l_or_r = []
__turn_u_or_d = []
for i in range(11):
	__turn_l_or_r.append(i * 2 * __dimension)
	__turn_u_or_d.append(i * 2 * __dimension)

# Initialize some graphical elements
setAutoUpdate(False)
resize(__width, __height)
background("black")

def __int__(self):
	pass

def move_ship():
	# Determine the immediate future (i.e., next iteration) position of the ship
	nextx = self.__shipx
	nexty = __shipy
	
	if __direction == None:
		return False
	elif __direction == "U":
		nexty -= __pixels_per_turn
	elif __direction == "D":
		nexty += __pixels_per_turn
	elif __direction == "L" :
		nextx -= __pixels_per_turn
	elif __direction == "R":
		nextx += __pixels_per_turn
	
	__direction = None
	
	# If the future position escapes the borders, prevent the ship from moving further
	if nextx < 0 or nextx + __dimension > __width or nexty < 0 or nexty + __dimension > __height:
		pass
	# Otherwise move the ship
	else:
		__shipx = nextx
		__shipy = nexty
	
	return True

# Game loop
while not closed():
	# Clear the screen
	clear()
	
	# Draw grid
	setColor("blue")
	for i in range(__dimension, __height - __dimension, __dimension * 2):
		for j in range(__dimension, __height - __dimension, __dimension * 2):
			rect(i, j, __dimension, __dimension)
	
	# Draw the triangle
	setColor("green")
	polygon(__shipx, __shipy + __dimension, __shipx + 0.5 * __dimension, __shipy, __shipx + __dimension, __shipy + __dimension)
	
	# Update screen
	update()
	
	# Pause execution
	sleep(__delay)
	
	# Get the set of keys being held by the player
	keys = getHeldKeys()
	
	if len(keys) == 1:
		print("Ship is at", __shipx, __shipy, "with direction", keys)
		print("shipy in turn_u_or_d evaluates to", __shipy in __turn_u_or_d)
		print("shipx in turn_l_or_r evaluates to", __shipx in __turn_l_or_r)
		print(__turn_u_or_d)
		print(__turn_l_or_r)
	
	# Determine the direction the player wants to go
	if   "Up"    in keys and ((__direction == "L" or __direction == "R" or __direction == None) and __shipx in __turn_u_or_d):
		__direction = "U"
		if move_ship():
			__direction = None
		else:
			continue
	elif "Down"  in keys and ((__direction == "L" or __direction == "R" or __direction == None) and __shipx in __turn_u_or_d):
		__direction = "D"
		if move_ship():
			__direction = None
		else:
			continue
	elif "Left"  in keys and ((__direction == "U" or __direction == "D" or __direction == None) and __shipy in __turn_l_or_r):
		__direction = "L"
		if move_ship():
			__direction = None
		else:
			continue
	elif "Right" in keys and ((__direction == "U" or __direction == "D" or __direction == None) and __shipy in __turn_l_or_r):
		__direction = "R"
		if move_ship():
			__direction = None
		else:
			continue
	elif "Up" in keys:
		__direction = "U"
	elif "Down" in keys:
		__direction = "D"
	elif "Left" in keys:
		__direction = "L"
	elif "Right" in keys:
		__direction = "R"
	
	keys = None

# If the game has ended but the window is still open, display "Game Over"			
clear()
setFont("System", 54, "bold")
setColor("white")
text(width / 2, height / 2, "Game Over")
update()