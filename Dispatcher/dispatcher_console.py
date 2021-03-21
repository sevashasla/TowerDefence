from dispatcher import Dispatcher
import fcntl
import sys
import os


class DispatcherConsole(Dispatcher):
	def __init__(self):
		super().__init__()

	def start(self):
		#make non-blocking stdin
		orig_fl = fcntl.fcntl(sys.stdin, fcntl.F_GETFL)
		fcntl.fcntl(sys.stdin, fcntl.F_SETFL, orig_fl | os.O_NONBLOCK)
		print("I am ready to check your signals")


	def finish(self):
		pass

	def get_events(self) -> list:
		try:
			events = [[i] for i in sys.stdin.read().split('\n')[:-1]]
		except TypeError:
			events = []
		return events
