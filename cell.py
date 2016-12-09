import pygame

class Cell:

	def __init__(self,x,y):
		self.x = x
		self.y = y

	def get_walls(self, game):
		wall1 = [(self.x  * (game.BLOCK_SIZE), self.y * (game.BLOCK_SIZE)), (self.x  * (game.BLOCK_SIZE) + game.BLOCK_SIZE, self.y * (game.BLOCK_SIZE))]
		wall2 = [(self.x  * (game.BLOCK_SIZE), self.y * (game.BLOCK_SIZE)), (self.x * (game.BLOCK_SIZE), self.y * (game.BLOCK_SIZE) + game.BLOCK_SIZE)]
		wall3 = [(self.x  * (game.BLOCK_SIZE), self.y * (game.BLOCK_SIZE) + game.BLOCK_SIZE), (self.x  * (game.BLOCK_SIZE) + game.BLOCK_SIZE, self.y * (game.BLOCK_SIZE) + game.BLOCK_SIZE)]
		wall4 = [(self.x  * (game.BLOCK_SIZE) + game.BLOCK_SIZE, self.y * (game.BLOCK_SIZE)), (self.x  * (game.BLOCK_SIZE) + game.BLOCK_SIZE, self.y * (game.BLOCK_SIZE) + game.BLOCK_SIZE)]

		return wall1,wall2,wall3,wall4
		