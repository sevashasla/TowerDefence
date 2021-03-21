import pygame
import sys
import os

sys.path.insert(0, "./Game/")
from Display import Display
from coordinates import Coordinates
from interface import Interface

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


class DisplayGraphics(Display):
	def __init__(self, width, height):
		super().__init__()
		self.width = width
		self.height = height
		self.fps = 30
		self.interface = Interface()
	
	def start(self):
		pygame.init()
		self.screen = pygame.display.set_mode((self.width, self.height))
		self.clock = pygame.time.Clock()

	def show(self, field, pocket):
		self.clock.tick(self.fps)
		
		self.screen.fill(WHITE)

		#draw interface
		self.interface.draw(self.screen)


		
		#draw road
		pygame.draw.polygon(self.screen, BLACK, field.road.vertices)


		#draw pocket
		font = pygame.font.SysFont("comicsans", 20)
		text = font.render("Money: {}".format(pocket.getMoney()), True, BLACK)
		text_rect = text.get_rect(center=Coordinates(450, 15).to_tuple())
		self.screen.blit(text, text_rect)		

		current_path = os.path.abspath(os.getcwd())

		#draw units
		for unit in field.units:
			if not hasattr(unit, "loaded_image"):
				unit.loaded_image = pygame.image.load(os.path.join(current_path, "Unit", type(unit).__name__ + ".jpg")).convert() #change?
				unit.loaded_image = pygame.transform.scale(unit.loaded_image, (20, 20))
			self.screen.blit(unit.loaded_image, (unit.coordinates.x, unit.coordinates.y))

		#draw tower
		for tower in field.towers:
			if not hasattr(tower, "loaded_image"):
				tower.loaded_image = pygame.image.load(os.path.join(current_path, "Tower", type(tower).__name__ + ".jpg")).convert() #change?
				tower.loaded_image = pygame.transform.scale(tower.loaded_image, (30, 30))
			self.screen.blit(tower.loaded_image, (tower.coordinates.x, tower.coordinates.y))

		pygame.display.flip()


	def finish(self):
		pygame.quit()

