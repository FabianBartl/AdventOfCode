
import sys

def main():
	# read data file
	inputFile = sys.argv[1] if len(sys.argv) >= 2 else "example.txt"
	with open(inputFile, "r") as fobj:
		lines = fobj.readlines()
	
	regX = 1
	cycle = 0
	
	for line in lines:
		line = line.strip()
		
		if line == "noop":
			cycle += 1
		
		elif line.startswith("addx"):
			num = int(line.split(" ")[1])
			cycle += 2
			regX += num
	
	# result
	print("Part 1:", f"{regX=}", f"{cycle=}")


if __name__ == "__main__":
	main()
