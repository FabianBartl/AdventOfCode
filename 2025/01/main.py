
import sys


def solve_part1(lines: list[str]) -> None:
    stats = { num: 0 for num in range(100) }
    current = 50
    
    for ind, line in enumerate(lines):
        direction = str(line[0]).lower()
        count = int(line[1:])
        print(f"\n{ind}:\t{direction=} {count=}", end=" ")
        
        if direction == "r":
            current += count
        elif direction == "l":
            current -= count
        else:
            print(f"unknown {direction=}")
        
        current %= 100
        stats[current] += 1
        print(f"{current=} {stats[current]=}", end=" ")
    
    print(f"Solution 1: {stats[0]}")


"""
def solve_part2(lines: list[str]) -> None:
    passed_zero = 0
    current = 50
    
    for ind, line in enumerate(lines):
        direction = str(line[0]).lower()
        count = int(line[1:])
        print(f"\n{ind}:\t{direction=}   {count=}", end="   ")
        
        before = current
        if direction == "r":
            after = current + count
        elif direction == "l":
            after = current - count

        pz = 0
        if after < 0 or after > 99:
            pz += abs(after // 100)
        
        corrected = after % 100
        
        if corrected == 0 and pz != 0:
            pz += 1
            
        if pz > 0 and before == 0:
            pz -= 1
        
        print(f"{corrected=}", end="   ")
        if pz > 0:
            print(f"{pz=}", end="   ")
        
        passed_zero += pz
        current = corrected
        
    print(f"Solution 2: {passed_zero}")
"""


def solve_part2(lines: list[str]) -> None:
    passed_zero = 0
    current = 50
    
    for ind, line in enumerate(lines):
        direction = str(line[0]).lower()
        count = int(line[1:])
        
        pz = 0
        # the stupidly trivial way:
        for _ in range(count):
            if direction == "r":
                current += 1
            elif direction == "l":
                current -= 1
            
            if current > 99:
                current = 0
            elif current < 0:
                current = 99

            if current == 0:
                pz += 1
        
        print(f"{ind}", end=" ")
        passed_zero += pz
        
        print(f"The dial is rotated {direction.upper()}{count} to point at {current}.", end=" ")
        if pz > 0:
            print(f"During this rotation, it points at zero {pz}x.", end=" ")
        print("")
        
    print(f"Solution 2: {passed_zero}")


def main() -> None:
    inputFile = sys.argv[1] if len(sys.argv) >= 2 else "example.txt"
    inputData = []
    with open(inputFile, "r") as fobj:
        lines = [ line.strip() for line in fobj.readlines() ]

    solve_part1(lines)
    solve_part2(lines)


if __name__ == "__main__":
    main()
