
import sys, re


class Tree:
	def __init__(self, height, visible=False):
		self.height = height
		self.visible = visible
	
	def __repr__(self):
		return f"Tree({len(self)}, {bool(self)})"
	
	def __len__(self):
		return int(self.height)
	
	def __bool__(self):
		return bool(self.visible)
	
	def __lt__(self, otherTree):
		return len(self) < len(otherTree)
	
	def __gt__(self, otherTree):
		return len(self) > len(otherTree)

class Forest:
	def __init__(self, treeGrid):
		self.treeGrid = treeGrid
		self.rowsNum = len(self.treeGrid)
		self.columnsNum = len(self.treeGrid[0])
	
	def __repr__(self):
		gridStr = ""
		for num, row in enumerate(self.treeGrid):
			if num == 0:
				gridStr += " ["
			else:
				gridStr += "  "
			gridStr += "".join([ "#" if tree else "_" for tree in row ])
			if num != self.rowsNum-1:
				gridStr += "\n"
			else:
				gridStr += "]"
		return f"Forest(\n{gridStr}\n)"
	
	def __len__(self):
		return self.rowsNum * self.columnsNum
	
	def __getitem__(self, row, column):
		return self.treeGrid[row][column]
	
	def __setitem__(self, row, column, treeVisibility):
		self.treeGrid[row][column].visible = bool(treeVisibility)


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
	
	# look from top
	print(forest)
	
	# result
	print("Part 1:")


if __name__ == "__main__":
	main()
