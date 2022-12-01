
with open("input.txt", "r") as file:

	lines = [ line.strip("\n") for line in file ]
	data = []
	tmp_str = ""
	p1, p2 = 0, 0

	lines.append("")
	for line in lines:
		if line == "":
			data.append(tmp_str.split(" ")[:-1])
			tmp_str = ""
		else:
			tmp_str += line + " "
	
	# Part 1
	for dataset in data:
	
		letterStr = ""
		for person in dataset:
			letterStr += person
	
		letterSet = { letter for letter in [ letter for letter in letterStr ] }
		
		p1 += len(letterSet)
	
	# Part 2
	for dataset in data:
		
		personSets = []
		for person in dataset:
			personSets.append(set([ letter for letter in person ]))
		
		intersection = set(personSets[0])
		for personSet in personSets:
			intersection &= personSet
		
		p2 += len(intersection)	

	print(f"Part 1: {p1}")
	print(f"Part 2: {p2}")
