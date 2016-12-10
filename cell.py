import pygame

class Cell:

	def __init__(self,x,y):
		self.x = x
		self.y = y
		self.top = True
		self.bot = True
		self.right = True
		self.left = True
		self.visited = False

	def get_walls(self, game):
		walls = []
		active = [self.top, self.bot, self.left, self.right]
		wall1 = [(self.x  * (game.BLOCK_SIZE), self.y * (game.BLOCK_SIZE)), (self.x  * (game.BLOCK_SIZE) + game.BLOCK_SIZE, self.y * (game.BLOCK_SIZE))]
		walls.append(wall1)

		wall3 = [(self.x  * (game.BLOCK_SIZE), self.y * (game.BLOCK_SIZE) + game.BLOCK_SIZE), (self.x  * (game.BLOCK_SIZE) + game.BLOCK_SIZE, self.y * (game.BLOCK_SIZE) + game.BLOCK_SIZE)]
		walls.append(wall3)

		wall2 = [(self.x  * (game.BLOCK_SIZE), self.y * (game.BLOCK_SIZE)), (self.x * (game.BLOCK_SIZE), self.y * (game.BLOCK_SIZE) + game.BLOCK_SIZE)]
		walls.append(wall2)

		wall4 = [(self.x  * (game.BLOCK_SIZE) + game.BLOCK_SIZE, self.y * (game.BLOCK_SIZE)), (self.x  * (game.BLOCK_SIZE) + game.BLOCK_SIZE, self.y * (game.BLOCK_SIZE) + game.BLOCK_SIZE)]
		walls.append(wall4)

		return walls, active
		