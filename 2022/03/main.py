
import sys, string


def char2priority(char:str):
	return string.ascii_letters.index(char) + 1



def part1(inputFile:str):
	# read data file
	inputData = []
	with open(inputFile, "r") as fobj:
		for line in fobj.readlines():
			line = line.strip()
			halfLenght = len(line) // 2
			inputData.append([ set(line[halfLenght:]), set(line[:halfLenght]) ])
	
	# extract intersecting char
	totalPriority = 0
	for rucksack in inputData:
		char = min(rucksack[0] & rucksack[1])
		priority = char2priority(char)
		totalPriority += priority
	
	# result
	print("Part 1:", totalPriority)


def part2(inputFile:str):
	# read data file
	inputData = []
	with open(inputFile, "r") as fobj:
		for line in fobj.readlines():
			line = line.strip()
			inputData.append(set(line))
	
	# extract intersecting char
	totalPriority = 0
	for index, rucksack in enumerate(inputData):
		if not index % 3:
			char = min(rucksack & inputData[index+1] & inputData[index+2])
			priority = char2priority(char)
			totalPriority += priority
	
	# result
	print("Part 2:", totalPriority)


if __name__ == "__main__":
	inputFile = sys.argv[1] if len(sys.argv) >= 2 else "example.txt"
	part1(inputFile)
	part2(inputFile)
