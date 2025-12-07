
import sys
import os
import numpy as np


def print_field(row_count: int, col_count: int, field: np.array) -> None:
    os.system("cls")
    print(row_count, "x", col_count)
    for row_ind in range(row_count):
        print(f"{row_ind:>3}", end="  ")
        for col in range(col_count):
            print(field[row_ind, col], end="")
        print("")


def solve_part1(row_count: int, col_count: int, field: np.array) -> None:
    # simulate
    beam_splittings = 0
    new_field = np.copy(field)
    for iterstep in range(row_count):
        print(f"\n{iterstep}: {beam_splittings=}")
        print_field(row_count, col_count, field)
        
        for row_ind in range(row_count-1):
            for col_ind in range(col_count):

                ind_curr = (row_ind, col_ind)
                ind_below = (row_ind+1, col_ind)
                cell = field[ind_curr]
                cell_below = field[ind_below]

                if cell == ".":
                    pass
                elif cell == "^":
                    new_field[ind_curr] = cell
                
                elif cell == "S":
                    new_field[ind_curr] = "X"
                    new_field[ind_below] = "|"
                
                elif cell == "|":
                    new_field[ind_curr] = "|"
                    if cell_below == ".":
                        new_field[ind_below] = "|"

                    elif cell_below == "^":
                        ind_below_left = (row_ind+1, col_ind-1)
                        ind_below_right = (row_ind+1, col_ind+1)

                        new_field[ind_below_left] = "|"
                        new_field[ind_below_right] = "|"
                        
                        if field[ind_below_left] != "|":
                            beam_splittings += 1
                        if new_field[ind_below_right] != "|":
                            beam_splittings += 1

        field = np.copy(new_field)

    print("Solution:", beam_splittings)


def main() -> None:
    inputFile = sys.argv[1] if len(sys.argv) >= 2 else "example.txt"
    with open(inputFile, "r") as fobj:
        lines = [ list(line.strip()) for line in fobj.readlines() ]
        
    row_count = len(lines)
    col_count = len(lines[0])
    field = np.asarray(lines, dtype=object)
    print_field(row_count, col_count, field)
    
    solve_part1(row_count, col_count, field)


if __name__ == "__main__":
    main()
