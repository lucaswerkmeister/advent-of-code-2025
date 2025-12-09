#!/usr/bin/env python3
import math
import sys

for file in sys.argv[1:]:
    red_tiles = []
    with open(file) as f:
        while line := f.readline():
            x, y = line.strip().split(',')
            red_tiles.append((int(x), int(y)))

    max_area = 0
    for i, tile1 in enumerate(red_tiles):
        for tile2 in red_tiles[i+1:]:
            dx = abs(tile1[0] - tile2[0]) + 1
            dy = abs(tile1[1] - tile2[1]) + 1
            max_area = max(dx * dy, max_area)

    print(f'{file}: largest area is {max_area}')
