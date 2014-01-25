# Tetras.py

import pygame
import random

class tetras:
	def __init__(self, surf, x, y, inner_colour, outer_colour):
		self.surf = surf
		self.inner_colour = inner_colour
		self.outer_colour = outer_colour
		self.shape = []
		self.coord_list = []
		# I, O, T, J, L, Z, S:	
		self.shapes = [
		[[1, 1, 1, 1], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]],
		[[0, 1, 1, 0], [0, 1, 1, 0], [0, 0, 0, 0], [0, 0, 0, 0]],
		[[0, 1, 1, 1], [0, 0, 1, 0], [0, 0, 0, 0], [0, 0, 0, 0]],
		[[0, 1, 1, 1], [0, 0, 0, 1], [0, 0, 0, 0], [0, 0, 0, 0]],
		[[1, 1, 1, 0], [1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]],
		[[0, 1, 1, 0], [0, 0, 1, 1], [0, 0, 0, 0], [0, 0, 0, 0]], 
		[[0, 1, 1, 0], [1, 1, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]]
		self.new_shape()
	
	def new_shape(self):
		choice = self.shapes[random.randrange(7)]
		self.shape = [[i, k] for i, j in enumerate(choice) for k, l in enumerate(j) if l==1]			
	
	# add left/right checks for move_(dir) methods.
	def move_left(self):
		for y, j in enumerate(self.shape):
			self.shape[y][1] -= 1	# decrement column 
		
	def move_right(self):
		for y, j in enumerate(self.shape):
			self.shape[y][1] += 1	# increment column
		
	def move_down(self):
		for y, j in enumerate(self.shape):
			self.shape[y][0] += 1	# increment row
		
	#def update(self):
	#	self.ydropped += 30
	#	self.coord_list = []
	#	for row in range(4):
	#		self.currenty = (self.initialy * (row + 1)) + self.ydropped
	#		for column, val in enumerate(self.shape[row]):
	#			self.currentx = self.initialx * (column + 1)
	#			if val == 0:
	#				pass
	#			elif val == 1:
	#				coords = ((self.currenty/30)-1, (self.currentx/30)-1)
	#				self.coord_list.append(coords)
					
					
	'''	
	Old Methods
		
	# def draw(self):
		
		#			pygame.draw.rect(self.surf, self.outer_colour, (self.currentx, self.currenty, 30, 30))
		#			pygame.draw.rect(self.surf, self.inner_colour, (self.currentx+2, self.currenty+2, 26, 26))
		#			print "Printing what we drew"
		#			print self.currentx, self.currenty
	
	'''
	
	
	
	