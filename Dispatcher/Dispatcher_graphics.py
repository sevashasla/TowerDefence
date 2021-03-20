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
		events = []
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				events.append(["stop"])
			elif event.type == pygame.MOUSEBUTTONUP:
				pos = pygame.mouse.get_pos()
				events.append(["mouse_click", pos])
		return events