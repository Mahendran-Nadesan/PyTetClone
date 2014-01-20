# Python Tetris clone

import pygame
import sys
import time
import random
import Pieces
from Tetras import tetras
from Board import board
from pygame.locals import *



# Temp/test functions (eventually to be added to classes, etc.)
def draw_tile(surf, x, y, inner_colour, outer_colour):
	
	pygame.draw.rect(surf, outer_colour, (x, y, BLOCK_SIZE, BLOCK_SIZE))
	pygame.draw.rect(surf, inner_colour, (x+2, y+2, 26, 26))

HEIGHT = 600
WIDTH = 300
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)	
FPS = 1
BLOCK_SIZE = 30
SHAPES = [
[[1, 1, 1, 1], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]],
[[0, 1, 1, 0], [0, 1, 1, 0], [0, 0, 0, 0], [0, 0, 0, 0]],
[[0, 1, 1, 1], [0, 0, 1, 0], [0, 0, 0, 0], [0, 0, 0, 0]],
[[0, 1, 1, 1], [0, 0, 0, 1], [0, 0, 0, 0], [0, 0, 0, 0]],
[[1, 1, 1, 0], [1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]],
[[0, 1, 1, 0], [0, 0, 1, 1], [0, 0, 0, 0], [0, 0, 0, 0]],
[[0, 1, 1, 0], [1, 1, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]]

# I, O, T, J, L, Z, S	
I_SHAPE = [[1, 1, 1, 1], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
O_SHAPE = [[0, 1, 1, 0], [0, 1, 1, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
T_SHAPE = [[0, 1, 1, 1], [0, 0, 1, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
J_SHAPE = [[0, 1, 1, 1], [0, 0, 0, 1], [0, 0, 0, 0], [0, 0, 0, 0]]
L_SHAPE = [[1, 1, 1, 0], [1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
Z_SHAPE = [[0, 1, 1, 0], [0, 0, 1, 1], [0, 0, 0, 0], [0, 0, 0, 0]]
S_SHAPE = [[0, 1, 1, 0], [1, 1, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

def gen_shape(surf, shape, start_pos, inner_colour, outer_colour):
##	print "gen_shape started"
	for i in range(4):
##		print "loop entered"
		y = start_pos[1]*(i+1)
##		print 'y is %i' % y
##		print 'i is %i' % i
		for j, k in enumerate(shape[i]): # can I use enum?
			x = start_pos[0]*(j+1)
##			print "x: %i, y: %i, j: %i, k: %i" % (x, y, j, k)
##			print "x is %i" % x
##			print "j is %i" % j
##			print "k is %i" % k
			if k==0:
				pass
			elif k==1:
				draw_tile(surf, x, y, inner_colour, outer_colour)
##				print "drawing %i %i" % (x, y)
##	print "gen_shape_done"



def gen_board(surf, inner_colour, outer_colour):
	num_rows = HEIGHT/BLOCK_SIZE
	num_columns = WIDTH/BLOCK_SIZE
	board = []
	for i in range(num_rows):
		board.append([1] * num_columns)
	# gen_shape(surf, board, [0, 0], BLUE, BLACK) # lol, gen_shape uses range(4), i.e. shapes only
	# s = [draw_tile(surf, (x, y), BLUE, BLACK) for x, y in smallfunc(x, y)]
	for row in range(num_rows):
		y = BLOCK_SIZE*(row)
		for column in range(num_columns):
			x = BLOCK_SIZE*(column)
			if board[row][column]==1:
				draw_tile(surf, x, y, inner_colour, outer_colour)
			else:
				pass
	

def main_window():
	
	pygame.init()
	
	
	
	fps_clock = pygame.time.Clock()
	main_win = pygame.display.set_mode((WIDTH, HEIGHT))
	new_board = board(main_win, (HEIGHT/BLOCK_SIZE), (WIDTH/BLOCK_SIZE), BLUE, BLACK)
	current_shape = tetras(main_win, 30, 30, YELLOW, BLACK)
	
	while True:
		fps_clock.tick(FPS)
		main_win.fill((255, 255, 255))
		# pygame.draw.rect(main_win, (0, 0, 0), (10, 10, BLOCK_SIZE, BLOCK_SIZE))
		# draw_tile(main_win, BLOCK_SIZE, BLOCK_SIZE)
		# test all shapes
		# for i, j in enumerate(SHAPES):
			# gen_shape(main_win, j, [BLOCK_SIZE, BLOCK_SIZE+(i*BLOCK_SIZE)])
		
		
		if current_shape.currenty < (HEIGHT):
			print current_shape.currenty
			print "working check"
			current_shape.update()
		else:
			current_shape = tetras(main_win, 30, 30, YELLOW, BLACK)
			print "working too"
			
		# gen_board(main_win, BLUE, BLACK)
		# gen_shape(main_win, SHAPES[random.randrange(7)], [BLOCK_SIZE, BLOCK_SIZE], YELLOW, BLACK)
		new_board.draw()	
		print "Drawing current shape"
		current_shape.draw()
		# drop_shape(main_win)
		# if fps_clock.get_time() == 2000:
		
		
		pygame.display.update()
		print "main loop works..."	
		
		
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
				
def main():
	main_window()

if __name__ == "__main__":
	main()
