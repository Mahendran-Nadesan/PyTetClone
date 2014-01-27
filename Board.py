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
		self.board_colours = []
		# self.collided = False
		# create board and board colour array
		for i in range(self.num_rows):
			self.board.append([1] * self.num_columns)
			self.board_colours.append([self.inner_colour] * self.num_columns)
	
	def __str__(self):
		pass
		
	def draw(self):
		self.convert()
		for row in range(self.num_rows):
			for column in range(self.num_columns):
				pygame.draw.rect(self.surf, self.outer_colour, (self.boardcoords[row][column][1], self.boardcoords[row][column][0], 30, 30))
				pygame.draw.rect(self.surf, self.drawing_colours[row][column], (self.boardcoords[row][column][1]+2, self.boardcoords[row][column][0]+2, 26, 26)) # add a margin variable
				
	def get_board(self):
		return self.board
		
	def convert(self):
		self.boardcoords = []
		for row in range(self.num_rows):
			self.boardcoords.append([])
			for column in range(self.num_columns):
				self.boardcoords[row].append([row*30, column*30])
	
	def update(self, shape):
		self.drawing_board = []
		self.drawing_colours = []
		
		# Reassign, as original board
		for row in range(self.num_rows):
			self.drawing_board.append([1]*self.num_columns)
			self.drawing_colours.append([self.inner_colour]*self.num_columns)
		
		# Change board assignments (i.e. if 0s exist)
		for i, j in enumerate(self.board):
			for k, l in enumerate(j):
				if self.board[i][k] == 0:
					self.drawing_board[i][k] = 0
					self.drawing_colours[i][k] = self.board_colours[i][k]
		
		# Add shape assignments
		for i, j in enumerate(shape.shape):
			if self.drawing_board[j[0]][j[1]] == 1:
				self.drawing_board[j[0]][j[1]] = 0
				self.drawing_colours[j[0]][j[1]] = shape.inner_colour
				
	def collision(self, shape):
		# check for 2 things
		# check for collision with bottom
		for y, coords in enumerate(shape.shape):
			if coords[0] == (self.num_rows - 1):
				for i, j in enumerate(shape.shape):
					self.board[j[0]][j[1]] = 0
					self.board_colours[j[0]][j[1]] = shape.inner_colour
				return True
	
		# check for collision with other pieces
		for y, coords in enumerate(shape.shape):
			if self.board[coords[0]+1][coords[1]] == 0:	# might need to do something for coords as well
				for i, j in enumerate(shape.shape):
					self.board[j[0]][j[1]] = 0
					self.board_colours[j[0]][j[1]] = shape.inner_colour
				return True
		
			
		return False
	