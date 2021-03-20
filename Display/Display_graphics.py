import pygame
from Display import Display


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


class DisplayGraphics(Display):
	def __init__(self):
		super().__init__()
		self.width = 512
		self.height = 512
	
	def start(self):
		pygame.init()
		self.screen = pygame.display.set_mode((self.width, self.height))

	def show(self, items):
		self.screen.fill(WHITE)
		for item in items:
			item.draw()
		pygame.display.flip()

	def finish(self):
		pygame.quit()

