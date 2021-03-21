import pygame
from Button import Button
from coordinates import Coordinates

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

class Interface:
	# def __init__(self, color, coordinates, width, height):
	def __init__(self):

		self.color = BLUE
		self.coordinates = Coordinates(0, 512)
		self.width = 512
		self.height = 256

		self.buttons = [Button("WeakTower", GREEN, Coordinates(128, 512 + 128 + 64), 128, 64, "weak tower", BLACK, 25), 
						Button("AverageTower", RED, Coordinates(256 + 128, 512 + 128 + 64), 128, 64, "average tower", BLACK, 25)]

		# self.image_name = 

	def draw(self, screen):

		if not hasattr(self, "rect"):
			self.rect = pygame.Rect(self.coordinates.x, self.coordinates.y, self.width, self.height)

		pygame.draw.rect(screen, self.color, self.rect)
		for button in self.buttons:
			button.draw(screen)

