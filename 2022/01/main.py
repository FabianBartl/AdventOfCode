
import sys


def getTotalCalories(data: list, sorted:bool=True) -> list[int]:
	totalCalories = []
	calories = 0
	
	for line in data:
		if line == "\n":
			totalCalories.append(calories)
			calories = 0
		else:
			calories += int(line)
	totalCalories.append(calories)
	
	if sorted:
		totalCalories.sort()
	
	return totalCalories


def main():
	# read data file
	inputFile = sys.argv[1] if len(sys.argv) >= 2 else "example.txt"
	with open(inputFile, "r") as fobj:
		inputData = fobj.readlines()
	
	# get calories per elve
	totalCalories = getTotalCalories(inputData, sorted=True)
	
	# get max calories
	maxCalories = totalCalories[-1]
	# get top 3 calories
	top3Calories = totalCalories[-3:]
	
	# result
	print(totalCalories)
	print("Part 1:", maxCalories)
	print("Part 2:", sum(top3Calories))


if __name__ == "__main__":
	main()
