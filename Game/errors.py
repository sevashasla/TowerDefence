from abc import ABC, abstractmethod

class MoneyError(Exception):
    pass


class FieldError(Exception):
	pass


class CastleError(Exception):
	pass



class ErrorCatcher:

	@abstractmethod
	def __init__(self):
		pass

	@abstractmethod
	def search_for_errors(self, error):
		pass

	@abstractmethod
	def reset(self):
		pass