
import sys


class Grid:
	def __init__(self, cellGrid=dict()):
		self.cellGrid = cellGrid
	
	def render(self, start, rope):
		minX, maxX = -1, 10
		minY, maxY = -1, 10
		for y in range(maxY, minY, -1):
			for x in range(minX, maxX):
				if (x,y) == rope.head:
					cell = "H"
				elif (x,y) == rope.tail:
					cell = "T"
				elif (x,y) == start:
					cell = "s"
				else:
					cell = "#" if self.cellGrid.get((x,y)) else "."
				print(cell, end="")
			print("\n", end="")
	
	def __repr__(self):
		return f"Grid(cellGrid={self.cellGrid.__repr__()})"
	
	def __getitem__(self, xy):
		(xy := list(xy)).append(None)
		return self.cellGrid.get((xy[0], xy[1]), xy[2])
	
	def __setitem__(self, xy, value):
		self.cellGrid[xy] = value
	
	def __len__(self):
		return len(self.cellGrid)

class Rope:
	def __init__(self, head, tail):
		self.head = head
		self.tail = tail
	
	def __repr__(self):
		return f"Rope(head={self.head}, tail={self.tail})"
	
	def move(self, direction, grid):
		self.head = list(self.head)
		if direction == "R":
			self.head[0] += 1
		elif direction == "U":
			self.head[1] += 1
		elif direction == "L":
			self.head[0] -= 1	
		elif direction == "D":
			self.head[1] -= 1
		self.head = tuple(self.head)
	
	def update(self, grid):
		xDiff, yDiff = self.head[0]-self.tail[0], self.head[1]-self.tail[1]
		self.tail = list(self.tail)
		if xDiff > 1:
			self.tail[0] += 1
		elif xDiff < -1:
			self.tail[0] -= 1
		elif yDiff > 1:
			self.tail[1] += 1
		elif yDiff < -1:
			self.tail[1] -= 1
		
		if yDiff > 1 and (xDiff == 1 or xDiff == -1):
			self.tail[0] += xDiff
		elif yDiff < -1 and (xDiff == 1 or xDiff == -1):
			self.tail[0] += xDiff
		elif xDiff > 1 and (yDiff == 1 or yDiff == -1):
			self.tail[1] += yDiff
		elif xDiff < -1 and (yDiff == 1 or yDiff == -1):
			self.tail[1] += yDiff
		self.tail = tuple(self.tail)

	def __len__(self):
		return max(self.head[0]-self.tail[0], self.head[1]-self.tail[1])


def main():
	# read data file
	inputFile = sys.argv[1] if len(sys.argv) >= 2 else "example.txt"
	movements = []
	with open(inputFile, "r") as fobj:
		lines = fobj.readlines()
		
		for line in lines:
			line = line.strip().split(" ")
			movements.extend([ line[0] for _ in range(int(line[1])) ])
	
	start = (0,0)
	grid = Grid({start: True})
	rope = Rope(start, start)
	
	# do movement
	for direction in movements:
		rope.move(direction, grid)
		rope.update(grid)
		grid[rope.tail] = True

		grid.render(start, rope)
		print(direction, rope, grid, sep="\n")
		input()
	
	grid.render(start, rope)
	
	# results
	print("Part 1:", len(grid))


if __name__ == "__main__":
	main()
