#!/usr/bin/env python3
import sys

type Machine = str

def paths_from_to(
        outwards: dict[Machine, list[Machine]],
        inwards: dict[Machine, list[Machine]],
        src: Machine,  # `from` is a keyword :<
        dst: Machine,
) -> int:
    paths_to_dst: dict[Machine, int] = { dst: 1 }
    worklist = [dst]
    downstreams: dict[Machine, set[Machine]] = {}
    cyclic: set[Machine] = set()
    while worklist:
        machine, worklist = worklist[0], worklist[1:]
        if machine in cyclic:
            continue
        machine_downstreams = downstreams.setdefault(machine, set())
        for other in inwards.get(machine, []):
            other_downstreams = downstreams.setdefault(other, set())
            if other in other_downstreams:
                cyclic.add(other)
                continue
            other_downstreams.add(machine)
            other_downstreams.update(machine_downstreams)
            paths = sum(paths_to_dst.get(sibling, 0) for sibling in outwards[other])
            if paths != paths_to_dst.get(other):
                paths_to_dst[other] = paths
                worklist.append(other)

    return paths_to_dst[src]

for file in sys.argv[1:]:
    outwards: dict[Machine, list[Machine]] = {}
    with open(file) as f:
        for line in f:
            machine, others = line.strip().split(': ')
            outwards[machine] = others.split(' ')

    inwards: dict[Machine, list[Machine]] = {}
    for machine, others in outwards.items():
        for other in others:
            inwards.setdefault(other, []).append(machine)

    paths_from_you_to_out = paths_from_to(outwards, inwards, 'you', 'out')
    print(f'{file}: {paths_from_you_to_out} paths from {'you'!r} to {'out'!r}')
    if file == 'input.sample':
        assert paths_from_you_to_out == 5
    elif file == 'input.mine':
        assert paths_from_you_to_out == 5
