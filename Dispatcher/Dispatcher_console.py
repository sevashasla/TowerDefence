from Dispatcher import Dispatcher

class DispatcherConsole(Dispatcher):
	def __init__(self):
		super().__init__()

	def start(self):
		print("I am ready to check your signals")


	def finish(self):
		pass

	def get_events(self) -> list:
		message = input()
		return [message]
		