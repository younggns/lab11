import pygame

pygame.init()

Display = pygame.display.set_mode((600,300))

pygame.display.set_caption("Bar Graph")
pygame.display.update()

white = (255,255,255)
black = (0,0,0)
red = (255, 0, 0)
green = (0, 255, 0)
yellow = (255, 255, 0)

# You will be visualizing this data. 
# (Label, Color of the bar, Length of the bar)
data = [('Apple',red,15), ('Banana',yellow,45), ('Melon',green,28)]


# Design your own Class
# The class should be initialized with the label, color, and length of each item in the 'data' list.
# The class should have a function(or multiple functions) to draw a bar graph.


loopCond = True
while loopCond:
	Display.fill(white)

	# Write the codes to draw a graph based on 'data' list.
	
	pygame.display.update()	


pygame.quit()
quit()