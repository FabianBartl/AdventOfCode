
import sys


class Grid:
	def __init__(self, cellGrid=dict()):
		self.cellGrid = cellGrid
	
	def render(self):
		raise NotImplementedError
	
	def __repr__(self):
		return self.cellGrid.__repr__()
	
	def __getitem__(self, xy):
		(xy := list(xy)).append(None)
		return self.cellGrid.get((xy[0], xy[1]), xy[2])

class Cell:
	def __init__(self, visited=False):
		self.visited = visited
	
	def render(self):
		return "#" if self.visited else "_"
	
	def __repr__(self):
		return f"Cell(visited={self.visited})"
	
	def __bool__(self):
		return self.visited

class Rope:
	def __init__(self, x, y, *, head=None, tail=None):
		self.x = x
		self.y = y
		self.head = head
		self.tail = tail
	
	def __repr__(self):
		return f"Rope(x={self.x}, y={self.y}, head={self.head}, tail={self.tail})"

	def isFirst(self):
		return self.head is None

	def isLast(self):
		return self.tail is None
	
	def __len__(self):
		raise NotImplementedError


def main():
	grid = Grid()

	head = Rope(0,0)
	tail = Rope(0,0, head=head)
	head.tail = tail

	# read data file
	inputFile = sys.argv[1] if len(sys.argv) >= 2 else "example.txt"
	moves = []
	with open(inputFile, "r") as fobj:
		lines = fobj.readlines()
		
		for line in lines:
			line = line.strip().split(" ")
			moves.extend([ line[0] for _ in range(int(line[1])) ])
	
	# do movement
	for move in moves:
		pass
	
	# result
	print("Part 1:")


if __name__ == "__main__":
	main()
