
import sys, re


class Tree:
	def __init__(self, height, visible=False, score=0):
		self.height = height
		self.visible = visible
		self.score = score
	
	def render(self):
		return "#" if self.visible else "_"
	
	def __repr__(self):
		return f"Tree(height={self.height}, visible={self.visible}, score={self.score})"
	
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
	
	def getMaxScore(self):
		maxScore = 0
		for row in self:
			for tree in row:
				if tree.score > maxScore:
					maxScore = tree.score
		return maxScore
	
	def render(self, *, rowStr=lambda row: "[" + "".join([ tree.render() for tree in row ]) + "]"):
		gridStr = ""
		for num, row in enumerate(self.treeGrid):
			gridStr += " [" if not num else "  "
			gridStr += rowStr(row)
			gridStr += ",\n" if num != self.rowsNum-1 else "]"
		return f"Forest(\n{gridStr}\n)"
	
	def __repr__(self):
		return self.render(rowStr=lambda row: f"{row}")
	
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

def setScore(forest):
	for r in range(forest.rowsNum):
		for c in range(forest.columnsNum):
			tree = forest.treeGrid[r][c]
			
			# look to right
			counterRight = 0
			for colNum in range(c+1, forest.columnsNum):
				counterRight += 1
				if len(forest.treeGrid[r][colNum]) >= len(tree):
					break
			
			# look to left
			counterLeft = 0
			for colNum in range(-(forest.columnsNum-c+1), -(forest.columnsNum+1), -1):
				counterLeft += 1
				if len(forest.treeGrid[r][colNum]) >= len(tree):
					break
			
			# look to bottom
			counterBottom = 0
			for rowNum in range(r+1, forest.rowsNum):
				counterBottom += 1
				if len(forest.treeGrid[rowNum][c]) >= len(tree):
					break
			
			# look to top
			counterTop = 0
			for rowNum in range(-(forest.rowsNum-r+1), -(forest.rowsNum+1), -1):
				counterTop += 1
				if len(forest.treeGrid[rowNum][c]) >= len(tree):
					break
			
			tree.score = counterRight * counterLeft * counterBottom * counterTop


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
				treeRow.append(Tree(int(char), visibility, 0))
			treeGrid.append(treeRow)
		forest = Forest(treeGrid)
	
	# Part 1: get total number of visible trees
	setVisibility(forest)
	totalVisibleTrees = forest.countVisibleTrees()
	
	# Part 2: get tree score with the best viewing distance in all directions
	setScore(forest)
	maxScore = forest.getMaxScore()
	
	# result
	print(forest.render(), "\n")
	print("Part 1:", totalVisibleTrees)
	print("Part 2:", maxScore)


if __name__ == "__main__":
	main()
