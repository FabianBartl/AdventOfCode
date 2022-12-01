
def binarySearch(word, i, minLimit, maxLimit):
	if i == len(word)-1:
		if word[i] == "0":
			return minLimit
		elif word[i] == "1":
			return maxLimit
		
	elif word[i] == "0": #1st part of seat range ('0' means 'F' or 'L')
		return binarySearch(word, i+1, minLimit, ((maxLimit-minLimit)//2)+minLimit)
		
	elif word[i] == "1": #2nd part of seat range ('1' means 'B' or 'R')
		return binarySearch(word, i+1, ((maxLimit-minLimit)//2)+minLimit+1, maxLimit)


# only getMySeat function is by: https://github.com/Square789/AoC/blob/main/y2020/vis/v05.py
def getMySeat(words):

	seatIDs = [ int(word.replace("F", "0").replace("B", "1").replace("L", "0").replace("R", "1"), 2) for word in words ]
	
	for seatID in range(128*8):
		prevSeat, nextSeat = seatID - 1, seatID + 1
	
		if seatID not in seatIDs and prevSeat in seatIDs and nextSeat in seatIDs:
			return seatID


with open("input.txt", "r") as file:

	lines = [ line.strip("\n").upper() for line in file ]
	rowIDs, colIDs = [], []
	seatIDs = []
	p1, p2 = 0, 0

	for line in lines:
	
		line = line.replace("F", "0").replace("L", "0")
		line = line.replace("B", "1").replace("R", "1")
		
		rowNumber = binarySearch(line[:-3], 0, 0, 127)
		colNumber = binarySearch(line[-3:], 0, 0, 7)
		
		rowIDs.append(rowNumber)
		colIDs.append(colNumber)
		seatIDs.append(rowNumber * 8 + colNumber)

	p1 = max(seatIDs)
	p2 = getMySeat2(lines)
	
	print(f"Part 1: {p1}")
	print(f"Part 2: {p2}")
