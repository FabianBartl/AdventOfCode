
import re, sys
from collections import namedtuple

Num = namedtuple("Num", ["pos", "val"])


def parse_line_p1(line:str) -> int:
    nums = re.findall(r"[0-9]", line)
    num = int("".join([ nums[0], nums[-1] ]))
    print(f"{line=} {num=}")
    return num


def findall_nums(line:str) -> list[Num]:
    num_names = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    num_digits = { str(n) for n in range(1, 10) }

    found_nums = []
    for ind, char in enumerate(line):
        # print(f"{ind=} {char=}")

        if char in num_digits:
            found_nums.append(Num(ind, int(char)))
            print(f"found digit: {char}")
            continue

        pos = 0
        while pos < len(num_names):
            name = num_names[pos]
            substr = line[ind:ind+len(name)]
            # print(f"{pos=} {name=} {substr=}")
            
            if name == substr:
                found_nums.append(Num(ind, pos+1))  # pos+1 is the numerical repr. of the written name 
                print(f"found number: {pos+1} = {name}")
                pos += len(name)
            else:
                pos += 1
    
    return found_nums


def parse_line_p2(line:str) -> int:
    print(f"\n{line}")
    nums = findall_nums(line)
    num = nums[0].val*10 + nums[-1].val

    print(f"{line=} {nums=} {num=}")
    return num


def run(input_file:str):
    total_sum_p1 = total_sum_p2 = 0
    with open(input_file, "r", encoding="utf-8") as file:
        for line in file.readlines():
            line = line.strip()
            # total_sum_p1 += parse_line_p1(line)
            total_sum_p2 += parse_line_p2(line)
    # print(f"{total_sum_p1=}")
    print(f"{total_sum_p2=}")


if __name__ == "__main__":
    run(sys.argv[1])
