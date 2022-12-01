
import re

with open("input.txt", "r") as file:
	
	lines = [ line.strip("\n") for line in file ]
	data = []
	tmp_str = ""
	required = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"] # 'cid' is optional
	p1, p2 = 0, 0
	
	lines.append("")
	for line in lines:
		if line == "":
			data.append(tmp_str.split(" ")[:-1])
			tmp_str = ""
		else:
			tmp_str += line + " "

	for dataset in data:
		key_lst, val_lst = [], []
		accept1, accept2 = False, False
		
		for date in dataset:
			key_lst.append(date.split(":")[0])
			val_lst.append(date.split(":")[1])
		
		# Part 1
		for i in range(len(required)):
			if required[i] in key_lst: accept1 = True
			else: accept1 = False
			if not accept1: break
		if accept1: p1 += 1
		
		# Part 2
		for i in range(len(required)):
			if required[i] in key_lst:
				pos = key_lst.index(required[i])
				
				if key_lst[pos] == "byr" and val_lst[pos].isdigit():
					if 1920 <= int(val_lst[pos]) <= 2002: accept2 = True
					else: accept2 = False
					
				elif key_lst[pos] == "iyr" and val_lst[pos].isdigit():
					if 2010 <= int(val_lst[pos]) <= 2020: accept2 = True
					else: accept2 = False

				elif key_lst[pos] == "eyr" and val_lst[pos].isdigit():
					if 2020 <= int(val_lst[pos]) <= 2030: accept2 = True
					else: accept2 = False
					
				elif key_lst[pos] == "hgt" and re.search(r"[0-9]+(cm|in)", val_lst[pos]):
					if val_lst[pos][-2:] == "cm" and (150 <= int(val_lst[pos][:-2]) <= 193): accept2 = True
					elif val_lst[pos][-2:] == "in" and (59 <= int(val_lst[pos][:-2]) <= 76): accept2 = True
					else: accept2 = False
				
				elif key_lst[pos] == "hcl" and re.search(r"#[0-9a-f]{6}", val_lst[pos]): accept2 = True
				elif key_lst[pos] == "ecl" and val_lst[pos] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]: accept2 = True
				elif key_lst[pos] == "pid" and re.search(r"[0-9]{9}", val_lst[pos]): accept2 = True
				else: accept2 = False
			else: accept2 = False
			if not accept2: break
		if accept2: p2 += 1
	
	print(f"Part 1: {p1}")
	print(f"Part 2: {p2}")
