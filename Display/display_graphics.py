import pygame
import sys
import os

from .display import Display
from ..Game.coordinates import Coordinates
from ..Game.interface import Interface
from ..Game.errors import ErrorCatcher

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
EMPTY = (255, 0, 255)


class DisplayGraphics(Display):
	def __init__(self, interface, width, height):
		super().__init__()
		self.width = width
		self.height = height
		self.fps = 30
		self.interface = interface
		self.error_catcher = ErrorCatcher()
	
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
		for rectangle in field.road.rectangles:
			pygame.draw.rect(self.screen, BLACK, rectangle.point_and_size())

		#draw pocket
		font = pygame.font.SysFont("comicsans", 20)
		text = font.render("Money: {}".format(pocket.get_money()), True, BLACK)
		text_rect = text.get_rect(center=Coordinates(450, 15).to_tuple()) #STRANGE?
		self.screen.blit(text, text_rect)

		current_path = os.path.abspath(os.getcwd())

		#draw units
		for unit in field.units:
			if not hasattr(unit, "loaded_image"):
				unit.loaded_image = pygame.image.load(os.path.join(current_path, "TowerDefence/Assets", type(unit).__name__ + ".png"))
				unit.loaded_image = pygame.transform.scale(unit.loaded_image, unit.shape)
				unit.loaded_image.set_colorkey(EMPTY)
			self.screen.blit(unit.loaded_image, (unit.coordinates.x, unit.coordinates.y))

		#draw tower
		for tower in field.towers:
			if not hasattr(tower, "loaded_image"):
				tower.loaded_image = pygame.image.load(os.path.join(current_path, "TowerDefence/Assets", type(tower).__name__ + ".png"))
				tower.loaded_image = pygame.transform.scale(tower.loaded_image, tower.shape)
				tower.loaded_image.set_colorkey(EMPTY)
			self.screen.blit(tower.loaded_image, (tower.coordinates.x, tower.coordinates.y))

		#draw castle
		if not hasattr(field.castle, "loaded_image"):
			field.castle.loaded_image = pygame.image.load(os.path.join(current_path, 
				"TowerDefence/Assets/Castle.png"))
			field.castle.loaded_image = pygame.transform.scale(field.castle.loaded_image, 
				(field.castle.width, field.castle.height))
			field.castle.loaded_image.set_colorkey(EMPTY)
		self.screen.blit(field.castle.loaded_image, (field.castle.coordinates.x, field.castle.coordinates.y))

		if self.has_FieldError:
				font = pygame.font.SysFont("comicsans", 16)
				text = font.render("YOU CAN NOT PLACE TOWER HERE", True, RED)
				text_rect = text.get_rect(center=Coordinates(350, 50).to_tuple())
				self.screen.blit(text, text_rect)
				self.has_FieldError = False

		if self.error_catcher.MoneyError_count > 0:
			font = pygame.font.SysFont("comicsans", 16)
			text = font.render("YOU DO NOT HAVE ENOUGH MONEY", True, RED)
			text_rect = text.get_rect(center=Coordinates(350, 75).to_tuple())
			self.screen.blit(text, text_rect)
			self.error_catcher.search_for_errors(None)

		pygame.display.flip()



	def finish(self):
		pygame.quit()

