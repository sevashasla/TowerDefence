from dataclasses import dataclass
import functools

@dataclass
class Rectangle:

	x1: int
	y1: int
	x2: int
	y2: int

	def __init__(self, coordinates):
		self.x1 = min(coordinates['x1'], coordinates['x2'])
		self.y1 = min(coordinates['y1'], coordinates['y2']) 
		self.x2 = max(coordinates['x1'], coordinates['x2']) 
		self.y2 = max(coordinates['y1'], coordinates['y2'])

	@property
	def tuple(self):
		return (self.x1, self.y1, self.x2, self.y2)
	
	def width(self):
		return abs(self.x2 - self.x1)

	def height(self):
		return abs(self.y2 - self.y1)

	def point_and_size(self): 
		return (self.x1, self.y1, self.width(), self.height())