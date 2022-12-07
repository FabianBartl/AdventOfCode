
import sys

class Directory:
	def __init__(self, name, parent, size=0):
		self.name = name
		self.size = size
		self.entries = []
		self.parent = parent
	
	def addEntry(self, entry):
		self.entries.append(entry)
		self.size += entry.size
	
	def getEntry(self, name):
		for entry in self.entries:
			if entry.name == name:
				return entry
	
	def printTree(self, depth=0):
		print(f"{'  '*depth}{self.__repr__()}")
		for entry in self.entries:
			if type(entry) is File:
				print(f"{'  '*(depth+1)}{entry.__repr__()}")
			else:
				entry.printTree(depth+1)
	
	def __repr__(self):
		return f"- {self.name} (dir, size={self.size})"

class File:
	def __init__(self, name, parent, size=0):
		self.name = name
		self.size = size
		self.parent = parent
	
	def __repr__(self):
		return f"- {self.name} (file, size={self.size})"


def main():
	# read data file
	inputFile = sys.argv[1] if len(sys.argv) >= 2 else "example.txt"
	with open(inputFile, "r") as fobj:
		lines = fobj.readlines()
		
		previousDir = None
		currentDir = None
		rootDir = Directory("/", previousDir)
		
		for num, line in enumerate(lines):
			args = line.strip().split(" ")
			
			if args[0] == "$":
				
				if args[1] == "cd":
					if args[2] == "/":
						currentDir = rootDir
					elif args[2] == "..":
						currentDir = currentDir.parent
					else:
						currentDir = currentDir.getEntry(args[2])
				
				elif args[1] == "ls":
					pass
			
			elif args[0] == "dir":
				currentDir.addEntry(Directory(args[1], currentDir))
			
			else:
				currentDir.addEntry(File(args[1], currentDir, int(args[0])))
	
	rootDir.printTree()
	
	# solve it
	maxSize = 100_000
	bigSizes = []
	for entry in rootDir.entries:
		if type(entry) is Directory:
			if entry.size < maxSize:
				bigSizes.append(entry.size)
	
	# result
	print("Part 1:")


if __name__ == "__main__":
	main()
