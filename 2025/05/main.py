
import sys
import numpy as np


def solve_part1(ingredient_ranges: list[tuple[int,int]], ingredient_ids: list[int]) -> None:
    fresh_ids = 0
    
    for _id in ingredient_ids:
        for _range in ingredient_ranges:
            if _range[0] <= _id <= _range[1]:
                fresh_ids += 1
                break
    
    print("Solution:", fresh_ids)


# def solve_part2(ingredient_ranges: list[tuple[int,int]]) -> None:
#     fresh_id_count = 0
    
#     for _range in ingredient_ranges:
#         range_size = _range[1] - _range[0] + 1
#         fresh_id_count += range_size
    
#     print("Solution:", fresh_id_count)


def main() -> None:
    ingredient_ranges: list[tuple[int,int]] = []
    ingredient_ids: list[int] = []
    
    mode = "ranges"
    inputFile = sys.argv[1] if len(sys.argv) >= 2 else "example.txt"
    with open(inputFile, "r") as fobj:
        for line in fobj.readlines():
            line = line.strip()

            if line == "" and mode == "ranges":
                mode = "ids"
                continue
            
            if mode == "ranges":
                lower, upper = line.split("-")
                ingredient_ranges.append( (int(lower), int(upper)) )

            elif mode == "ids":
                ingredient_ids.append(int(line))
    
    print(ingredient_ranges)
    print(ingredient_ids)

    solve_part1(ingredient_ranges, ingredient_ids)
    # solve_part2(ingredient_ranges)


if __name__ == "__main__":
    main()
