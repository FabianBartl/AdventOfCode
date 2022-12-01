

def countGold(listOfBags, bagsDict):
	for bag in listOfBags:
		print(bag)
		if bag == "no other":
			return 0
		elif bag == "shiny gold":
			return 1
		else:
			return countGold(bagsDict[bag], bagsDict)


with open("input.txt", "r") as file:
	
	lines = [ line.strip("\n") for line in file ]
	data = {}
	tmp_lst, tmp_str = [], ""
	p1, p2 = 0, 0
	
	# Part 1
	for line in lines:

		key_color = line.split("contain")[0].strip("bags ")
		value_colors = line.split("contain")[1].split(",")

		tmp_lst = []
		for i, element in enumerate(value_colors):
			tmp_str = ""
			
			print(element)
			for element_part in element.split(" ")[2:4]:
				tmp_str += element_part + " "
			
			tmp_lst.append(tmp_str[:-1])
		data[key_color] = tmp_lst
		print(tmp_lst)
	
	print(data)
	
	for dataset in data.values():
		print(countGold(dataset, data))
	
	print(f"Part 1: {p1}")
	print(f"Part 2: {p2}")

	
	



