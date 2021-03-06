import pygame
import sys
import os

from .display import Display
from ..Game.coordinates import Coordinates
from ..Game.interface import Interface
from ..Game.errors import *
from .error_catcher_graphics import ErrorCatcherGraphics

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
EMPTY = (255, 0, 255)
FONT = "comicsans"
UPPER = 2
HEALTH_WIDTH = 2


def get_assets_path(game_path, element=None):
	if element is None:
		return os.path.join(game_path, "Assets")
	else:
		return os.path.join(game_path, "Assets", get_name(element) + ".png")

def get_text_paths(game_path, text_name=None):
	if text_name is None:
		return os.path.join(game_path, "Data")
	else:
		return os.path.join(game_path, "Data", text_name)	


def get_name(variable_to_find_name):
	return type(variable_to_find_name).__name__


def get_health_color(unit):
	normalized_health = unit.health / unit.max_health
	if normalized_health < 0.0:
		return RED

	green = min(255, round(255 * 2 * normalized_health))
	red = min(255, 255 * 2 - round(255 * 2 * normalized_health))
	return (red, green, 0)


class DisplayGraphics(Display):
	def __init__(self, interface, width, height, game_path, other_display=None):
		super().__init__()
		self.interface = interface
		self.width = width
		self.height = height
		self.fps = 30
		self.game_path = game_path
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


	def show_game(self, field, pocket, error_catcher):
		self.clock.tick(self.fps)
		self.screen.fill(WHITE)

		#draw interface
		self.interface.draw(self.screen)

		#draw road
		for rectangle in field.road.rectangles:
			pygame.draw.rect(self.screen, BLACK, rectangle.point_and_size())

		#draw pocket
		font = pygame.font.SysFont(FONT, 20)
		text = font.render(f"Money: {pocket.get_money()}", True, BLACK)
		text_rect = text.get_rect(center=Coordinates(450, 15).tuple)
		self.screen.blit(text, text_rect)

		#draw health of the casle, 20)
		text = font.render(f"Castle: {field.castle.get_health()} HP", True, BLACK)
		text_rect = text.get_rect(center=Coordinates(450, 40).tuple)
		self.screen.blit(text, text_rect)

		#draw units
		for unit in field.units:
			if not hasattr(type(unit), "loaded_image"):
				type(unit).loaded_image = pygame.image.load(get_assets_path(self.game_path, unit))
				type(unit).loaded_image = pygame.transform.scale(type(unit).loaded_image, unit.shape)
				type(unit).loaded_image.set_colorkey(EMPTY)
			
			self.screen.blit(unit.loaded_image, (unit.coordinates.x - unit.shape[0] / 2, 
												 unit.coordinates.y - unit.shape[1] / 2))

		#draw tower
		for tower in field.towers:
			if not hasattr(type(tower), "loaded_image"):
				type(tower).loaded_image = pygame.image.load(get_assets_path(self.game_path, tower))
				type(tower).loaded_image = pygame.transform.scale(type(tower).loaded_image, type(tower).shape)
				type(tower).loaded_image.set_colorkey(EMPTY)

			pygame.draw.rect(self.screen, get_health_color(tower), (tower.coordinates.x - tower.shape[0] / 2 + UPPER, 
																	tower.coordinates.y - tower.shape[1] / 2 - UPPER, 
																	tower.shape[0],
																	HEALTH_WIDTH))
			self.screen.blit(tower.loaded_image, (tower.coordinates.x - tower.shape[0] / 2, 
												  tower.coordinates.y - tower.shape[1] / 2))

		#draw castle
		if not hasattr(field.castle, "loaded_image"):
			field.castle.loaded_image = pygame.image.load(get_assets_path(self.game_path, field.castle))
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
		if error_catcher.FieldError_count > 0:
			font = pygame.font.SysFont(FONT, 16)
			text = font.render("YOU CAN NOT PLACE TOWER HERE", True, RED)
			text_rect = text.get_rect(center=Coordinates(350, 50).tuple)
			self.screen.blit(text, text_rect)
			error_catcher.search_for_errors(None)

		if error_catcher.MoneyError_count > 0:
			font = pygame.font.SysFont(FONT, 16)
			text = font.render("YOU DO NOT HAVE ENOUGH MONEY", True, RED)
			text_rect = text.get_rect(center=Coordinates(350, 75).tuple)
			self.screen.blit(text, text_rect)
			error_catcher.search_for_errors(None)

		if error_catcher.CastleError_count > 0:
			lose_game_image = pygame.image.load(os.path.join(get_assets_path(self.game_path) + "/YouDied.png"))
			self.screen.blit(lose_game_image, (0, self.height / 3 * 2))
			error_catcher.search_for_errors(None)

		if error_catcher.WinError_count > 0:
			win_game_image = pygame.image.load(os.path.join(get_assets_path(self.game_path) + "/EpicWin.png"))
			win_game_image = pygame.transform.scale(win_game_image, (self.width, self.height // 3))
			self.screen.blit(win_game_image, (0, 511))
			error_catcher.search_for_errors(None)

		pygame.display.flip()


	def show_menu(self):
		self.clock.tick(self.fps)
		self.screen.fill(WHITE)
		#draw interface
		self.interface.draw(self.screen)

		for cell in self.interface.text:

			# print(cell["text_path"], get_name(cell["text_path"]))
			with open(get_text_paths(self.game_path, cell["text_path"]), 'r') as cell_file:
				lines = cell_file.read().splitlines()
			

			for number, line in enumerate(lines):

				number_of_tabs = line.count('\t')
				line = line.strip('\t')

				font = pygame.font.SysFont(FONT, 18)
				text = font.render(line, True, BLACK)

				text_rect = text.get_rect(topleft=Coordinates(cell["coordinates"][0] + 18 * number_of_tabs,
															 cell["coordinates"][1] + 15 * number).tuple)

				self.screen.blit(text, text_rect)
		

		pygame.display.flip()

	def finish(self):
		if not self.copy_from_other:
			pygame.quit()
