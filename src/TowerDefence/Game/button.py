import pygame
from .coordinates import Coordinates
import os
import sys


class Button():

	def __init__(self, data, game_path):
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
		self.game_path = game_path


	def clicked(self, pos) -> bool:
		if ((self.center.x - self.width // 2 <= pos.x <= self.center.x + self.width // 2) and 
			(self.center.y - self.height // 2 <= pos.y <= self.center.y + self.height // 2)):
			return True
		return False

	def draw(self, screen) -> None:
		if not hasattr(self, "rect"):	
			self.rect = pygame.Rect((self.coordinates.x, self.coordinates.y, self.width, self.height))
			self.image = pygame.image.load(os.path.join(self.game_path, "Assets/" + self.image_name))
			self.image = pygame.transform.scale(self.image, (self.width, self.height))

		screen.blit(self.image, self.coordinates.tuple)
		if(self.text != ""):
			font = pygame.font.SysFont("comicsans", self.text_size)
			text = font.render(self.text, True, self.text_color)
			text_rect = text.get_rect(center=self.rect.center)
			screen.blit(text, text_rect)
