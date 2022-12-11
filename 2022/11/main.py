
import sys, re


class Monkey:
	def __init__(self, name, items, operation, test, decision):
		self.name      : str               = name
		self.items     : list[int]         = items
		self.operation : object            = operation  # lambda function
		self.test      : int               = test
		self.decision  : dict[bool:Monkey] = decision
	
	def inspect(self):
		worryLvl = self.items.pop(0)
		worryLvl = self.operation(worryLvl)
		worryLvl //= 3
		decision[ worryLvl % test == 0 ].catch(item)
	
	def catch(self, item):
		self.items.append(item)
	
	def __repr__(self):
		return f"Monkey(name='{self.name}', items={self.items}, operation={self.operation}, test={self.test}, decision={'{'}True: Monkey(name='{self.decision[True].name}'), False: Monkey(name='{self.decision[False].name}'){'}'})"


def parseMonkey(lines):
	intPattern = re.compile(r"\d+")

	name = intPattern.findall(lines[0])[0]
	items = list(map( int, intPattern.findall(lines[1]) ))
	operation = eval(f"lambda old: {lines[2].split('=')[1]}")
	test = int(intPattern.findall(lines[3])[0])
	ifTrue = int(intPattern.findall(lines[4])[0])
	ifFalse = int(intPattern.findall(lines[5])[0])
	decision = {True: ifTrue, False: ifFalse}
	
	return Monkey(name, items, operation, test, decision)
	

def main():
	# read data file
	inputFile = sys.argv[1] if len(sys.argv) >= 2 else "example.txt"
	with open(inputFile, "r") as fobj:
		lines = fobj.readlines()
		
		monkeyCount = (len(lines)+1) // 7
		monkeys = []
		for lineNum in range(monkeyCount):
			monkeys.append( parseMonkey(lines[lineNum*7:(lineNum+1)*7]) )
	
	# replace monkey names by Monkey objects in decision dictionary
	for monkey in monkeys:
		monkey.decision[True ] = monkeys[ int(monkey.decision[True ]) ]
		monkey.decision[False] = monkeys[ int(monkey.decision[False]) ]

	print(monkeys)
	
	# do rounds
	for roundNum in range(20):
		
		# do turns
		for monkey in monkeys:
			pass
	
	# result
	print("Part 1:")


if __name__ == "__main__":
	main()
