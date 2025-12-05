
import sys

from colorama import Fore
from colorama import init as colorama_init
colorama_init(autoreset=True)
RESET = f"{Fore.RESET}"

Digit = int


def list_to_str(lst: list) -> str:
    return "".join(map(str, lst))


# return the first largest digit from a list and the position
def get_first_largest_num(subbank: list[Digit]) -> tuple[Digit, int]:
    found_max = -1
    max_ind = -1
    
    for ind, num in enumerate(subbank):
        if found_max == 9:      # assume the numbers are like expected only a single digit
            break
        if num > found_max:
            found_max = num
            max_ind = ind
    
    return found_max, max_ind


# 
def find_largest_num(bank: list[Digit], length: int) -> int:
    print(list_to_str(bank))
    
    found_digits = []
    found_positions = []
    left_ind = 0
    right_ind = length - 1

    while (len(found_digits) < length):
        
        subbank = bank[left_ind: None if right_ind == 0 else -right_ind ]
        print(" "*left_ind, list_to_str(subbank), sep="")
        print(" "*(left_ind-1), f"{Fore.CYAN}{left_ind}{RESET}", " "*(len(bank)-1-right_ind-left_ind), f"{Fore.MAGENTA}{right_ind}{RESET}", sep="")
        
        max_digit, digit_pos = get_first_largest_num(subbank)
        digit_pos += left_ind
        found_positions.append(digit_pos)
        found_digits.append(max_digit)
        print(" "*digit_pos, f"{Fore.GREEN}{max_digit}{RESET}", sep="")
        
        left_ind = digit_pos + 1
        right_ind = length - 1 - len(found_digits)

    found_positions_set = set(found_positions)
    for ind, digit in enumerate(bank):
        color = Fore.GREEN if ind in found_positions_set else ""
        print(f"{color}{digit}{RESET}", end="")
    print()

    return int("".join(map(str, found_digits)))


def solve_part2(banks: list[list[Digit]], length: int) -> None:
    print(f"{length=}")
    
    all_found_max: list[int] = []
    for bi, bank in enumerate(banks):
        print(f"\n{bi}:")
        found_max = find_largest_num(bank, length)
        all_found_max.append(found_max)
    
    print("\nSolution:", sum(all_found_max))


def main() -> None:
    inputFile = sys.argv[1] if len(sys.argv) > 1 else "example.txt"
    length = int(sys.argv[2]) if len(sys.argv) > 2 else 12
    with open(inputFile, "r") as fobj:
        banks = [ list(map(Digit, line.strip())) for line in fobj.readlines() ]
        
    solve_part2(banks, length)


if __name__ == "__main__":
    main()
