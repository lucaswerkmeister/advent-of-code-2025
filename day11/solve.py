#!/usr/bin/env python3
import sys

type Machine = str

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

    paths_to_out: dict[Machine, int] = { 'out': 1 }
    worklist = ['out']
    while worklist:
        machine, worklist = worklist[0], worklist[1:]
        for other in inwards.get(machine, []):
            paths_to_out[other] = sum(paths_to_out.get(sibling, 0) for sibling in outwards[other])
            worklist.append(other)

    paths_from_you_to_out = paths_to_out['you']
    print(f'{file}: {paths_from_you_to_out} paths from {'you'!r} to {'out'!r}')
    if file == 'input.sample':
        assert paths_from_you_to_out == 5
