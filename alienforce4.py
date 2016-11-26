# Things to fix - change time between updates to compensate for longer loop iterations

from SimpleGraphics import *
from time import sleep

# Initialize variables for referencing the width and height of the window
width  = 420
height = 420

dimension = 20

pixels_per_turn = 5

shipx = width  - dimension
shipy = height - dimension

shots_fired    = 0
max_shots      = 1
shot_size      = 6
shotx          = None
shoty          = None
shot_direction = None

u_coord = [shipx, shipy + dimension, shipx + 0.5 * dimension, shipy, shipx + dimension, shipy + dimension]
d_coord = [shipx, shipy, shipx + 0.5 * dimension, shipy + dimension, shipx + dimension, shipy]
l_coord = [shipx + dimension, shipy, shipx, shipy + 0.5 * dimension, shipx + dimension, shipy + dimension]
r_coord = [shipx, shipy, shipx + dimension, shipy + 0.5 * dimension, shipx, shipy + dimension]

direction      = None
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
	if   direction == "U":
		polygon(*u_coord)
	elif direction == "D":
		polygon(*d_coord)
	elif direction == None or direction == "L":
		polygon(*l_coord)
	elif direction == "R":
		polygon(*r_coord)
	
	if shots_fired > 0:
		if shot_direction == "U":
			# Determine the immediate future (i.e., next iteration) position of the shot
			nextx = shotx
			nexty = shoty
			
			nexty -= 2 * pixels_per_turn
			
			# If the future position escapes the borders, prevent the shot from moving further
			if nextx < 0 or nextx + shot_size > width or nexty < 0 or nexty + shot_size > height:
				shots_fired = 0
			# Otherwise move the shot
			else:
				shotx = nextx
				shoty = nexty
		elif shot_direction == "D":
			# Determine the immediate future (i.e., next iteration) position of the shot
			nextx = shotx
			nexty = shoty
			
			nexty += 2 * pixels_per_turn
			
			# If the future position escapes the borders, prevent the shot from moving further
			if nextx < 0 or nextx + shot_size > width or nexty < 0 or nexty + shot_size > height:
				shots_fired = 0
			# Otherwise move the shot
			else:
				shotx = nextx
				shoty = nexty
		elif shot_direction == "L":
			# Determine the immediate future (i.e., next iteration) position of the shot
			nextx = shotx
			nexty = shoty
			
			nextx -= 2 * pixels_per_turn
			
			# If the future position escapes the borders, prevent the shot from moving further
			if nextx < 0 or nextx + shot_size > width or nexty < 0 or nexty + shot_size > height:
				shots_fired = 0
			# Otherwise move the shot
			else:
				shotx = nextx
				shoty = nexty
		else:
			# Determine the immediate future (i.e., next iteration) position of the shot
			nextx = shotx
			nexty = shoty
			
			nextx += 2 * pixels_per_turn
			
			# If the future position escapes the borders, prevent the shot from moving further
			if nextx < 0 or nextx + shot_size > width or nexty < 0 or nexty + shot_size > height:
				shots_fired = 0
			# Otherwise move the shot
			else:
				shotx = nextx
				shoty = nexty
		
		setColor("white")
		ellipse(shotx, shoty, shot_size, shot_size)
		print("shot drawn")
	
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
	if   "space" in keys and shots_fired < max_shots:
		print("shot fired")
		shots_fired = 1
		shot_direction = direction
		if direction == "U":
			shotx = int(u_coord[2] - 0.5 * shot_size)
			shoty = int(u_coord[3] - shot_size)
		elif direction == "D":
			shotx = int(d_coord[2] - 0.5 * shot_size)
			shoty = int(d_coord[3] + shot_size)
		elif direction == "L":
			shotx = int(l_coord[2] - shot_size)
			shoty = int(l_coord[3] - 0.5 * shot_size)
		else:
			shotx = int(r_coord[2] - shot_size)
			shoty = int(r_coord[3] - 0.5 * shot_size)
		print("shotx is", shotx, "and shoty is", shoty)
	elif "Up"    in keys:
		next_direction = "U"
		continue
	elif "Down"  in keys:
		next_direction = "D"
		continue
	elif "Left"  in keys:
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
	
	u_coord = [shipx, shipy + dimension, shipx + 0.5 * dimension, shipy, shipx + dimension, shipy + dimension]
	d_coord = [shipx, shipy, shipx + 0.5 * dimension, shipy + dimension, shipx + dimension, shipy]
	l_coord = [shipx + dimension, shipy, shipx, shipy + 0.5 * dimension, shipx + dimension, shipy + dimension]
	r_coord = [shipx, shipy, shipx + dimension, shipy + 0.5 * dimension, shipx, shipy + dimension]	

# If the game has ended but the window is still open, display "Game Over"
clear()
setFont("System", 54, "bold")
setColor("white")
text(width / 2, height / 2, "Game Over")
update()