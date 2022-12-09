
import sys, time


class Grid:
	def __init__(self, cellGrid=dict()):
		self.cellGrid = cellGrid
	
	def render(self, start, rope, minXY=(-1,-2), maxXY=(6,5)):
		minX, minY = minXY
		maxX, maxY = maxXY
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
	def __init__(self, knots):
		self.knots = knots
		self.head = self.knots[0]
		self.tail = self.knots[-1]
	
	def __repr__(self):
		return f"Rope(knots={self.knots})"
	
	def updateHead(self):
		self.head = self.knots[0]
	
	def updateTail(self):
		self.tail = self.knots[-1]
	
	def move(self, direction, grid):
		head = list(self.knots[0])
		if direction == "R":
			head[0] += 1
		elif direction == "U":
			head[1] += 1
		elif direction == "L":
			head[0] -= 1	
		elif direction == "D":
			head[1] -= 1
		self.knots[0] = tuple(head)
		self.updateHead()
	
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
		self.updateTail()

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
	minXY, maxXY = (-20,-20), (20,20)
	grid = Grid({start: True})
	rope = Rope([start, start])
	
	# do movement
	for index, direction in enumerate(movements):
		rope.move(direction, grid)
		rope.update(grid)
		grid[rope.tail] = True

		print(f"{index} / {len(movements)-1}")
		grid.render(start, rope, minXY, maxXY)
		time.sleep(0.1)
		# print(direction, rope, grid, sep="\n")
		# input()
	
	grid.render(start, rope, minXY, maxXY)
	
	# results
	print("Part 1:", len(grid))


if __name__ == "__main__":
	main()
