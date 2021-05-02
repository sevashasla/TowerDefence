from ..Game.errors import *


class ErrorCatcherGraphics(ErrorCatcher):

	def __init__(self):
		self.has_FieldError = False
		self.has_MoneyError = False
		self.has_CastleError = False
		self.FieldError_count = 0
		self.MoneyError_count = 0
		self.CastleError_count = 0


	def search_for_errors(self, error):
		if error == 'FieldError':
			self.has_FieldError = True
			self.FieldError_count = 30
		if error == 'MoneyError':
			self.has_MoneyError = True
			self.MoneyError_count = 30
		if error == 'CastleError':
			self.has_CastleError = True
			self.CastleError_count = 30
		if error is None:
			self.FieldError_count = max(self.FieldError_count - 1, 0)
			self.MoneyError_count = max(self.MoneyError_count - 1, 0)
			self.CastleError_count = max(self.CastleError_count - 1, 0)


	def reset(self):
		self.has_FieldError = False
		self.has_MoneyError = False
		self.has_CastleError = False
		self.FieldError_count = 0
		self.MoneyError_count = 0
		self.CastleError_count = 0
