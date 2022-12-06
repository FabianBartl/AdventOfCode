
import sys


def main():
	# read data file
	inputFile = sys.argv[1] if len(sys.argv) >= 2 else "example.txt"
	with open(inputFile, "r") as fobj:
		stream = fobj.readline().strip()
	
	# get starting sequence
	seqPos_start = 0
	seqLen = 4
	for index, _ in enumerate(stream[:-seqLen]):
		seq = stream[index:index+seqLen]
		seqSet = set(seq)
		# print(seq, seqSet)
		if len(seqSet) == seqLen:
			seqPos_start = index + seqLen
			break
	
	# get message sequence
	seqPos_message = 0
	seqLen = 14
	for index, _ in enumerate(stream[:-seqLen]):
		seq = stream[index:index+seqLen]
		seqSet = set(seq)
		# print(seq, seqSet)
		if len(seqSet) == seqLen:
			seqPos_message = index + seqLen
			break
		
	# results
	print("Part 1:", seqPos_start)
	print("Part 2:", seqPos_message)


if __name__ == "__main__":
	main()
