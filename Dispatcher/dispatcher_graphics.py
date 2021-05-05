from .dispatcher import Dispatcher

import pygame
import sys

from ..Game.coordinates import Coordinates
from ..Game.interface import Interface

from ..Command.stop import StopCommand
from ..Command.place_tower import PlaceTowerCommand


class DispatcherGraphics(Dispatcher):
	def __init__(self, interface):
		super().__init__()
		self.interface = interface
		self.last_chosen_type_of_tower = None

	def start(self):
		pass

	def finish(self):
		pygame.quit()


	def get_events(self) -> list:
		events = []
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				events.append(StopCommand())
				break

			elif event.type == pygame.MOUSEBUTTONUP:
				pos = pygame.mouse.get_pos()
				print(pos)
				coordinates_of_click = Coordinates(coordinates=pos)	
				clicked = False

				for button in self.interface.buttons:
					if button.clicked(coordinates_of_click):
						if button.task.endswith("Tower"):
							self.last_chosen_type_of_tower = button.task
						clicked = True
						break

				if not clicked and not self.last_chosen_type_of_tower is None:
					events.append(PlaceTowerCommand(self.last_chosen_type_of_tower, 
						coordinates_of_click))
		return events
