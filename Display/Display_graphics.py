import pygame
from Display import Display

class DisplayPygame(Display):
	def __init__(self):
		super().__init__()
		self.size = (512, 512)
	
	def start(self):
		pygame.init()
