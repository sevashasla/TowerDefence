from abc import ABC, abstractmethod
from Dispatcher import Dispatcher
import pygame

class DispatcherGraphics(Dispatcher):
	def __init__(self):
		super().__init__()

	def start(self):
		pass

	def finish(self):
		pygame.quit()

	def get_events(self) -> list:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
					return ["stop"] #stop
		return ["continue"]
