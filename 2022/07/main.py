
import sys

class Directory:
	def __init__(self, name, parent, size=0):
		self.name = name
		self.size = size
		self.entries = []
		self.parent = parent
	
	def addEntry(self, entry):
		self.entries.append(entry)
		# self.size += entry.size
	
	def getEntry(self, name):
		for entry in self.entries:
			if entry.name == name:
				return entry
	
	def printTree(self, depth=0):
		print(f"{'  '*depth}- {self.name} (dir, size={self.size})")
		for entry in self.entries:
			if type(entry) is File:
				print(f"{'  '*(depth+1)}- {entry.name} (file, size={entry.size})")
			else:
				entry.printTree(depth+1)
	
	def __repr__(self):
		return f"Directory('{self.name}')"

class File:
	def __init__(self, name, parent, size=0):
		self.name = name
		self.size = size
		self.parent = parent
	
	def __repr__(self):
		return f"File('{self.name}')"


def getDeepestDirs(dir, deepestDirs, currDepth=0):
	noDirs = True
	for entry in dir.entries:
		if type(entry) is Directory:
			if deeperDir := getDeepestDirs(entry, deepestDirs, currDepth+1):
				deepestDirs.append(deeperDir)
			noDirs = False
	if noDirs:
		return dir, currDepth

def getAllDirs(dir, allDirs, currDepth=0):
	for entry in dir.entries:
		if type(entry) is Directory:
			allDirs.append(getAllDirs(entry, allDirs, currDepth+1))
	return dir, currDepth

def getEntrySize(entry):
	if type(entry) is File:
		return entry.size
	else:
		return sum(map(getEntrySize, entry.entries))


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
	
	# get size of every directory
	rootDir.size = getEntrySize(rootDir)
	allDirs = []
	getAllDirs(rootDir, allDirs)
	for dir, _ in allDirs:
		dir.size = getEntrySize(dir)
	
	# Part 1: get the sum of sizes of all directories smaller than 100_000
	maxSize = 100_000
	totalSize = 0
	for dir, _ in allDirs:
		if dir.size <= maxSize:
			totalSize += dir.size
	
	# Part 2: get the smallest size of the directories, that are big enough to make space for the update
	diskSize = 70_000_000
	updateSize = 30_000_000
	neededSize = updateSize - (diskSize - rootDir.size)
	
	freedSize = 0
	possibleDirs = []
	for dir, _ in allDirs:
		if dir.size >= neededSize:
			possibleDirs.append(dir)
	freedSize = min(possibleDirs, key=lambda x: x.size).size
	
	# results
	rootDir.printTree()
	print("Part 1:", totalSize)
	print("Part 2:", freedSize)


if __name__ == "__main__":
	main()
