
import sys
from dataclasses import dataclass
from typing import Optional

@dataclass
class Range:
    lower: int
    upper: int

def range_size(_range: Range) -> int:
    return _range.upper - _range.lower + 1


def solve_part1(ingredient_ranges: list[Range], ingredient_ids: list[int]) -> None:
    fresh_ids = 0
    
    for _id in ingredient_ids:
        for _range in ingredient_ranges:
            if _range.lower <= _id <= _range.upper:
                fresh_ids += 1
                break
    
    print("Solution:", fresh_ids)


def merge_two_ranges(first: Range, second: Range) -> tuple[ Range, Optional[Range] ]:
    print(f"merge {first} ({range_size(first)}) and {second} ({range_size(second)})")
    
    if first.lower <= second.lower <= first.upper and first.lower <= second.upper <= first.upper:
        return first, None
    elif second.lower <= first.lower <= second.upper and second.lower <= first.upper <= second.upper:
        return second, None
    
    if first.lower <= second.lower <= first.upper and first.upper <= second.upper:
        return Range(first.lower, second.upper), None
    elif second.lower <= first.lower <= second.upper and second.upper <= first.upper:
        return Range(second.lower, first.upper), None
    
    return first, second


def merge_all_ranges(_ranges: list[Range]) -> list[Range]:
    for iterind in range(len(_ranges)):
        base_range = _ranges.pop(0)
        print(f"\n\n{iterind}: {base_range} ({range_size(base_range)})")

        merge_happened = False
        curr_ind = 0
        while curr_ind < len(_ranges) or merge_happened:
            print(f"\ncompared range index {curr_ind}:")

            if curr_ind > len(_ranges) - 1:
                print("overflow, merged_happened")
                curr_ind = 0
                merge_happened = False
            
            curr_range = _ranges.pop(curr_ind)
            new_range1, new_range2 = merge_two_ranges(base_range, curr_range)
            if new_range2 is None:
                print(f"merged into {new_range1} ({range_size(new_range1)})")
                merge_happened = True
                base_range = new_range1
            else:
                print(f"no merge")
                _ranges.insert(curr_ind, curr_range)
                curr_ind += 1
        
        _ranges.append(base_range)
        print(_ranges)

    print(_ranges)
    return _ranges


def solve_part2(ingredient_ranges: list[Range]) -> None:
    fresh_id_count = 0
    
    ingredient_ranges_merged = merge_all_ranges(ingredient_ranges)
    for _range in ingredient_ranges_merged:
        fresh_id_count += range_size(_range)

    print("Solution:", fresh_id_count)


def main() -> None:
    ingredient_ranges: list[Range] = []
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
                ingredient_ranges.append( Range(lower=int(lower), upper=int(upper)) )

            elif mode == "ids":
                ingredient_ids.append(int(line))
    
    print(ingredient_ranges)
    print(ingredient_ids)

    # solve_part1(ingredient_ranges, ingredient_ids)
    solve_part2(ingredient_ranges)


if __name__ == "__main__":
    main()
