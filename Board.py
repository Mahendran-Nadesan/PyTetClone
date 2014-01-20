# Board.py

from Tetras import tetras
import pygame

class board:
	def __init__(self, surf, num_rows, num_columns, inner_colour, outer_colour):
		self.surf = surf
		self.num_rows = num_rows
		self.num_columns = num_columns
		self.inner_colour = inner_colour
		self.outer_colour = outer_colour
		self.board = []
		for i in range(num_rows):
			self.board.append([1] * num_columns)
		#print self.board	
		#return self.board
		
	def draw(self):
		for row in range(self.num_rows):
			y = 30 * (row)
			for column in range(self.num_columns):
				x = 30 * (column)
				if self.board[row][column]==1:
					pygame.draw.rect(self.surf, self.outer_colour, (x, y, 30, 30))
					pygame.draw.rect(self.surf, self.inner_colour, (x+2, y+2, 26, 26))
				else:
					pass
	
		
	def get_board(self):
		return self.board
		
	
	