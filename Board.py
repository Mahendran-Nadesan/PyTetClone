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
		self.board_filled = []
		self.collided = False
		self.permanents = []
		# create board and board colour array
		for i in range(self.num_rows):
			self.board.append([1] * self.num_columns)
			self.board_colours.append([self.inner_colour] * self.num_columns)
		
	def draw(self):
		for row in range(self.num_rows):
			y = 30 * (row)										# add BLOCK_SIZE instead of 30
			for column in range(self.num_columns):
				x = 30 * (column)								# add BLOCK_SIZE instead of 30
				#if self.board[row][column]==1:
				pygame.draw.rect(self.surf, self.outer_colour, (x, y, 30, 30))
				pygame.draw.rect(self.surf, self.board_colours[row][column], (x+2, y+2, 26, 26)) # add a margin variable
				#else:
				#	pass
		
	def get_board(self):
		return self.board
	
	def update(self, shape):
		# add list coords of current shape to board list
		print shape.currenty
		self.board_filled = []
		self.board_filled.append(shape.coord_list)
		# change the colour of the appropriate tiles
		# I dislike this method - find a different way
		for i, j in enumerate(self.board_colours):
			for k, l in enumerate(j):							# [i][k] are the indices
				#self.board[i][k] = 1
				self.board_colours[i][k] = self.inner_colour 	# reset them all to blue (use commented method below?)
				for m in self.board_filled[0]:
					if m[0] == i and m[1] == k:					# check if the values in list are equal to the array indices
						#self.board[i][k] = 0
						self.board_colours[i][k] = shape.inner_colour	# change to shape's colour
					else:
						pass
				if len(self.permanents)==0:
					pass
				else:
					for n, o in enumerate(self.permanents):
						for p in o:
							self.board_colours[p[0]][p[1]] = (255, 0, 0)
						#if n[0] == i and n[1] == k:
						#	self.board[i][k] = 0
						#	self.board_colours[i][k] = (255, 0, 0)
		
		
		# other method for resetting colours to blue
		# for colours in range(self.num_rows):
			# self.board_colours.append([self.inner_colour] * self.num_columns)
		
		# find some way to delete them, but not delete accumulations
			
	def collision(self, shape, height):
		
		# check for collision with bottom
		if shape.currenty - ((3-shape.maxy)*30) == height:
			self.permanents.append(shape.coord_list)
			for i, j in enumerate(self.board_colours):
				for k, l in enumerate(j):							# [i][k] are the indices
					#self.board[i][k] = 1
					self.board_colours[i][k] = self.inner_colour 	# reset them all to blue (use commented method below?)
					for m in self.board_filled[0]:
						if m[0] == i and m[1] == k:					# check if the values in list are equal to the array indices
							self.board[i][k] = 0
							self.board_colours[i][k] = shape.inner_colour	# change to shape's colour
						else:
							pass
					if len(self.permanents)==0:
						pass
					else:
						for n, o in enumerate(self.permanents):
							for p in o:
								self.board_colours[p[0]][p[1]] = (255, 0, 0)
			return True
			
		elif shape.currenty - ((3-shape.maxy)*30) < height:
			for i, j in enumerate(self.board):
				if 0 in j:
					print "THIS ROW HAS A ZERO"
					print i
					if ((shape.currenty/30)+1)==i:
						self.permanents.append(shape.coord_list)
						return True
					else:
						return False
				else:
					return False
		#	for i, j in enumerate(self.permanents):
		#		for k in j:
		#			if shape.currenty - ((3-shape.maxy)*30) == k[0]:
		#				self.board_colours[k[0]][k[1]] = (255, 0, 0)
					
			# self.board
		#	print "end reached"
		#	print shape.currenty
		#	print shape.coord_list
			
		else:
			print "False"
			return False
		
		
	
	