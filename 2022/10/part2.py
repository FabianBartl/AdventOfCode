
import sys, time


class Machine:
	def __init__(self):
		self.regX = 0				# sprite position
		self.cycle = 0				# clock cycle
		self.screen = [False] * 240	# 40 cols x 6 rows
	
	def update(self, value=None):
		if self.regX <= self.cycle % 40 <= self.regX+2:
			self.screen[self.cycle] = True
		if value is not None:
			self.regX += value
		self.cycle += 1
	
	def render(self):
		for pos in range(0, 240):
			print("█" if self.screen[pos] else " ", end="")
			if (pos+1) % 40 == 0:
				print()
	
	def __repr__(self):
		return f"Machine(regX={self.regX}, cycle={self.cycle})"


def main():
	# read data file
	inputFile = sys.argv[1] if len(sys.argv) >= 2 else "example2.txt"
	with open(inputFile, "r") as fobj:
		lines = fobj.readlines()
	
	machine = Machine()
	sleepTime = 0.000_1
	
	t0 = time.time()
	for line in lines:
		line = line.strip().split(" ")
		
		if line[0] == "noop":
			machine.update()
		
		elif line[0] == "addx":
			machine.update()
			machine.update(int(line[1]))
		
		print("\nCycle:", machine.cycle)
		machine.render()
		time.sleep(sleepTime)
	
	# result
	print("\nPart 2:", f"({1 / (time.time() - t0)} FPS)")
	machine.render()


if __name__ == "__main__":
	main()
