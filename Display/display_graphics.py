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
	def __init__(self, interface, width, height, other_display=None):
		super().__init__()
		self.width = width
		self.height = height
		self.fps = 30
		self.interface = interface
		self.error_catcher = ErrorCatcher()

		self.copy_from_other = False

		if not other_display is None:
			self.copy_from_other = True
			self.screen = other_display.screen
			self.clock = other_display.clock
	
	def start(self):

		if not self.copy_from_other:
			pygame.init()
			self.screen = pygame.display.set_mode((self.width, self.height))
			self.clock = pygame.time.Clock()


	def show_game(self, field, pocket):
		self.clock.tick(self.fps)
		
		self.screen.fill(WHITE)

		#draw interface
		self.interface.draw(self.screen)

		#draw road
		for rectangle in field.road.rectangles:
			pygame.draw.rect(self.screen, BLACK, rectangle.point_and_size())

		#draw pocket
		font = pygame.font.SysFont("comicsans", 20)
		text = font.render(f"Money: {pocket.get_money()}", True, BLACK)
		text_rect = text.get_rect(center=Coordinates(450, 15).tuple)
		self.screen.blit(text, text_rect)

		#draw health of the casle
		font = pygame.font.SysFont("comicsans", 20)
		text = font.render(f"Castle: {field.castle.health} HP", True, BLACK)
		text_rect = text.get_rect(center=Coordinates(450, 40).tuple)
		self.screen.blit(text, text_rect)

		current_path = os.path.abspath(os.getcwd())

		#draw units
		for unit in field.units:
			if not hasattr(unit, "loaded_image"):
				unit.loaded_image = pygame.image.load(os.path.join(current_path, "TowerDefence/Assets", type(unit).__name__ + ".png"))
				unit.loaded_image = pygame.transform.scale(unit.loaded_image, unit.shape)
				unit.loaded_image.set_colorkey(EMPTY)
			self.screen.blit(unit.loaded_image, (unit.coordinates.x - unit.shape[0] / 2, 
												 unit.coordinates.y - unit.shape[1] / 2))

		#draw tower
		for tower in field.towers:
			if not hasattr(tower, "loaded_image"):
				tower.loaded_image = pygame.image.load(os.path.join(current_path, "TowerDefence/Assets", type(tower).__name__ + ".png"))
				tower.loaded_image = pygame.transform.scale(tower.loaded_image, tower.shape)
				tower.loaded_image.set_colorkey(EMPTY)
			self.screen.blit(tower.loaded_image, (tower.coordinates.x - tower.shape[0] / 2, 
												  tower.coordinates.y - tower.shape[1] / 2))

		#draw castle
		if not hasattr(field.castle, "loaded_image"):
			field.castle.loaded_image = pygame.image.load(os.path.join(current_path, 
				"TowerDefence/Assets/Castle.png"))
			field.castle.loaded_image = pygame.transform.scale(field.castle.loaded_image, 
				(field.castle.width, field.castle.height))
			field.castle.loaded_image.set_colorkey(EMPTY)
		self.screen.blit(field.castle.loaded_image, (field.castle.coordinates.x, field.castle.coordinates.y))

		#draw attacks

		for positions in field.attacks_by_units:
			pygame.draw.line(self.screen, RED, positions[0].tuple, positions[1].tuple, 2)

		for positions in field.attacks_by_towers:
			pygame.draw.line(self.screen, GREEN, positions[0].tuple, positions[1].tuple, 2)			

		# search for errors
		if self.error_catcher.FieldError_count > 0:
			font = pygame.font.SysFont("comicsans", 16)
			text = font.render("YOU CAN NOT PLACE TOWER HERE", True, RED)
			text_rect = text.get_rect(center=Coordinates(350, 50).tuple)
			self.screen.blit(text, text_rect)
			self.error_catcher.search_for_errors(None)

		if self.error_catcher.MoneyError_count > 0:
			font = pygame.font.SysFont("comicsans", 16)
			text = font.render("YOU DO NOT HAVE ENOUGH MONEY", True, RED)
			text_rect = text.get_rect(center=Coordinates(350, 75).tuple)
			self.screen.blit(text, text_rect)
			self.error_catcher.search_for_errors(None)

		if self.error_catcher.CastleError_count > 0:
			lose_game_image = pygame.image.load(os.path.join(current_path, "TowerDefence/Assets/YouDied.png"))
			self.screen.blit(lose_game_image, (0, self.height / 3 * 2))
			self.error_catcher.search_for_errors(None)

		pygame.display.flip()


	def show_menu(self):
		self.clock.tick(self.fps)
		
		self.screen.fill(WHITE)

		#draw interface
		self.interface.draw(self.screen)

		pygame.display.flip()

	def finish(self):
		if not self.copy_from_other:
			pygame.quit()

