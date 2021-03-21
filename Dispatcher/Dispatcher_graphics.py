from abc import ABC, abstractmethod
from Dispatcher import Dispatcher

import pygame
import sys

sys.path.insert(0, "/Game/")
from coordinates import Coordinates
from interface import Interface

class DispatcherGraphics(Dispatcher):
	def __init__(self):
		super().__init__()
		self.interface = Interface()
		self.button_with_pos = []

	def start(self):
		pass

	def finish(self):
		pygame.quit()


	def get_events(self) -> list:
		events = []
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				events.append(["stop"])

			elif event.type == pygame.MOUSEBUTTONUP:
				pos = pygame.mouse.get_pos()
				
				if(len(self.button_with_pos) == 1):
					self.button_with_pos.append(Coordinates(coordinates=pos))
					events.append(["place"] + self.button_with_pos)
					self.button_with_pos = []

				for button in self.interface.buttons:
					if(button.clicked(Coordinates(coordinates=pos))):
						if(len(self.button_with_pos) >= 1):
							print("here")
							self.button_with_pos.clear()
						self.button_with_pos.append(button.task)
	
		return events
