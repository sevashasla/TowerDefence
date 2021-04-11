import pygame
from .coordinates import Coordinates
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> add files to checkpoint 2
import os
import sys


class Button():

	def __init__(self, data):
		self.color = tuple(data["color"])
		self.task = data["task"]
		self.coordinates = Coordinates(coordinates=data["coordinates"])
		self.width = data["width"]
		self.height = data["height"]
		self.text = data["text"]
		self.text_size = data["text_size"]
		self.text_color = tuple(data["text_color"])
		self.center = Coordinates(self.coordinates.x + self.width // 2, self.coordinates.y + self.height // 2)
		self.image_name = data["image"]


	def clicked(self, pos) -> bool:
<<<<<<< HEAD
=======

class Button():
	def __init__(self, task, color, coordinates, width, height, text="", text_color=None, text_size=None):
		self.color = color
		self.task = task
		
		self.coordinates = coordinates

		self.width = width
		self.height = height
		self.text = text
		self.text_color = text_color
		self.text_size = text_size

		self.center = Coordinates(self.coordinates.x + self.width // 2, self.coordinates.y + self.height // 2)


	def clicked(self, pos):
>>>>>>> delete it later
=======
>>>>>>> add files to checkpoint 2
		if ((self.center.x - self.width // 2 <= pos.x <= self.center.x + self.width // 2) and 
			(self.center.y - self.height // 2 <= pos.y <= self.center.y + self.height // 2)):
			return True
		return False

<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> add files to checkpoint 2
	def draw(self, screen) -> None:
		if not hasattr(self, "rect"):	
			self.rect = pygame.Rect((self.coordinates.x, self.coordinates.y, self.width, self.height))
			current_path = os.path.abspath(os.getcwd())
			self.image = pygame.image.load(os.path.join(current_path, "TowerDefence/Assets/" + self.image_name))
			self.image = pygame.transform.scale(self.image, (self.width, self.height))

		screen.blit(self.image, self.coordinates.to_tuple())
<<<<<<< HEAD
=======
	def draw(self, screen):
		if not hasattr(self, "rect"):
			self.rect = pygame.Rect((self.coordinates.x, self.coordinates.y, self.width, self.height))

		pygame.draw.rect(screen, self.color, self.rect)
>>>>>>> delete it later
=======
>>>>>>> add files to checkpoint 2
		if(self.text != ""):
			font = pygame.font.SysFont("comicsans", self.text_size)
			text = font.render(self.text, True, self.text_color)
			text_rect = text.get_rect(center=self.rect.center)
			screen.blit(text, text_rect)
