import pygame
from Display import Display

class DisplayGraphics(Display):
	def __init__(self):
		super().__init__()
		self.size = (512, 512)
	
	def start(self):
		pygame.init()
		self.screen = pygame.display.set_mode(self.size)

	def run(self):
		running = True
		while running:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					running = False

	def show(self, items):
		pass

	
