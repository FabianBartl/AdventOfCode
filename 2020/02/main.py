
with open("input.txt", "r") as file:
	
	lines = [ line.strip("\n") for line in file ]
	p1, p2 = 0, 0
	
	for rule in lines:
	
		letter = rule.split(" ")[1][:-1]
		word = rule.split(" ")[-1]

		#Part 1
		min = int(rule.split("-")[0])
		max = int(rule.split("-")[1].split(" ")[0])
		if min <= word.count(letter) <= max: p1 += 1
		
		# Part 2
		pos1 = int(rule.split("-")[0]) - 1
		pos2 = int(rule.split("-")[1].split(" ")[0]) - 1
		if word[pos1] != word[pos2] and ( word[pos1] == letter or word[pos2] == letter ): p2 += 1
	
	print(f"Part 1: {p1}")
	print(f"Part 2: {p2}")

# One-Liner
f=open("input.txt");l=[z.strip("\n") for z in f];e=[[rule.split(" ")[1][:-1],rule.split(" ")[-1],int(rule.split("-")[0]),int(rule.split("-")[1].split(" ")[0])]for rule in l];p=len([0 for p in e if p[2]<=p[1].count(p[0])<=p[3]]);s=len([0 for p in e if p[1][p[2]-1]!=p[1][p[3]-1]and(p[1][p[2]-1]==p[0]or p[1][p[3]-1]==p[0])]);print(f"Part 1: {p}\nPart 2: {s}")
