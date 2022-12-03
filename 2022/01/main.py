
import sys


def getTotalCalories(data: list) -> list[int]:
	totalCalories = []
	calories = 0
	
	for line in data:
		line = line.strip()
		if line == "":
			totalCalories.append(calories)
			calories = 0
		else:
			calories += int(line)
	totalCalories.append(calories)
	
	totalCalories.sort()
	
	return totalCalories


def main():
	# read data file
	inputFile = sys.argv[1] if len(sys.argv) >= 2 else "example.txt"
	with open(inputFile, "r") as fobj:
		inputData = fobj.readlines()
	
	# get calories per elve
	totalCalories = getTotalCalories(inputData)
	
	# get max calories
	maxCalories = totalCalories[-1]
	# get top 3 calories
	top3Calories = totalCalories[-3:]
	
	# result
	print("Part 1:", maxCalories)
	print("Part 2:", sum(top3Calories))


if __name__ == "__main__":
	main()
