
import sys


def main():
	# read data file
	inputFile = sys.argv[1] if len(sys.argv) >= 2 else "example.txt"
	inputData = []
	with open(inputFile, "r") as fobj:
		for line in fobj.readlines():
			line = line.strip().split(",")
			section1 = list(map(int, line[0].split("-")))
			section2 = list(map(int, line[1].split("-")))
			inputData.append([ [min(section1), max(section1)], [min(section2), max(section2)] ])
	
	# extract intersecting char
	overlapsP1 = overlapsP2 = 0
	for sections in inputData:
		section1, section2 = sections
		
		if section2[0] <= section1[0] <= section2[1] and section2[0] <= section1[1] <= section2[1] or \
		   section1[0] <= section2[0] <= section1[1] and section1[0] <= section2[1] <= section1[1]:
			overlapsP1 += 1
		
		if section2[0] <= section1[0] <= section2[1] or section2[0] <= section1[1] <= section2[1] or \
		   section1[0] <= section2[0] <= section1[1] or section1[0] <= section2[1] <= section1[1]:
			overlapsP2 += 1
	
	# result
	print("Part 1:", overlapsP1)
	print("Part 2:", overlapsP2)


if __name__ == "__main__":
	main()
