
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


def parseMonkey(lines):
	print(lines)
	intPattern = re.compile(r"\d+")
	name = intPattern.findall(lines[0])[0]
	items = list(map( int, intPattern.findall(lines[1]) ))
	# operation = 
	test = int(intPattern.findall(lines[3])[0])
	# ifTrue = 
	# ifFalse = 
	# decision = {True: , False: }


def main():
	# read data file
	inputFile = sys.argv[1] if len(sys.argv) >= 2 else "example.txt"
	with open(inputFile, "r") as fobj:
		lines = fobj.readlines()
		
		monkeyCount = (len(lines)+1) // 7
		monkeys = []
		
		for lineNum in range(monkeyCount):
			print(lineNum, lineNum+7)
			monkeys.append( parseMonkey(lines[lineNum*7:(lineNum+1)*7]) )
	
	# result
	print("Part 1:")


if __name__ == "__main__":
	main()
