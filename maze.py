class Maze:

	def __init__(self, cols_count, rows_count):
		self.maze = [[0 for x in range(cols_count)] for x in range(rows_count)]

	def generate(self):
		pass

	def getMaze(self):
		return self.maze