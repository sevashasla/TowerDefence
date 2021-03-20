class FieldError(Exception):
	pass


class Road: 

	def __init__(self, x_size, y_size):
		self.pixels = []
		self.x_size = x_size
		self.y_size = y_size
		for i in range(self.y_size):
			self.pixels.append([False] * self.x_size)
		for y in range(0, y_size * 8 // 20):
			for x in range(x_size * 9 // 20, x_size * 11 // 20):
				self.pixels[x][y] = True
		for y in range(y_size * 6 // 20, y_size * 8 // 20):
			for x in range(x_size * 11 // 20, x_size * 17 // 20):
				self.pixels[x][y] = True	
		for y in range(y_size * 8 // 20, y_size * 12 // 20):
			for x in range(x_size * 15 // 20, x_size * 17 // 20):
				self.pixels[x][y] = True
		for y in range(y_size * 10 // 20, y_size * 12 // 20):
			for x in range(x_size * 3 // 20, x_size * 15 // 20):
				self.pixels[x][y] = True
		for y in range(y_size * 12 // 20, y_size * 16 // 20):
			for x in range(x_size * 5 // 20, x_size * 9 // 20):
				self.pixels[x][y] = True
		for y in range(y_size * 16 // 20, y_size):
			for x in range(x_size * 9 // 20, x_size * 11 // 20):
				self.pixels[x][y] = True
				
		self.vertices = []
		self.vertices.append((x_size * 9 // 20, 0))
		self.vertices.append((x_size * 11 // 20, 0))
		self.vertices.append((x_size * 9 // 20, y_size * 8 // 20))
		self.vertices.append((x_size * 11 // 20, y_size * 6 // 20))
		self.vertices.append((x_size * 17 // 20, y_size * 6 // 20))
		self.vertices.append((x_size * 15 // 20, y_size * 8 // 20))
		self.vertices.append((x_size * 11 // 20, y_size * 10 // 20))
		self.vertices.append((x_size * 17 // 20, y_size * 12 // 20))
		self.vertices.append((x_size * 3 // 20, y_size * 10 // 20))
		self.vertices.append((x_size * 5 // 20, y_size * 12 // 20))
		self.vertices.append((x_size * 3 // 20, y_size * 16 // 20))
		self.vertices.append((x_size * 5 // 20, y_size * 14 // 20))
		self.vertices.append((x_size * 11 // 20, y_size * 14 // 20))
		self.vertices.append((x_size * 9 // 20, y_size * 16 // 20))
		self.vertices.append((x_size * 9 // 20, y_size - 1))
		self.vertices.append((x_size * 11 // 20, y_size - 1))


	def belongs_to_road(self, coordinates):
		if coordinates[0] < 0 or coordinates[0] >= self.x_size or coordinates[1] < 0 or coordinates[1] >= self.y_size:
			raise FieldError
		return self.pixels[coordinates[0]][coordinates[1]] 

