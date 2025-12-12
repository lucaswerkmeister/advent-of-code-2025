#!/usr/bin/env python3
import sys

from day11 import Machine, parse_machines, paths_from_to

for file in sys.argv[1:]:
    outwards, inwards = parse_machines(file)

    paths_from_you_to_out = paths_from_to(outwards, inwards, 'you', 'out')
    print(f'{file}: {paths_from_you_to_out} paths from {'you'!r} to {'out'!r}')
    if file == 'input.part1.sample':
        assert paths_from_you_to_out == 5
    elif file == 'input.part1.mine':
        assert paths_from_you_to_out == 5
