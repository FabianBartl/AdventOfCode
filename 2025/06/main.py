
import sys
import re
import numpy as np


def mul(factors: list[int]) -> int:
    total = 1
    for factor in factors:
        total *= factor
    return total


def calculate_solution(operators: list[str], operands_list: list[list[int]]) -> int:
    total = 0
    for operator, operands in zip(operators, operands_list):
        if operator == "+":
            result = sum(operands)
        elif operator == "*":
            result = mul(operands)

        print(f"{operator} {result=}")
        total += result
    return total


def solve_part1(lines: list[str]) -> None:
    # parse the file
    operators = list(lines.pop().strip().replace(" ", ""))
    
    number_cols: list[list[int]] = [ [] for _ in range(len(operators)) ]
    for line in lines:
        line = re.sub(r" +", " ", line).strip()

        for col, num in enumerate(line.split(" ")):
            number_cols[col].append(int(num))

    print(operators)
    print(number_cols)

    # calculate solution
    res = calculate_solution(operators, number_cols)
    print("Solution:", res)


def solve_part2(lines: list[str]) -> None:
    # parse the file
    operators = list(lines.pop().strip().replace(" ", ""))
    operands_count = len(lines)
    
    lines_matrix: list[list[str]] = [ list(line.strip("\n")) for line in lines ]
    lines_array = np.asarray(lines_matrix, dtype=object)
    print(lines_array, "\n")
    
    # rotate and flip to read digits from left to right and group per operation
    lines_array = np.rot90(lines_array)
    lines_array = np.rot90(lines_array)
    lines_array = np.rot90(lines_array)
    lines_array = np.fliplr(lines_array)
    print(lines_array)
    
    # convert transformed matrix back to groups of integers per operation
    blocks: list[list[int]] = [ [] for _ in range(len(operators)) ]
    lines_list: list[list[int]] = lines_array.tolist()
    
    ind = 0
    while len(lines_list) > 0:
        element = "".join(lines_list.pop(0)).strip()
        if element == "":
            ind += 1
            continue
        blocks[ind].append(int(element))
    
    print(blocks)
    
    # calculate solution
    res = calculate_solution(operators, blocks)
    print("Solution:", res)


def main() -> None:
    inputFile = sys.argv[1] if len(sys.argv) >= 2 else "example.txt"
    with open(inputFile, "r") as fobj:
        lines = fobj.readlines()
    
    # solve_part1(lines)
    solve_part2(lines)


if __name__ == "__main__":
    main()
