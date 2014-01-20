# Tetras.py

import pygame
import random

class tetras:
	def __init__(self, surf, x, y, inner_colour, outer_colour):
		self.surf = surf
		self.initialx = x
		self.initialy = y
		self.currentx = x
		self.currenty = y
		self.inner_colour = inner_colour
		self.outer_colour = outer_colour
		self.shape = []
		self.ydropped = 0
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
		self.shape = self.shapes[random.randrange(7)]
		print "Printing new shape"
		print self.shape
		return self.shape
		
	def draw(self):
		for row in range(4):
			self.currenty = (self.initialy * (row + 1)) + self.ydropped
			print self.currenty, self.ydropped
			for column, val in enumerate(self.shape[row]):
				print "Printing..."
				print row, column, val
				self.currentx = self.initialx * (column + 1)
				if val == 0:
					pass
				elif val == 1:
					pygame.draw.rect(self.surf, self.outer_colour, (self.currentx, self.currenty, 30, 30))
					pygame.draw.rect(self.surf, self.inner_colour, (self.currentx+2, self.currenty+2, 26, 26))
					print "Printing what we drew"
					print self.currentx, self.currenty
		
	def update(self):
		self.ydropped += 30
		
		
	
	
	