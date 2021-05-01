from dataclasses import dataclass

@dataclass
class Rectangle:
	x1: int
	y1: int
	x2: int
	y2: int

	def to_tuple(self):
		return (self.x1, self.y1, self.x2, self.y2)
	
	def width(self):
		return abs(self.x2 - self.x1)

	def height(self):
		return abs(self.y2 - self.y1)

	def point_and_size(self): 
		return (self.x1, self.y1, self.width(), self.height())
		

class Road: 
	def __init__(self, width, height, rectangles):
		self.width = width
		self.height = height
		self.rectangles = []
		for rectangle in rectangles:
			self.rectangles.append(Rectangle(min(rectangle["x1"], rectangle["x2"]), 
				min(rectangle["y1"], rectangle["y2"]), 
				max(rectangle["x1"], rectangle["x2"]), 
				max(rectangle["y1"], rectangle["y2"])))
			print((min(rectangle["x1"], rectangle["x2"]), 
				min(rectangle["y1"], rectangle["y2"]), 
				max(rectangle["x1"], rectangle["x2"]), 
				max(rectangle["y1"], rectangle["y2"])))

	def belong_to_rectangle(self, rectangle, coordinates) -> bool:
		return (rectangle.x1 <= coordinates.x <= rectangle.x2) and (rectangle.y1 <= coordinates.y <= rectangle.y2)

	def belongs_to_road(self, coordinates) -> bool:
		if coordinates.x < 0 or coordinates.x >= self.width or coordinates.y < 0 or coordinates.y >= self.height:
			# raise FieldError
			return False
		for rectangle in self.rectangles:
			if self.belong_to_rectangle(rectangle, coordinates):
				return True
