import pygame
import random
import math

BLOCK_SIZE = 40
NUM_SQUARES = 20
WHITE  = (255,255,255)
BLACK = (0,0,0)
WINDOW_WIDTH = (BLOCK_SIZE + 1) * NUM_SQUARES
WINDOW_HEIGHT = (BLOCK_SIZE + 1) * NUM_SQUARES

pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

def draw_board():
	for y in range(NUM_SQUARES):
		for x in range(NUM_SQUARES):
			rect = pygame.Rect(x * (BLOCK_SIZE + 1), y * (BLOCK_SIZE + 1), BLOCK_SIZE, BLOCK_SIZE)
			pygame.draw.rect(window, WHITE, rect)

class Game:

	def __init__(self):
		pass

	def getPresentFrame(self):
		pygame.event.pump()
		draw_board()
		#updates the window
		pygame.display.flip()
		

	def getNextFrame(self):
		pygame.event.pump()
		draw_board()
		#update the window
		pygame.display.flip()


score = 0
image = None
finish = False
g = Game()
g.getPresentFrame()
running = True
while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		else:
			g.getNextFrame()


pygame.quit()