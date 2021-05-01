import fcntl
import sys
import os

from .dispatcher import Dispatcher
from ..Game.coordinates import Coordinates

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
		events = []
		try:
			for event in sys.stdin.read().split('\n')[:-1]:
				event = event.split(' ')
				if(event[0] == "place"):
					pos = [int(event[2]), int(event[3])]
					event[2] = Coordinates(coordinates=pos)
				events.append(event)
		except TypeError:
			pass
		return events