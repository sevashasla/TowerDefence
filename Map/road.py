from ..Game.rectangle import Rectangle

class FieldError(Exception):
	pass

class Road: 
	def __init__(self, width, height, rectangles):
		self.width = width
		self.height = height
		self.rectangles = [Rectangle(rectangle) for rectangle in rectangles]


	def belongs_to_rectangle(self, rectangle, coordinates) -> bool:
		return (rectangle.x1 <= coordinates.x <= rectangle.x2) and (rectangle.y1 <= coordinates.y <= rectangle.y2)

	def belongs_to_road(self, coordinates) -> bool:
		if coordinates.x < 0 or coordinates.x >= self.width or coordinates.y < 0 or coordinates.y >= self.height:
			return False
		for rectangle in self.rectangles:
			if self.belongs_to_rectangle(rectangle, coordinates):
				return True
