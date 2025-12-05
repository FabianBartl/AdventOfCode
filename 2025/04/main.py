
import sys
import numpy as np


def get_neighbors(row: int, col: int, field: np.array, fill: int, padding: int) -> np.array:
    padded = np.pad(field, (padding, padding), mode="constant", constant_values=(fill, fill))
    row += padding
    col += padding
    neighbors = padded[row-1:row+2, col-1:col+2]
    return neighbors


def solve_part1(width: int, height: int, field: np.array, symbols: dict) -> None:
    padding = 1
    field_copy = np.copy(field)
    padded_field = np.pad(field, (padding,padding), mode="constant", constant_values=(symbols["_"], symbols["_"]))
    
    count_enough_space = 0
    for col in range(width):
        for row in range(height):
            cell = field_copy[row,col]
            if cell == symbols["."]:
                continue
            
            pad_row = row + padding
            pad_col = col + padding
            neighborhood = padded_field[pad_row-1:pad_row+2, pad_col-1:pad_col+2]
            neighborhood[1,1] = symbols["x"]
            neighborhood[neighborhood == symbols["@"]] = symbols["#"]

            stats = dict(zip(*np.unique(neighborhood, return_counts=True)))
            print(stats)
            if stats[symbols["#"]] < 4:
                padded_field[pad_row-1:pad_row+2, pad_col-1:pad_col+2] = neighborhood
                count_enough_space += stats[symbols["x"]]

    print(count_enough_space)
    print(padded_field)
            
            
    #         cell_neighbors = get_neighbors(h, w, field, symbols["."], 1)
    #         cell_neighbors[1,2] = -1
    #         unique, counts = np.unique(cell_neighbors, return_counts=True)
    #         stats = dict(zip(unique, counts))
    #         print(f"({h}r, {w}c): {stats}")

    #         neighbor_count = stats[symbols["@"]]
    #         if neighbor_count < 4:
    #             count_enough_space += neighbor_count
    
    # print(f"Solution: {count_enough_space}")



def main() -> None:
    symbols = {".": 0, "@": 1, "_": -1, "x": 2, "#": 3}
    
    inputFile = sys.argv[1] if len(sys.argv) >= 2 else "example.txt"
    with open(inputFile, "r") as fobj:
        lines = [ list(map(lambda v: symbols[v], line.strip())) for line in fobj.readlines() ]
        width = len(lines[0])
        height = len(lines)
        field = np.asarray(lines)
    
    # field = np.arange(24).reshape(6,4)
    # width = 4
    # height = 6
    
    print(width, height)
    print(field, "\n")

    solve_part1(width, height, field, symbols)


if __name__ == "__main__":
    main()
