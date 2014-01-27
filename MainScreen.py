# Python Tetris clone

import pygame
import sys
import time
import random
import Pieces
from Tetras import tetras
from Board import board
from pygame.locals import *

COLOURS = [
(255, 255, 255), 
(255, 0, 0),
(0, 255, 0),
(255, 255, 0),
(0, 255, 255)]
HEIGHT = 600
WIDTH = 300
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)	
FPS = 2
BLOCK_SIZE = 30

def handle_events(shape, event_key):
	#pygame.time.set_timer(USEREVENT+1, 100)
	if event_key == pygame.K_RIGHT:
		shape.move_right()
	elif event_key == pygame.K_LEFT:
		shape.move_left()
	
def main_window():
	DROP_EVENT = USEREVENT + 1
	
	
	lost = False
	pygame.init()
	fps_clock = pygame.time.Clock()
	main_win = pygame.display.set_mode((WIDTH, HEIGHT))
	new_board = board(main_win, (HEIGHT/BLOCK_SIZE), (WIDTH/BLOCK_SIZE), BLUE, BLACK)
	current_shape = tetras(main_win, 30, 30, COLOURS[random.randrange(5)], BLACK)
	
	pygame.time.set_timer(DROP_EVENT, 1000) # moves down every second, make this a variable later.
	
	while True:
		
		print "Main Loop starts"
		
		fps_clock.tick(FPS)
		
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
			elif event.type == KEYDOWN:
				handle_events(current_shape, event.key)
			elif event.type == DROP_EVENT:
				current_shape.move_down()
	
			
		new_board.update(current_shape)
		
		if new_board.collision(current_shape) == False:
			new_board.draw()
		else:
			current_shape = tetras(main_win, 30, 30, COLOURS[random.randrange(5)], BLACK)
			new_board.draw()	
			
		pygame.display.update()
		
		print "Main Loop ends"	
		
		
		#for event in pygame.event.get():
		#	if event.type == pygame.QUIT:
		#		print new_board.get_board() # this may not be useful
		#		pygame.quit()
		#		sys.exit()
				
def main():
	main_window()

if __name__ == "__main__":
	main()
