
import sys
import numpy as np
import matplotlib.pyplot as plt


def draw(boxes: list[np.array], cables: list[ tuple[int,int] ]) -> None:
    boxes_array = np.asarray(boxes)
    x = boxes_array[:, 0]
    y = boxes_array[:, 1]
    z = boxes_array[:, 2]
    # labels = np.array([ f"{i}={int(c[0])},{int(c[1])},{int(c[2])}" for i,c in enumerate(boxes) ], dtype=object)
    labels = np.array([ i for i,c in enumerate(boxes) ], dtype=object)

    fig = plt.figure()
    ax = fig.add_subplot(projection="3d")
    ax.scatter(x, y, z)
    for sx, sy, sz, label in zip(x, y, z, labels):
        ax.text(sx, sy, sz, label)
    
    for cable in cables:
        box1 = boxes_array[cable[0]]
        box2 = boxes_array[cable[1]]
        x = (box1[0], box2[0])
        y = (box1[1], box2[1])
        z = (box1[2], box2[2])
        ax.plot(x, y, z)

    plt.show()


def dist(v1: np.array, v2: np.array) -> float:
    return abs(v2 - v1)


def solve_part1(coords: list[np.array]) -> None:

    print("Solution:")


def main() -> None:
    inputFile = sys.argv[1] if len(sys.argv) >= 2 else "example.txt"
    with open(inputFile, "r") as fobj:
        coords = []
        for line in fobj.readlines():
            x, y, z = line.strip().split(",")
            coords.append(np.array( (float(x), float(y), float(z)) ))
    
    # example_connected = [
    #     (0, 19), (0, 7),
    #     (2, 13),
    # ]
    # draw(coords, example_connected)

    draw(coords, [])
    
    solve_part1(coords)


if __name__ == "__main__":
    main()
