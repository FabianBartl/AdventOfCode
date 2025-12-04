
import sys
import re
from tqdm import tqdm

def solve_part1(banks: list[list[int]]) -> None:
    all_found_max = []
    
    for ind, bank in enumerate(banks):
        bank: list[int]
        print(f"\n{ind}: {bank}")
        
        found_max = 0
        for split_ind in range(1, len(bank)):
            first_part = bank[:split_ind]
            last_part = bank[split_ind:]
            print(f"{first_part} | {last_part}")
            
            first_max = max(first_part)
            last_max = max(last_part)
            
            current = first_max*10 + last_max
            if current > found_max:
                found_max = current
                print(f"found new max: {current}")
        
        print(f"{found_max=}")
        all_found_max.append(found_max)
    
    print(f"Solution:", sum(all_found_max))


def solve_part2(banks: list[list[int]]) -> None:
    # start_joltage = 100_000_000_000
    # end_joltage   = 999_999_999_999
    # start_joltage = 10_000_000
    # end_joltage   = 99_999_999
    start_joltage = 100_000
    end_joltage   = 999_999

    all_found_max = []
    for ind, bank in enumerate(banks):
        banktext = "".join(map(str, bank))
        print(f"\n{ind}: {banktext}")
        
        found_max = 0
        for joltage in range(end_joltage, start_joltage-1, -1):
            
            joltagetext = str(joltage)
            if 0 in set(joltagetext):
                continue
            pattern = r"\d*".join(list(joltagetext))
            
            if (matched := re.search(pattern, banktext)) is not None:
                found_max = joltage
                print(f"found match for {joltage}")
                break
        
        all_found_max.append(found_max)
    print(f"Solution:", sum(all_found_max))


def main() -> None:
    inputFile = sys.argv[1] if len(sys.argv) >= 2 else "example.txt"
    inputData = []
    with open(inputFile, "r") as fobj:
        banks = [ list(map(int, line.strip())) for line in fobj.readlines() ]
    
    # solve_part1(banks)
    solve_part2(banks)


if __name__ == "__main__":
    main()
