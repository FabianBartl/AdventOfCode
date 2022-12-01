
with open("input.txt", "r") as file:
	
	lines = [ line.strip("\n") for line in file ]
	right, down = [1, 3, 5, 7, 1], [1, 1, 1, 1, 2]
	p1, p2 = 0, 0
	
	for i in range(len(right)):
	
		pos_x = 0
		counter = 0

		for pos_y in range(0, len(lines), down[i]):
			if lines[pos_y][pos_x] == "#": counter += 1
			pos_x = (pos_x + right[i]) % len(lines[0])
		
		if right[i] == 3 and down[i] == 1: p1 = counter
		p2 *= counter
	
	print(f"Part 1: {p1}")
	print(f"Part 2: {p2}")
