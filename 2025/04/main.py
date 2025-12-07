
import sys
import os
import numpy as np


def print_field(width: int, height: int, field: np.array) -> None:
    os.system("cls")
    print(width, "x", height)
    for ir, row in enumerate(range(width)):
        print(f"{ir:>3}", end="  ")
        for col in range(height):
            print(field[row,col], end="")
        print("")


def solve_part1(width: int, height: int, field: np.array) -> None:
    print_field(width, height, field)

    padding = 1
    field_copy = np.copy(field)
    padded_field = np.pad(field, (padding,padding), mode="constant", constant_values=("-","-"))
    
    accesible_role_count = 0
    for row in range(width):
        for col in range(height):
            cell = field_copy[row,col]
            print(row, "x", col, "=", cell)
            if cell != "@":
                continue
            
            pad_row = row + padding
            pad_col = col + padding
            neighborhood = np.copy(padded_field[pad_row-1:pad_row+2, pad_col-1:pad_col+2])
            neighborhood[1,1] = "x"
            print_field(3, 3, neighborhood)
            
            stats = dict(zip(*np.unique(neighborhood, return_counts=True)))
            if stats.get("@", 0) < 4:
                accesible_role_count += 1
            
            print("")

    print_field(width, height, field)
    print(f"Solution: {accesible_role_count}")


def solve_part2(width: int, height: int, field: np.array) -> None:
    print_field(width, height, field)

    padding = 1
    total_accesible_role_count = 0
    while True:
        field_copy = np.copy(field)
        padded_field = np.pad(field, (padding,padding), mode="constant", constant_values=("-","-"))
        
        accesible_role_count = 0
        for row in range(width):
            for col in range(height):
                cell = field_copy[row,col]
                # print(row, "x", col, "=", cell)

                if cell == ".":
                    continue
                elif cell == "x":
                    field[row,col] = "."
                    continue
                
                pad_row = row + padding
                pad_col = col + padding
                neighborhood = np.copy(padded_field[pad_row-1:pad_row+2, pad_col-1:pad_col+2])
                neighborhood[1,1] = "x"
                # print_field(3, 3, neighborhood)
                
                stats = dict(zip(*np.unique(neighborhood, return_counts=True)))
                if stats.get("@", 0) < 4:
                    accesible_role_count += 1
                    field[row,col] = "x"
                
                # print("")
    
        print_field(width, height, field)
        # print(f"{accesible_role_count=}")
        
        total_accesible_role_count += accesible_role_count
        if accesible_role_count == 0:
            break
    
    print_field(width, height, field)
    print(f"Solution: {total_accesible_role_count}")


def main() -> None:    
    inputFile = sys.argv[1] if len(sys.argv) >= 2 else "example.txt"
    with open(inputFile, "r") as fobj:
        lines = [ list(line.strip()) for line in fobj.readlines() ]
        width = len(lines[0])
        height = len(lines)
        field = np.asarray(lines, dtype=object)

    # solve_part1(width, height, field)
    solve_part2(width, height, field)


if __name__ == "__main__":
    main()
