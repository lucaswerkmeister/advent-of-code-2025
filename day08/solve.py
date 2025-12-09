#!/usr/bin/env python3
import functools
import math
import operator
import sys

type Box = tuple[int, int, int]
type Pair = tuple[box, box]
type Distance = float
type Circuit = set[Box]
type Circuits = dict[Box, Circuit]
"""Invariant: the key of each Circuit is its *smallest* member Box."""

def process(file: str, num_connections: int) -> int:
    boxes: list[Box] = []
    with open(file) as f:
        while line := f.readline():
            x, y, z = line.strip().split(',')
            boxes.append((int(x), int(y), int(z)))
    boxes.sort()

    shortest_connections: list[tuple[Distance, Pair]] = []
    for i, box1 in enumerate(boxes):
        for box2 in boxes[i+1:]:
            pair = (box1, box2)
            distance = math.dist(box1, box2)
            if len(shortest_connections) < num_connections or distance < shortest_connections[-1][0]:
                shortest_connections.append((distance, pair))
                shortest_connections.sort()
                shortest_connections = shortest_connections[:num_connections]
    connections = {pair for distance, pair in shortest_connections}

    circuits: Circuits = {}
    for pair in connections:
        add_pair_to_circuits(pair, circuits)

    for box, circuit in circuits.items():
        assert box == min(circuit)

    assert len({box for circuit in circuits.values() for box in circuit}) == sum(len(circuit) for circuit in circuits.values()), \
        f'{len({box for circuit in circuits.values() for box in circuit})} boxes in all circuits but individual circuits sum to {sum(len(circuit) for circuit in circuits.values())}!'
    assert {box for pair in connections for box in pair} == {box for circuit in circuits.values() for box in circuit}, \
        f'{len({box for pair in connections for box in pair})} boxes in connections but {len({box for circuit in circuits.values() for box in circuit})} boxes in circuits!'

    circuit_sizes = [len(circuit) for circuit in circuits.values()]
    circuit_sizes.sort(reverse=True)
    return functools.reduce(operator.mul, circuit_sizes[:3], 1)

def add_pair_to_circuits(pair: Pair, circuits: Circuits) -> None:
    # check the invariant out of paranoia
    for box, circuit in circuits.items():
        assert box == min(circuit)
    box1, box2 = pair
    branch = None
    if box1 in circuits:
        branch = 'box1 in circuits'
        # update circuit
        circuit = circuits[box1]
        assert box1 in circuit
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
                    # save merged circuit
                    circuits[other_box] = circuit
                break
    elif box2 in circuits:
        branch = 'box2 in circuits'
        # update circuit, reindex with box1 as newly-smallest member
        circuit = circuits[box2]
        circuit.add(box1)
        assert box2 in circuit
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
                    # our circuit’s key is smaller, keep that index and drop the other
                    del circuits[other_box]
                else:
                    # other circuit’s key is smaller, drop ours
                    del circuits[box1]
                    # save merged circuit
                    circuits[other_box] = circuit
                break
    else:
        branch = 'else'
        for other_box, circuit in circuits.items():
            # find other circuit to add to
            if box1 in circuit or box2 in circuit:
                branch = 'box1 in circuit or box2 in circuit'
                # update circuit
                circuit.add(box1)
                circuit.add(box2)
                if box1 < other_box:
                    branch += ', box1 < other_box'
                    # reindex with box1 as newly-smallest member
                    del circuits[other_box]
                    circuits[box1] = circuit
                # find other circuit to potentially merge this one with
                for other_circuit_box, other_circuit in circuits.items():
                    if other_circuit == circuit:
                        continue
                    if box1 in other_circuit or box2 in other_circuit:
                        branch += ', box1 in other_circuit or box2 in other_circuit'
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
                            # save merged circuit
                            circuits[other_circuit_box] = circuit
                        break
                break
        else:
            branch = 'else else'
            # no other circuit contains this connection, add new circuit
            circuits[box1] = { box1, box2 }
    assert box1 in {box for circuit in circuits.values() for box in circuit}
    assert box2 in {box for circuit in circuits.values() for box in circuit}, \
        f'branch is {branch}'


for file in sys.argv[1:]:
    connections = {
        'input.sample': 10,
        'input': 1000,
    }[file]
    product = process(file, connections)
    print(f'{file}: the product of the three largest circuit sizes is {product}')
