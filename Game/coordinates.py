class Coordinates:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        # print('Point set at coordinates: x = {0}; y = {1};'.format(*[x, y]))

    def __str__(self):
    	return str(self.x) + ' ' + str(self.y)
