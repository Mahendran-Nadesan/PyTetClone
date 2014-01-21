# Python Tetris clone

import pygame
import sys
import time
import random
import Pieces
from Tetras import tetras
from Board import board
from pygame.locals import *


HEIGHT = 600
WIDTH = 300
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)	
FPS = 2
BLOCK_SIZE = 30

def main_window():
	
	pygame.init()
	fps_clock = pygame.time.Clock()
	main_win = pygame.display.set_mode((WIDTH, HEIGHT))
	new_board = board(main_win, (HEIGHT/BLOCK_SIZE), (WIDTH/BLOCK_SIZE), BLUE, BLACK)
	current_shape = tetras(main_win, 30, 30, YELLOW, BLACK)
	
	while True:
		print "Main Loop starts"
		fps_clock.tick(FPS)
		# main_win.fill((255, 255, 255))
		
		#if current_shape.currenty - ((3 - current_shape.maxy) * 30) < (HEIGHT): # this needs to be modified to account for the I tetra when horizontal (3 empty rows = 90)
			#print current_shape.maxy
		current_shape.update()
		new_board.update(current_shape)
		if new_board.collision(current_shape, HEIGHT) == False:
			print "Stuff's happening!!"
			print "Permanents: ", new_board.permanents
			new_board.draw()
			
		else:
			print "Nothing doing!!"
			print new_board.get_board()
			current_shape = tetras(main_win, 30, 30, YELLOW, BLACK)
			print "Permanents: ", new_board.permanents
			new_board.draw()	
		
		pygame.display.update()
		
		print "Main Loop ends"	
		
		
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				print new_board.get_board() # this may not be useful
				pygame.quit()
				sys.exit()
				
def main():
	main_window()

if __name__ == "__main__":
	main()
