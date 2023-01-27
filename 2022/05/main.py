
import sys, re, copy


def main():
	# read data file
	inputFile = sys.argv[1] if len(sys.argv) >= 2 else "example.txt"
	inputData = []
	with open(inputFile, "r") as fobj:
		lines = fobj.readlines()
		
		# get stacks data
		stackCount = (len(lines[0][:-1]) + 1) // 4
		emptyRow = [ [] for _ in range(stackCount) ]
		
		# read stacks
		stacks = emptyRow[:]
		lineIndex = 0
		for line in lines:
			line = line[:-1]
			lineIndex += 1
			if not line or line[1] == "1":
				break
			
			# put crates on stacks
			for stackNum in range(stackCount):
				crate = line[1 + 4*stackNum]
				if crate.strip():
					stacks[stackNum].append(crate)
	
	# copy stacks for different movements from part 1 and 2
	stacksP1 = copy.deepcopy(stacks)
	stacksP2 = copy.deepcopy(stacks)
	
	# read moves
	pattern = re.compile(r"\d+")
	moveArgs = dict()
	for line in lines[lineIndex+1:]:
		line = line.strip()
		args = pattern.findall(line)
		moveArgs = {"from": int(args[1])-1, "to": int(args[2])-1, "amount": int(args[0])}
		
		# execute move for part 1
		for crateNum in range(moveArgs["amount"]):
			crate = stacksP1[moveArgs["from"]].pop(0)
			stacksP1[moveArgs["to"]].insert(0, crate)
		
		# execute move for part 2
		crates = [ stacksP2[moveArgs["from"]].pop(0) for crateNum in range(moveArgs["amount"]) ]
		crates.reverse()
		for crate in crates:
			stacksP2[moveArgs["to"]].insert(0, crate)
	
	# get top crates
	topCratesP1 = "".join([ stacksP1[stackNum][0] for stackNum in range(stackCount) ])
	topCratesP2 = "".join([ stacksP2[stackNum][0] for stackNum in range(stackCount) ])
		
	# results
	print("Part 1:", topCratesP1)
	print("Part 2:", topCratesP2)


if __name__ == "__main__":
	main()
