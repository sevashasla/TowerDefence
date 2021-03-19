from abc import ABC, abstractmethod

class Dispatcher(ABC):
	@abstractmethod
	def __init__(self):
		pass
	
	@abstractmethod
	def start(self):
		pass

	@abstractmethod
	def finish(self):
		pass

	@abstractmethod
	def get_events(self) -> list:
		pass
