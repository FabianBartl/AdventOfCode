
import sys

class Machine:
	def __init__(self):
		self.regX = 1
		self.cycle = 0
		self.strenghts = []
	
	def update(self):
		self.cycle += 1
		if (self.cycle-20) % 40 == 0:
			signal = self.regX * self.cycle
			print(signal)
			self.strenghts.append(signal)

def main():
	# read data file
	inputFile = sys.argv[1] if len(sys.argv) >= 2 else "example.txt"
	with open(inputFile, "r") as fobj:
		lines = fobj.readlines()
	
	machine = Machine()
	
	for line in lines:
		line = line.strip()
		
		if line == "noop":
			machine.update()
		
		elif line.startswith("addx"):
			num = int(line.split(" ")[1])
			machine.update()
			machine.update()
			machine.regX += num
	
	# result
	print("Part 1:", sum(machine.strenghts))


if __name__ == "__main__":
	main()
