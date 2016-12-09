import pygame
import random
import math
from cell import Cell
			
class Game:

	def init_cells(self):
		for y in range(self.NUM_SQUARES):
			for x in range(self.NUM_SQUARES):
				c = Cell(x,y)
				self.cells.append(c)


	def __init__(self):

		self.BLOCK_SIZE = 40
		self.NUM_SQUARES = 20
		self.WHITE  = (255,255,255)
		self.BLACK = (0,0,0)
		self.WINDOW_WIDTH = (self.BLOCK_SIZE) * self.NUM_SQUARES + 40
		self.WINDOW_HEIGHT = (self.BLOCK_SIZE) * self.NUM_SQUARES + 40

		self.cells = []
		self.init_cells()

	def draw_board(self):
		for c in self.cells:
			walls = c.get_walls(self)
			for wall in walls:
				pygame.draw.line(self.window, self.WHITE, wall[0], wall[1])


	def getPresentFrame(self):
		pygame.event.pump()
		self.draw_board()
		#updates the window
		pygame.display.flip()
		

	def getNextFrame(self):
		pygame.event.pump()
		self.draw_board()
		#update the window
		pygame.display.flip()


	def run(self):
		pygame.init()
		self.window = pygame.display.set_mode((self.WINDOW_WIDTH, self.WINDOW_HEIGHT))
		self.getPresentFrame()
		running = True
		while running:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					running = False
				else:
					self.getNextFrame()

		pygame.quit()

g = Game()
g.run()