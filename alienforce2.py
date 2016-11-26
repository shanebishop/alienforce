from SimpleGraphics import *
from time import sleep

# Initialize variables for referencing the width and height of the window
width = 420
height = 420

dimension = 20

pixels_per_turn = 5

shipx = width  - dimension
shipy = height - dimension

direction = None
next_direction = None

delay = 0.05

turn_l_or_r = []
turn_u_or_d = []
for i in range(11):
	turn_l_or_r.append(i * 2 * dimension)
	turn_u_or_d.append(i * 2 * dimension)

# Initialize some graphical elements
setAutoUpdate(False)
resize(width, height)
background("black")

# Game loop
while not closed():
	# Clear the screen
	clear()
	
	# Draw grid
	setColor("blue")
	for i in range(dimension, height - dimension, dimension * 2):
		for j in range(dimension, height - dimension, dimension * 2):
			rect(i, j, dimension, dimension)
	
	# Draw the triangle
	setColor("green")
	polygon(shipx, shipy + dimension, shipx + 0.5 * dimension, shipy, shipx + dimension, shipy + dimension)
	
	# Update the screen
	update()
	
	# Pause execution
	sleep(delay)
	
	# Get the set of keys being held by the player
	keys = getHeldKeys()
	
	if len(keys) == 1:
		print("Ship is at", shipx, shipy, "with direction", keys)
		print("shipy in turn_u_or_d evaluates to", shipy in turn_u_or_d)
		print("shipx in turn_l_or_r evaluates to", shipx in turn_l_or_r)
		print(turn_u_or_d)
		print(turn_l_or_r)
	
	# Determine the direction the player wants to go
	if "Up" in keys:
		next_direction = "U"
		continue
	elif "Down" in keys:
		next_direction = "D"
		continue
	elif "Left" in keys:
		next_direction = "L"
		continue
	elif "Right" in keys:
		next_direction = "R"
		continue
	
	if   (next_direction == "U") and (shipx in turn_u_or_d and shipy in turn_l_or_r):
		# Determine the immediate future (i.e., next iteration) position of the ship
		nextx = shipx
		nexty = shipy
		
		nexty -= pixels_per_turn
		direction = "U"
		
		# If the future position escapes the borders, prevent the ship from moving further
		if nextx < 0 or nextx + dimension > width or nexty < 0 or nexty + dimension > height:
			pass
		# Otherwise move the ship
		else:
			shipx = nextx
			shipy = nexty
	elif (next_direction == "D") and (shipx in turn_u_or_d and shipy in turn_l_or_r):
		# Determine the immediate future (i.e., next iteration) position of the ship
		nextx = shipx
		nexty = shipy
		
		nexty += pixels_per_turn
		direction = "D"
		
		# If the future position escapes the borders, prevent the ship from moving further
		if nextx < 0 or nextx + dimension > width or nexty < 0 or nexty + dimension > height:
			pass
		# Otherwise move the ship
		else:
			shipx = nextx
			shipy = nexty
	elif (next_direction == "L") and (shipx in turn_u_or_d and shipy in turn_l_or_r):
		# Determine the immediate future (i.e., next iteration) position of the ship
		nextx = shipx
		nexty = shipy
		
		nextx -= pixels_per_turn
		direction = "L"
		
		# If the future position escapes the borders, prevent the ship from moving further
		if nextx < 0 or nextx + dimension > width or nexty < 0 or nexty + dimension > height:
			pass
		# Otherwise move the ship
		else:
			shipx = nextx
			shipy = nexty
	elif (next_direction == "R") and (shipx in turn_u_or_d and shipy in turn_l_or_r):
		# Determine the immediate future (i.e., next iteration) position of the ship
		nextx = shipx
		nexty = shipy
		
		nextx += pixels_per_turn
		direction = "R"
		
		# If the future position escapes the borders, prevent the ship from moving further
		if nextx < 0 or nextx + dimension > width or nexty < 0 or nexty + dimension > height:
			pass
		# Otherwise move the ship
		else:
			shipx = nextx
			shipy = nexty
	elif direction == "U":
		# Determine the immediate future (i.e., next iteration) position of the ship
		nextx = shipx
		nexty = shipy
		
		nexty -= pixels_per_turn
		
		# If the future position escapes the borders, prevent the ship from moving further
		if nextx < 0 or nextx + dimension > width or nexty < 0 or nexty + dimension > height:
			pass
		# Otherwise move the ship
		else:
			shipx = nextx
			shipy = nexty
	elif direction == "D":
		# Determine the immediate future (i.e., next iteration) position of the ship
		nextx = shipx
		nexty = shipy
		
		nexty += pixels_per_turn
		
		# If the future position escapes the borders, prevent the ship from moving further
		if nextx < 0 or nextx + dimension > width or nexty < 0 or nexty + dimension > height:
			pass
		# Otherwise move the ship
		else:
			shipx = nextx
			shipy = nexty
	elif direction == "L":
		# Determine the immediate future (i.e., next iteration) position of the ship
		nextx = shipx
		nexty = shipy
		
		nextx -= pixels_per_turn
		
		# If the future position escapes the borders, prevent the ship from moving further
		if nextx < 0 or nextx + dimension > width or nexty < 0 or nexty + dimension > height:
			pass
		# Otherwise move the ship
		else:
			shipx = nextx
			shipy = nexty
	elif direction == "R":
		# Determine the immediate future (i.e., next iteration) position of the ship
		nextx = shipx
		nexty = shipy
		
		nextx += pixels_per_turn
		
		# If the future position escapes the borders, prevent the ship from moving further
		if nextx < 0 or nextx + dimension > width or nexty < 0 or nexty + dimension > height:
			pass
		# Otherwise move the ship
		else:
			shipx = nextx
			shipy = nexty
	
	keys = None

# If the game has ended but the window is still open, display "Game Over"
clear()
setFont("System", 54, "bold")
setColor("white")
text(width / 2, height / 2, "Game Over")
update()