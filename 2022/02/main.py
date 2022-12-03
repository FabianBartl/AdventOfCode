
import sys

symbol2points = {
	"A": 1,  "X": 1,  # Rock
	"B": 2,  "Y": 2,  # Paper
	"C": 3,  "Z": 3   # Scissor
}

result2points = {
	"l": 0,  # lose
	"d": 3,  # draw
	"w": 6   # won
}

pointsT2result = {
	(1,1): "d",
	(1,2): "w",
	(1,3): "l",
	(2,1): "l",
	(2,2): "d",
	(2,3): "w",
	(3,1): "w",
	(3,2): "l",
	(3,3): "d"
}

symbol2result = {
	"X": "l",  # lose
	"Y": "d",  # draw
	"Z": "w"   # won
}

pointsResult2points = {
	(1,"l"): 3,
	(1,"d"): 1,
	(1,"w"): 2,
	(2,"l"): 1,
	(2,"d"): 2,
	(2,"w"): 3,
	(3,"l"): 2,
	(3,"d"): 3,
	(3,"w"): 1
}


def part1(inputFile:str):
	# read data file
	inputData = []
	with open(inputFile, "r") as fobj:
		for line in fobj.readlines():
			symbols = line.strip().split(" ")
			inputData.append([ symbol2points[symbols[0]], symbol2points[symbols[1]] ])
	
	# calculate points
	totalPoints = 0
	for _round in inputData:
		op, me = _round[0], _round[1]
		result = pointsT2result[(op,me)]
		totalPoints += me + result2points[result]
	
	print("Part 1:", totalPoints)


def part2(inputFile:str):
	# read data file
	inputData = []
	with open(inputFile, "r") as fobj:
		for line in fobj.readlines():
			symbols = line.strip().split(" ")
			inputData.append([ symbol2points[symbols[0]], symbol2result[symbols[1]] ])
	
	# calculate points
	totalPoints = 0
	for _round in inputData:
		op, me = _round[0], _round[1]  # points:int, result:str
		points = pointsResult2points[(op,me)]
		result = pointsT2result[(op,points)]
		totalPoints += points + result2points[result]
	
	print("Part 2:", totalPoints)


if __name__ == "__main__":
	inputFile = sys.argv[1] if len(sys.argv) >= 2 else "example.txt"
	part1(inputFile)
	part2(inputFile)
