
with open("input.txt", "r") as file:
	
	lines = [ int(line.strip("\n")) for line in file ]
	p1, p2 = 0, 0
	
	# Part 1
	for i_ind, i_el in enumerate(lines):
		for j_ind, j_el in enumerate(lines):
			if i_el + j_el == 2020 and i_ind != j_ind:
				p1 = i_el * j_el
	
	# Part 2
	for i_ind, i_el in enumerate(lines):
		for j_ind, j_el in enumerate(lines):
			for k_ind, k_el in enumerate(lines):
				if i_el + j_el + k_el == 2020 and i_ind != j_ind != k_ind:
					p2 = i_el * j_el * k_el

	print(f"Part 1: {p1}")
	print(f"Part 2: {p2}")

# One-Liner
f=open("input.txt");l=[int(z.strip("\n"))for z in f];p=max([[q*w for e,w in enumerate(l)if q+w==2020 and r!=e]for r,q in enumerate(l)])[0];s=max([max(m)for m in[[[q*w*t for u,t in enumerate(l)if q+w+t==2020 and r!=e!=u]for e,w in enumerate(l)]for r,q in enumerate(l)]])[0];print(f"Part 1: {p}\nPart 2: {s}")
