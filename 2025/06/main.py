
import sys
import re


def mul(factors: list[int]) -> int:
    total = 1
    for factor in factors:
        total *= factor
    return total


def solve_part1(operators: list[str], operands_list: list[list[int]]) -> None:
    total = 0
    for operator, operands in zip(operators, operands_list):
        if operator == "+":
            result = sum(operands)
        elif operator == "*":
            result = mul(operands)

        print(f"{operator} {result=}")
        total += result
        
    print("Solution:", total)


def main() -> None:
    inputFile = sys.argv[1] if len(sys.argv) >= 2 else "example.txt"
    with open(inputFile, "r") as fobj:
        lines = fobj.readlines()
        operators = list(lines.pop().strip().replace(" ", ""))
        
        number_cols: list[list[int]] = [ [] for _ in range(len(operators)) ]
        for line in lines:
            line = re.sub(r" +", " ", line).strip()

            for col, num in enumerate(line.split(" ")):
                number_cols[col].append(int(num))

    print(operators)
    print(number_cols)
    
    solve_part1(operators, number_cols)


if __name__ == "__main__":
    main()
