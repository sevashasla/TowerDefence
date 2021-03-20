import pygame
from Display import Display
import os

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
		self.fps = 30
	
	def start(self):
		pygame.init()
		self.screen = pygame.display.set_mode((self.width, self.height))
		self.clock = pygame.time.Clock()

	def show(self, field):
		self.clock.tick(self.fps)
		
		self.screen.fill(WHITE)
		
		#draw road
		# pygame.draw.polygon(self.screen, BLACK, field.road.edges)

		current_path = os.path.abspath(os.getcwd())

		#draw units
		for unit in field.units:
			if not hasattr(unit, "loaded_image"):
				unit.loaded_image = pygame.image.load(os.path.join(current_path, "../Unit", unit.image_name)).convert() #change?
				unit.loaded_image = pygame.transform.scale(unit.loaded_image, (20, 20))
			self.screen.blit(unit.loaded_image, (unit.coordinates.x, unit.coordinates.y))

		#draw tower
		for tower in field.towers:
			if not hasattr(tower, "loaded_image"):
				tower.loaded_image = pygame.image.load(os.path.join(current_path, "../Tower", tower.image_name)).convert() #change?
				tower.loaded_image = pygame.transform.scale(tower.loaded_image, (20, 20))
			self.screen.blit(tower.loaded_image, (tower.coordinates.x, tower.coordinates.y))



		pygame.display.flip()


	def finish(self):
		pygame.quit()

