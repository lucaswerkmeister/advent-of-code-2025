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

    # circuits is a dict of sets; each set’s key is its smallest member
    circuits = {}
    for pair in connections:
        box1, box2 = pair
        if box1 in circuits:
            # update circuit
            circuit = circuits[box1]
            circuit.add(box2)
            # find other circuit to potentially merge this one with
            for other_box, other_circuit in circuits.items():
                if other_box == box1:
                    continue
                if box2 in other_circuit:
                    # merge them
                    circuit.update(other_circuit)
                    if box1 < other_box:
                        # our circuit’s key is smaller, keep that index and drop the other
                        del circuits[other_box]
                    else:
                        # other circuit’s key is smaller, drop ours
                        del circuits[box1]
                    break
        elif box2 in circuits:
            # update circuit, reindex with box1 as newly-smallest member
            circuit = circuits[box2]
            circuit.add(box1)
            del circuits[box2]
            circuits[box1] = circuit
            # find other circuit to potentially merge this one with
            for other_box, other_circuit in circuits.items():
                if other_box == box1:
                    continue
                if box1 in other_circuit:
                    # merge them
                    circuit.update(other_circuit)
                    if box1 < other_box:
                        # our circuit’s key is smaller, keep that index and drop the oher
                        del circuits[other_box]
                    else:
                        # other circuit’s key is smaller, drop ours
                        del circuits[box1]
                    break
        else:
            for other_box, circuit in circuits.items():
                # find other circuit to add to
                if box1 in circuit or box2 in circuit:
                    # update circuit
                    circuit.add(box1)
                    circuit.add(box2)
                    if box1 < other_box:
                        # reindex with box1 as newly-smallest member
                        del circuits[other_box]
                        circuits[box1] = circuit
                    # find other circuit to potentially merge this one with
                    for other_circuit_box, other_circuit in circuits.items():
                        if other_circuit == circuit:
                            continue
                        if box1 in other_circuit or box2 in other_circuit:
                            # merge them
                            circuit.update(other_circuit)
                            if box1 < other_circuit_box or other_box < other_circuit_box:
                                # our circuit’s key is smaller, keep that index and drop the other
                                del circuits[other_circuit_box]
                            else:
                                # other circuit’s key is smaller, drop whichever was ours
                                if box1 < other_box:
                                    del circuits[box1]
                                else:
                                    del circuits[other_box]
                            break
                    break
            else:
                # no other circuit contains this connection, add new circuit
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
