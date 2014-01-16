# Python Tetris clone

import pygame
import sys
import time
import random
import Pieces
from pygame.locals import *



# Temp/test functions (eventually to be added to classes, etc.)
def draw_tile(surf, x, y):
	outer_colour = (0, 0, 0)
	inner_colour = (255, 255, 0)
	pygame.draw.rect(surf, outer_colour, (x, y, 30, 30))
	pygame.draw.rect(surf, inner_colour, (x+3, y+3, 24, 24))

BLOCK_SIZE = 20
L_SHAPE = [[1, 1, 1, 1]]
T_SHAPE = [[0, 1, 1, 1], [0, 0, 1, 0]]
	
def gen_shape(surf, shape, start_pos):
	print "gen_shape started"
	for i in range(len(shape)):
		print "loop entered"
		y = start_pos[1]*(i+1)
		print 'y is %i' % y
		print 'i is %i' % i
		for j in range(len(shape[i])):
			x = start_pos[0]*(j+1)
			print x
			print "j is %i" % j
			if shape[i][j]==0:
				pass
			else:
				draw_tile(surf, x, y)


def main_window():
	
	pygame.init()
	
	HEIGHT = 400
	WIDTH = 300
	
	fps_clock = pygame.time.Clock()
	main_win = pygame.display.set_mode((WIDTH, HEIGHT))
		
	while True:
		main_win.fill((255, 255, 255))
		# pygame.draw.rect(main_win, (0, 0, 0), (10, 10, 30, 30))
		# draw_tile(main_win, 30, 30)
		gen_shape(main_win, T_SHAPE, [30, 30])
		print "main loop works"	
		fps_clock.tick(1)
		pygame.display.update()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
				
def main():
	main_window()

if __name__ == "__main__":
	main()
