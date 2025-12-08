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

    connections = set()
    for i in range(num_connections):
        if i % 10 == 0:
            print(f'{i}/{num_connections}')
        shortest_distance = math.inf
        shortest_pair = (None, None)
        for i, box1 in enumerate(boxes):
            for box2 in boxes[i+1:]:
                pair = (box1, box2)
                if pair in connections:
                    continue
                distance = math.dist(box1, box2)
                if distance < shortest_distance:
                    shortest_distance = distance
                    shortest_pair = pair
        connections.add(shortest_pair)
    # note: because we sorted the boxes and only test each pair once, each pair is also sorted

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
