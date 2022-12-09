
import sys, time


class Grid:
	def __init__(self, cellGrid=dict()):
		self.cellGrid = cellGrid
	
	def render(self, start, rope, size=(10,)*4):
		minX, minY = rope.head[0]-size[0], rope.head[1]-size[1]
		maxX, maxY = rope.head[0]+size[2], rope.head[1]+size[3]
		for y in range(maxY, minY, -1):
			for x in range(minX, maxX):
				cell = "#" if self.cellGrid.get((x,y)) else "."
				if (x,y) == start:
					cell = "s"
				if (x,y) == rope.tail:
					cell = "T"
				for index, knot in enumerate(rope[1:-1], 1):
					if (x,y) == knot:
						cell = str(index)
				if (x,y) == rope.head:
					cell = "H"
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
		for index, knot in enumerate(self.knots[1:], 1):
			subHead = self.knots[index-1]
			subTail = list(knot)
			xDiff, yDiff = subHead[0]-subTail[0], subHead[1]-subTail[1]
			if xDiff > 1:
				subTail[0] += 1
			elif xDiff < -1:
				subTail[0] -= 1
			elif yDiff > 1:
				subTail[1] += 1
			elif yDiff < -1:
				subTail[1] -= 1
			if yDiff > 1 and (xDiff == 1 or xDiff == -1):
				subTail[0] += xDiff
			elif yDiff < -1 and (xDiff == 1 or xDiff == -1):
				subTail[0] += xDiff
			elif xDiff > 1 and (yDiff == 1 or yDiff == -1):
				subTail[1] += yDiff
			elif xDiff < -1 and (yDiff == 1 or yDiff == -1):
				subTail[1] += yDiff
			self.knots[index] = tuple(subTail)
		self.updateTail()

	def __len__(self):
		return max(self.head[0]-self.tail[0], self.head[1]-self.tail[1])

	def __iter__(self):
		return iter(self.knots)

	def __getitem__(self, knot):
		return self.knots[knot]

	def __setitem__(self, knot, value):
		self.knots[knot] = value
		self.updateHead()
		self.updateTail()


def main():
	# read data file
	inputFile = sys.argv[1] if len(sys.argv) >= 2 else "example.txt"
	movements = []
	with open(inputFile, "r") as fobj:
		lines = fobj.readlines()
		
		for line in lines:
			line = line.strip().split(" ")
			movements.extend([ line[0] for _ in range(int(line[1])) ])
	
	size = (int(sys.argv[2]),)*4 if len(sys.argv) >= 3 else (10,)*4
	start = (0,0)
	sleepTime = 0.000_1
	
	# Part 1:
	grid = Grid({start: True})
	rope = Rope([start] * 2)
	
	# do movement
	for index, direction in enumerate(movements):
		rope.move(direction, grid)
		rope.update(grid)
		grid[rope.tail] = True

		print(f"{index} / {len(movements)-1}")
		grid.render(start, rope, size)
		time.sleep(sleepTime)
	
	grid.render(start, rope, size)
	result1 = len(grid)
	
	# Part 2:
	grid = Grid({start: True})
	rope = Rope([start] * 10)
	
	# do movement
	for index, direction in enumerate(movements):
		rope.move(direction, grid)
		rope.update(grid)
		grid[rope.tail] = True

		print(f"{index} / {len(movements)-1}")
		grid.render(start, rope, size)
		time.sleep(sleepTime)
	
	grid.render(start, rope, size)
	result2 = len(grid)
	
	# results
	print("Part 1:", result1)
	print("Part 2:", result2)


if __name__ == "__main__":
	main()
