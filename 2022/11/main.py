
import sys, re
from tqdm import tqdm


class Monkey:
	def __init__(self, name, items, operation, test, decision):
		self.name      : str               = name
		self.items     : list[int]         = items
		self.operation : object            = operation  # lambda function
		self.test      : int               = test
		self.decision  : dict[bool:Monkey] = decision
		self.inspections = 0
	
	def inspect(self, relieved):
		self.inspections += 1
		item = self.items.pop(0)
		item = self.operation(item)
		if relieved:
			item //= 3
		self.decision[ item % self.test == 0 ].catch(item)
	
	def inspectAll(self, relieved):
		for _ in range(len(self.items)):
			self.inspect(relieved)
	
	def catch(self, item):
		self.items.append(item)
	
	def copy(self):
		return Monkey(self.name, self.items.copy(), self.operation, self.test, self.decision.copy())
	
	def __repr__(self):
		return f"Monkey(name='{self.name}', items={self.items}, operation=<lambda function>, test={self.test}, decision={'{'}True: Monkey(name='{self.decision[True].name}'), False: Monkey(name='{self.decision[False].name}'){'}'}, inspections={self.inspections})"


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


def main(monkeys, rounds, relieved, part):
	# replace monkey names by Monkey objects in decision dictionary
	for monkey in monkeys:
		monkey.decision[True ] = monkeys[ int(monkey.decision[True ]) ]
		monkey.decision[False] = monkeys[ int(monkey.decision[False]) ]

	# do all rounds
	for roundNum in tqdm(range(rounds), desc="Rounds"):
		# do round
		for monkey in monkeys:
			# do turns
			while len(monkey.items) > 0:
				monkey.inspectAll(relieved)
	
	print(f"\nAfter Round: {rounds}")
	print("\n" + "\n\n".join([ monkey.__repr__() for monkey in monkeys ]))

	monkeys.sort( key=lambda x: x.inspections, reverse=True )
	monkeyBusiness = monkeys[0].inspections * monkeys[1].inspections
	
	# result
	print(f"\nPart {part}: {monkeyBusiness}\n\n")


if __name__ == "__main__":
	# read data file
	inputFile = sys.argv[1] if len(sys.argv) >= 2 else "example.txt"
	with open(inputFile, "r") as fobj:
		lines = fobj.readlines()
		
		monkeyCount = (len(lines)+1) // 7
		monkeys = []
		for lineNum in range(monkeyCount):
			monkeys.append( parseMonkey(lines[lineNum*7:(lineNum+1)*7]) )

	main([ monkey.copy() for monkey in monkeys ],    20, True,  1)
	main([ monkey.copy() for monkey in monkeys ], 1_000, False, 2)
