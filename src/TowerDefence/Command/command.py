from abc import ABC, abstractmethod

class Command(ABC):
	@abstractmethod
	def __init__(self):
		pass

	@abstractmethod
	def __str__(self):
		pass
