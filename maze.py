import pygame
import random
import math
import numpy
from cell import Cell

class Generator:

	def __init__(self):
		pass

	def dfs(self, game,x,y):
		game.getNextFrame()
		if game.cells[x][y].visited: return game.cells
		game.cells[x][y].visited = True
		
		num_neighbors = 4

		while num_neighbors != 0:
		
			r = random.randint(0,3)
			
			if  r == 0:
				if x + 1 <= game.NUM_SQUARES - 1:
					if not game.cells[x+1][y].visited:
						game.cells[x+1][y].left = False
						game.cells[x][y].right = False
						game.cells = self.dfs(game, x + 1, y)
			if  r == 1:
				if x - 1 >= 0:
					if not game.cells[x-1][y].visited:
						game.cells[x-1][y].right = False
						game.cells[x][y].left = False
						game.cells = self.dfs(game, x - 1, y)
			if  r == 2:
				if y + 1 <= game.NUM_SQUARES - 1:
					if not game.cells[x][y+1].visited:
						game.cells[x][y+1].top = False
						game.cells[x][y].bot = False
						game.cells = self.dfs(game, x, y+1)
			if  r == 3:
				if y - 1 >= 0:
					if not game.cells[x][y-1].visited:
						game.cells[x][y-1].bot = False
						game.cells[x][y].top = False
						game.cells = self.dfs(game, x, y-1)
				
			num_neighbors = 0
			if x + 1 <= game.NUM_SQUARES - 1:
				if not game.cells[x+1][y].visited: num_neighbors += 1
			if x - 1 >= 0:
				if not game.cells[x-1][y].visited: num_neighbors += 1
			if y + 1 <= game.NUM_SQUARES - 1:
				if not game.cells[x][y+1].visited: num_neighbors += 1
			if y - 1 >= 0:
				if not game.cells[x][y-1].visited: num_neighbors += 1
		return game.cells
			
class Game:

	def __init__(self):
	
		self.WINDOW_WIDTH = 800
		self.WINDOW_HEIGHT = 800
		self.NUM_SQUARES = 30
		self.BLOCK_SIZE = (self.WINDOW_WIDTH - 5) / self.NUM_SQUARES
		self.WHITE  = (255,255,255)
		self.BLACK = (0,0,0)
		self.cells = [[Cell(i,j) for j in range(self.NUM_SQUARES)] for i in range(self.NUM_SQUARES)]

	def draw_board(self):
		for row in self.cells:
			for col in row:
				walls, active = col.get_walls(self)
				for i in range(len(walls)):
					if active[i]:
						pygame.draw.line(self.window, self.WHITE, walls[i][0], walls[i][1])
					else:
						pygame.draw.line(self.window, self.BLACK, walls[i][0], walls[i][1])


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
		self.cells[0][0].top = False
		self.cells[self.NUM_SQUARES - 1][self.NUM_SQUARES - 1].bot = False

		self.cells = self.gen.dfs(self, 0,0)
		while running:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					running = False

		pygame.quit()

g = Game()
g.run()