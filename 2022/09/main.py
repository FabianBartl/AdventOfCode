
import sys


def main():
	# read data file
	inputFile = sys.argv[1] if len(sys.argv) >= 2 else "example.txt"
	inputData = []
	with open(inputFile, "r") as fobj:
		lines = fobj.readlines()
	
	# solve it
	for line in lines:
		line = line.strip()
	
	# result
	print("Part 1:")


if __name__ == "__main__":
	main()
