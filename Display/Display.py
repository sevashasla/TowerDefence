from abc import ABC, abstractmethod

class Display():
	@abstractmethod
	def __init__(self):
		pass

	@abstractmethod
	def show(self):
		pass

	@abstractmethod
	def start(self):
		pass

	@abstractmethod
	def finish(self):
		pass
