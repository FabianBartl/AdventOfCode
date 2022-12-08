
import sys, re


class Tree:
	def __init__(self, height, visible=False):
		self.height = height
		self.visible = visible
		self.score = 0
	
	def __repr__(self):
		return f"Tree({len(self)}, {'#' if self else '_'}, {self.score})"
	
	def __len__(self):
		return int(self.height)
	
	def __bool__(self):
		return bool(self.visible)
	
	def __gt__(self, otherTree):
		return len(self) > len(otherTree)

class Forest:
	def __init__(self, treeGrid):
		self.treeGrid = treeGrid
		self.rowsNum = len(self.treeGrid)
		self.columnsNum = len(self.treeGrid[0])
	
	def countVisibleTrees(self):
		visibleTrees = 0
		for row in self:
			for tree in row:
				if tree:
					visibleTrees += 1
		return visibleTrees
	
	def __repr__(self, *, onlyVisibility=False):
		gridStr = ""
		for num, row in enumerate(self.treeGrid):
			if num == 0:
				gridStr += " ["
			else:
				gridStr += "  "
			if onlyVisibility:
				treeStr = "".join([ f"{'#' if tree else '_'}" for tree in row ])
			else:
				treeStr = "".join([ f" {len(tree)} {'#' if tree else '_'} {tree.score} " for tree in row ])
			gridStr += "[" + treeStr + "]"
			if num != self.rowsNum-1:
				gridStr += ",\n"
			else:
				gridStr += "]"
		return f"Forest(\n{gridStr}\n)"
	
	def __iter__(self):
		return iter(self.treeGrid)


def setVisibility(forest):
	# look from left
	for rowNum, row in enumerate(forest):
		maxHeight = len(forest.treeGrid[rowNum][0])
		for colNum, tree in enumerate(row):
			if (currentHeight := len(tree)) > maxHeight:
				tree.visible = True
				maxHeight = currentHeight
	
	# look from right
	for rowNum, row in enumerate(forest):
		maxHeight = len(forest.treeGrid[rowNum][-1])
		for colNum, tree in enumerate(row[::-1]):
			if (currentHeight := len(tree)) > maxHeight:
				tree.visible = True
				maxHeight = currentHeight
	
	# look from top
	for colNum in range(forest.columnsNum):
		maxHeight = len(forest.treeGrid[0][colNum])
		for rowNum in range(forest.rowsNum):
			tree = forest.treeGrid[rowNum][colNum]
			if (currentHeight := len(tree)) > maxHeight:
				tree.visible = True
				maxHeight = currentHeight
	
	# look from top
	for colNum in range(forest.columnsNum):
		maxHeight = len(forest.treeGrid[-1][colNum])
		for rowNum in range(1, forest.rowsNum+1):
			tree = forest.treeGrid[-rowNum][colNum]
			if (currentHeight := len(tree)) > maxHeight:
				tree.visible = True
				maxHeight = currentHeight


def main():
	# read data file
	inputFile = sys.argv[1] if len(sys.argv) >= 2 else "example.txt"
	with open(inputFile, "r") as fobj:
		lines = fobj.readlines()
		
		treeGrid = []
		for num, line in enumerate(lines):
			line = line.strip()
			treeRow = []
			for pos, char in enumerate(line):
				visibility = (pos == 0 or pos == len(line)-1) or (num == 0 or num == len(lines)-1)
				treeRow.append(Tree(int(char), visibility))
			treeGrid.append(treeRow)
		forest = Forest(treeGrid)
	
	# Part 1: get total number of visible trees
	setVisibility(forest)
	totalVisibleTrees = forest.countVisibleTrees()
	
	# Part 2: get tree score with the best viewing distance in all directions
	scoreList = []
	for r in range(forest.rowsNum):
		for c in range(forest.columnsNum):
			tree = forest.treeGrid[r][c]
			
			# from left to right
			counterRight = 0
			for colNum in range(c+1, forest.columnsNum):
				counterRight += 1
				if len(forest.treeGrid[r][colNum]) >= len(tree):
					break
			
			# from right to left
			counterLeft = 0
			for colNum in range(-(forest.columnsNum-c+1), -(forest.columnsNum+1), -1):
				counterLeft += 1
				if len(forest.treeGrid[r][colNum]) >= len(tree):
					break
			
			# from top to bottom
			counterBottom = 0
			for rowNum in range(r+1, forest.rowsNum):
				counterBottom += 1
				if len(forest.treeGrid[rowNum][c]) >= len(tree):
					break
			
			# from bottom to top
			counterTop = 0
			for rowNum in range(-(forest.rowsNum-r+1), -(forest.rowsNum+1), -1):
				counterTop += 1
				if len(forest.treeGrid[rowNum][c]) >= len(tree):
					break
			
			scoreList.append(counterRight * counterLeft * counterBottom * counterTop)
	
	# result
	print(forest.__repr__(onlyVisibility=True))
	print("Part 1:", totalVisibleTrees)
	print("Part 2:", max(scoreList))


if __name__ == "__main__":
	main()
