
lines = [ int(line.strip("\n")) for line in open("input.txt", "r") if line.strip("\n") != "" ]
preambleLen = 5
tmp_lst = []

for currInd, currNum in enumerate(lines):
	if currInd - preambleLen <= 0: continue
	
	for lastNum1 in lines[currInd - preambleLen:currInd]:
		for lastNum2 in lines[currInd - preambleLen:currInd]:
		
			if lastNum1 == lastNum2: continue
			
			elif lastNum1 + lastNum2 == currNum: accept = True
			else: accept = False; break
		
		if not accept: break
	if not accept: tmp_lst.append([currInd, currNum])

print([ num[:] for num in tmp_lst[:] ])
print("end\n")
