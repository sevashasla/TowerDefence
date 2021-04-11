import pygame


class Button():
	def __init__(self, color, coordinates, width, height, text=""):
		self.color = color
		
		self.coordinates = coordinates

		self.width = width
		self.height = height
		self.text = text
		# self.image = pygame.Surface((self.width, self.height))
		# self.image.fill(color)
		self.rect = pygame.Rect((self.coordinates.x, self.coordinates.y, self.width, self.height))
		print(self.rect.center)

	def clicked(self, pos):
		if ((self.rect.center[0] - self.width // 2 <= pos[0] <= self.rect.center[0] + self.width // 2) and 
			(self.rect.center[1] - self.height // 2 <= pos[1] <= self.rect.center[1] + self.height // 2)):
			return True
		return False

	def draw(self, screen):
		pygame.draw.rect(screen, self.color, self.rect)
