import pygame
import random
import math
import numpy
from cell import Cell

class Generator:

	def __init__(self):
		pass

	def dfs(self, game,x,y):
		
		history = [(x,y)]
	
		while history:
			game.cells[x][y].visited = True
			neighbors = []

			if x + 1 <= game.NUM_SQUARES - 1:
				if not game.cells[x+1][y].visited: neighbors.append('r')
			if x - 1 >= 0:
				if not game.cells[x-1][y].visited: neighbors.append('l')
			if y + 1 <= game.NUM_SQUARES - 1:
				if not game.cells[x][y+1].visited: neighbors.append('d')
			if y - 1 >= 0:
				if not game.cells[x][y-1].visited: neighbors.append('u')
 	
			if neighbors:
				history.append((x,y))
				direction = random.choice(neighbors)
				
				if  direction == 'r':
					game.cells[x+1][y].left = False
					game.cells[x][y].right = False
					x = x + 1
				if direction == 'l':
					game.cells[x-1][y].right = False
					game.cells[x][y].left = False
					x = x - 1
				if  direction == 'd':
					game.cells[x][y+1].top = False
					game.cells[x][y].bot = False
					y = y + 1
				if direction == 'u':
					game.cells[x][y-1].bot = False
					game.cells[x][y].top = False
					y = y - 1
			else:
				x,y = history.pop()
		return game.cells

class Solver:
	pass
			
class Game:

	def __init__(self):
	
		self.WINDOW_WIDTH = 1000
		self.WINDOW_HEIGHT = 1000
		self.NUM_SQUARES = 200
		self.BLOCK_SIZE = (self.WINDOW_WIDTH - 20) / self.NUM_SQUARES
		self.WHITE  = (255,255,255)
		self.BLACK = (0,0,0)
		self.GREEN = (0,255,0)
		self.cells = [[Cell(i,j) for j in range(self.NUM_SQUARES)] for i in range(self.NUM_SQUARES)]

	def draw_board(self):
		for row in self.cells:
			for col in row:
				walls, active = col.get_walls(self)
				for i in range(len(walls)):
					if not active[i]:
						pygame.draw.line(self.window, self.BLACK, walls[i][0], walls[i][1])

		for row in self.cells:
			for col in row:
				walls, active = col.get_walls(self)
				for i in range(len(walls)):
					if active[i]:
						pygame.draw.line(self.window, self.WHITE, walls[i][0], walls[i][1])


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
		self.gen = Generator()
		randx = random.randint(0, self.NUM_SQUARES - 1)
		randy = random.randint(0, self.NUM_SQUARES - 1)
		self.cells[0][0].top = False
		self.cells[self.NUM_SQUARES - 1][self.NUM_SQUARES - 1].bot = False
		self.cells = self.gen.dfs(self, randx,randy)
		self.getNextFrame()
		while running:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					running = False

		pygame.quit()

g = Game()
g.run()