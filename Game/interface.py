import pygame
from .button import Button
from .coordinates import Coordinates

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

class Interface:
	# def __init__(self, color, coordinates, width, height):
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> add files to checkpoint 2
	def __init__(self, screen_width, screen_height, interface_data, buttons_data):

		self.color = tuple(interface_data["color"])
		self.coordinates = Coordinates(screen_height, 0)
		self.width = interface_data["width"]
		self.height = interface_data["height"]

		self.buttons = []
		for button in buttons_data:
			self.buttons.append(Button(button))

<<<<<<< HEAD
=======
	def __init__(self, screen_width, screen_height, width, height):

		self.color = BLUE
		self.coordinates = Coordinates(screen_height, 0)
		self.width = width
		self.height = height

		self.buttons = [Button("WeakTower", GREEN, Coordinates(128, 512 + 128 + 64), 128, 64, "weak tower", BLACK, 25), 
						Button("AverageTower", RED, Coordinates(256 + 128, 512 + 128 + 64), 128, 64, "average tower", BLACK, 25)]

		# self.image_name = 
>>>>>>> delete it later
=======
>>>>>>> add files to checkpoint 2

	def draw(self, screen):

		if not hasattr(self, "rect"):
			self.rect = pygame.Rect(self.coordinates.x, self.coordinates.y, self.width, self.height)

		pygame.draw.rect(screen, self.color, self.rect)
		for button in self.buttons:
			button.draw(screen)

