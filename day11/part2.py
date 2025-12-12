#!/usr/bin/env python3
import sys

from day11 import Machine, parse_machines, paths_from_to

for file in sys.argv[1:]:
    outwards, inwards = parse_machines(file)

    paths_via_dac_fft = paths_from_to(outwards, inwards, 'svr', 'dac') * \
        paths_from_to(outwards, inwards, 'dac', 'fft') * \
        paths_from_to(outwards, inwards, 'fft', 'out')
    paths_via_fft_dac = paths_from_to(outwards, inwards, 'svr', 'fft') * \
        paths_from_to(outwards, inwards, 'fft', 'dac') * \
        paths_from_to(outwards, inwards, 'dac', 'out')

    assert paths_via_dac_fft * paths_via_fft_dac == 0, \
        'If there are paths via dac->fft and via fft->dac, there must be a cycle and the only possible answer is ∞'

    paths_via_both_either_order = paths_via_dac_fft + paths_via_fft_dac
    print(f'{file}: {paths_via_both_either_order} paths from {'svr'!r} to {'fft'!r} via {'dac'!r} and {'fft'!r} in any order')
    if file == 'input.part2.sample':
        assert paths_via_both_either_order == 2
