import pygame
from .coordinates import Coordinates

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
		if ((self.center.x - self.width // 2 <= pos.x <= self.center.x + self.width // 2) and 
			(self.center.y - self.height // 2 <= pos.y <= self.center.y + self.height // 2)):
			return True
		return False

	def draw(self, screen):
		if not hasattr(self, "rect"):
			self.rect = pygame.Rect((self.coordinates.x, self.coordinates.y, self.width, self.height))

		pygame.draw.rect(screen, self.color, self.rect)
		if(self.text != ""):
			font = pygame.font.SysFont("comicsans", self.text_size)
			text = font.render(self.text, True, self.text_color)
			text_rect = text.get_rect(center=self.rect.center)
			screen.blit(text, text_rect)
