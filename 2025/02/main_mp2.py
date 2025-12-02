
import sys


def is_invalid_part1(num: int) -> bool:
    numtext = str(num)
    length = len(numtext)
    
    # odd numbers cant be symmetric -> always valid
    if length % 2 != 0:
        return False
    
    half = length // 2
    return numtext[:half] == numtext[half:]


def solve_part1(ranges: list[tuple[int, int]]) -> None:
    all_invalids = []
    
    for ind, interval in enumerate(ranges):
        lower, upper = interval
        print(f"\n{ind}: {interval=}")
        
        invalids = []
        for tested_num in range(lower, upper+1):
            if is_invalid_part1(tested_num):
                print(f"{tested_num=} is invalid")
                invalids.append(tested_num)

        print(f"found {len(invalids)} invalid numbers in the range")
        all_invalids.extend(invalids)

    print("Solution:", sum(all_invalids))


def is_invalid_part2(num: int) -> bool:
    numtext = str(num)
    length = len(numtext)
    
    max_pattern = 10**(length//2)
    for pattern in range(max_pattern):
        patterntext = str(pattern)
        if numtext.count(patterntext) == length / len(patterntext):
            return True
    
    return False


def solve_part2(ranges: list[tuple[int, int]]) -> None:
    all_invalids = []
    
    for ind, interval in enumerate(ranges):
        lower, upper = interval
        print(f"\n{ind}: {interval=}")
        
        invalids = []
        for tested_num in range(lower, upper+1):
            if is_invalid_part1(tested_num) or is_invalid_part2(tested_num):
                print(f"{tested_num=} is invalid")
                invalids.append(tested_num)

        print(f"found {len(invalids)} invalid numbers in the range")
        print(f"intermediate sum: {sum(invalids)}")
        all_invalids.extend(invalids)

    print(f"Solution: {sum(all_invalids)}       {sum(all_invalids):_}")


def main() -> None:
    inputFile = sys.argv[1] if len(sys.argv) >= 2 else "example.txt"
    inputData = []
    with open(inputFile, "r") as fobj:
        lines = [ line.strip() for line in fobj.readlines() ]
    
    ranges = []
    for interval in lines[0].split(","):
        lower, upper = interval.split("-")[:2]
        ranges.append( (int(lower), int(upper)) )

    # solve_part1(ranges)
    solve_part2(ranges)


if __name__ == "__main__":
    main()
