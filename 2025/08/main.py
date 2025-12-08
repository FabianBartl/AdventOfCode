
import sys
import numpy as np
import matplotlib.pyplot as plt


# init the global plot for live updates
FIG = plt.figure()
AX = FIG.add_subplot(projection="3d")
plt.show(block=False)
plt.get_current_fig_manager().full_screen_toggle()


def euclidian_dist(v1: np.array, v2: np.array) -> float:
    return np.linalg.norm(v2 - v1)


# returns the circuit index where the node is part of
def get_circuit_ind(search_node_ind: np.array, circuits: list[ set[int] ]) -> int:
    for circuit_ind, nodes_set in enumerate(circuits):
        if search_node_ind in nodes_set:
            return circuit_ind
    return None


# naive linear nearest neighbor search
def nns(start_node_ind: np.array, nodes: list[np.array]) -> tuple[int, float]:
    min_dist = float("inf")
    min_dist_node_ind = None
    start_node = nodes[start_node_ind]
    for node_ind, node in enumerate(nodes):
        if start_node_ind == node_ind:
            continue
        dist = euclidian_dist(start_node, node)
        if dist < min_dist:
            min_dist = dist
            min_dist_node_ind = node_ind
    return (min_dist_node_ind, min_dist)


def draw(boxes: list[np.array], cables: set[ tuple[int,int] ]) -> None:
    boxes_array = np.asarray(boxes)
    x = boxes_array[:, 0]
    y = boxes_array[:, 1]
    z = boxes_array[:, 2]
    labels = np.array([ f"{i}={int(c[0])},{int(c[1])},{int(c[2])}" for i,c in enumerate(boxes) ], dtype=object)
    # labels = np.array([ i for i,c in enumerate(boxes) ], dtype=object)

    AX.cla()
    AX.clabel()
    
    AX.scatter(x, y, z)
    for sx, sy, sz, label in zip(x, y, z, labels):
        AX.text(sx, sy, sz, label)
    
    for cable in cables:
        box1 = boxes_array[cable[0]]
        box2 = boxes_array[cable[1]]
        x = (box1[0], box2[0])
        y = (box1[1], box2[1])
        z = (box1[2], box2[2])
        AX.plot(x, y, z)

    FIG.canvas.draw()
    FIG.canvas.flush_events()


def solve_part1(boxes: list[np.array]) -> None:
    boxes_count = len(boxes)
    connected_boxes: set[int] = set()
    cables: set[ tuple[int,int] ] = set()
    circuits: list[ set[int] ] = []
    
    box_ind = -1
    while len(connected_boxes) < boxes_count:
        box_ind += 1
        if box_ind >= boxes_count:
            box_ind = 0

        # skip, if box already part of a circuit
        box_circuit_ind = get_circuit_ind(box_ind, circuits)
        if box_circuit_ind is not None:
            continue
        
        # get nearest neighbor
        neighbor_ind, dist = nns(box_ind, boxes)
        
        # add box to circuit of neighbor or create new circuit of neighbor and box
        neighbor_circuit_ind = get_circuit_ind(neighbor_ind, circuits)
        if neighbor_circuit_ind is not None:
            circuits[neighbor_circuit_ind].add(box_ind)
        else:
            circuits.append({box_ind, neighbor_circuit_ind})

        # connect box and neighbor by a cable
        cables.add( (box_ind, neighbor_ind) )
        connected_boxes.add(box_ind)
        connected_boxes.add(neighbor_ind)

        draw(boxes, cables)
        plt.waitforbuttonpress()
        # plt.pause(1e-6)

    draw(boxes, cables)
    plt.show(block=True)

    print("Solution:")


def main() -> None:
    inputFile = sys.argv[1] if len(sys.argv) >= 2 else "example.txt"
    with open(inputFile, "r") as fobj:
        coords = []
        for line in fobj.readlines():
            x, y, z = line.strip().split(",")
            coords.append(np.array( (float(x), float(y), float(z)) ))
    
    # example_connected = {
    #     (0, 19), (0, 7),
    #     (2, 13),
    # }
    # draw(coords, example_connected)
    # plt.show(block=True)

    solve_part1(coords)


if __name__ == "__main__":
    main()
