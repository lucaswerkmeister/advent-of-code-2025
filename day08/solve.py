#!/usr/bin/env python3
import functools
import math
import operator
import sys

def process(file: str, num_connections: int) -> int:
    boxes = []
    with open(file) as f:
        while line := f.readline():
            x, y, z = line.strip().split(',')
            boxes.append((int(x), int(y), int(z)))
    boxes.sort()

    shortest_connections = []
    for i, box1 in enumerate(boxes):
        for box2 in boxes[i+1:]:
            pair = (box1, box2)
            distance = math.dist(box1, box2)
            if len(shortest_connections) < num_connections or distance < shortest_connections[-1][0]:
                shortest_connections.append((distance, pair))
                shortest_connections.sort()
                shortest_connections = shortest_connections[:num_connections]
    connections = {pair for distance, pair in shortest_connections}

    circuits = {}
    for pair in connections:
        box1, box2 = pair
        if box1 in circuits:
            circuits[box1].add(box2)
        elif box2 in circuits:
            circuit = circuits[box2]
            circuit.add(box1)
            del circuits[box2]
            circuits[box1] = circuit
        else:
            for other_box, circuit in circuits.items():
                if box1 in circuit or box2 in circuit:
                    circuit.add(box1)
                    circuit.add(box2)
                    if box1 < other_box:
                        del circuits[other_box]
                        circuits[box1] = circuit
                    break
            else:
                circuits[box1] = { box1, box2 }

    circuit_sizes = [len(circuit) for circuit in circuits.values()]
    circuit_sizes.sort(reverse=True)
    return functools.reduce(operator.mul, circuit_sizes[:3], 1)

for file in sys.argv[1:]:
    connections = {
        'input.sample': 10,
        'input': 1000,
    }[file]
    product = process(file, connections)
    print(f'{file}: the product of the three largest circuit sizes is {product}')
