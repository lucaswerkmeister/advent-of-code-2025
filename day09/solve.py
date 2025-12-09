#!/usr/bin/env python3
import math
import sys

for file in sys.argv[1:]:
    red_tiles = []
    green_horizontals = {}
    green_verticals = {}
    with open(file) as f:
        previous_x = None
        previous_y = None
        while line := f.readline():
            x, y = line.strip().split(',')
            x, y = int(x), int(y)
            red_tiles.append((x, y))
            if previous_x is not None:
                if x == previous_x:
                    assert y != previous_y
                    y1, y2 = sorted([y, previous_y])
                    green_verticals.setdefault(x, []).append((y1, y2))
                else:
                    assert y == previous_y
                    x1, x2 = sorted([x, previous_x])
                    green_horizontals.setdefault(y, []).append((x1, x2))
            previous_x, previous_y = x, y

    max_part1_area = 0
    max_part2_area = 0
    for i, tile1 in enumerate(red_tiles):
        for tile2 in red_tiles[i+1:]:
            x1, x2 = sorted([tile1[0], tile2[0]])
            y1, y2 = sorted([tile1[1], tile2[1]])
            dx = x2 - x1 + 1
            dy = y2 - y1 + 1
            area = dx * dy
            if area <= max_part2_area:
                continue
            if area > max_part1_area:
                max_part1_area = area
            if dx <= 2 or dy <= 2:
                max_part2_area = area
                print(f'{max_part2_area=} because {dx=}<=2 or {dy=}<=2')
                continue
            def is_legal_rectangle():
                for x in range(x1 + 1, x2):
                    for y in range(y1 + 1, y2):
                        x_area = 'outside'  # one of 'outside', 'upper edge', 'lower edge', 'inside'
                        for x_incr in range(x):
                            for v in green_verticals.get(x_incr, []):
                                v_y1, v_y2 = v
                                if not v_y1 <= y <= v_y2:
                                    continue
                                if x_area == 'outside':
                                    if y == v_y1:
                                        x_area = 'upper edge'
                                    elif y == v_y2:
                                        x_area = 'lower edge'
                                    else:
                                        x_area = 'inside'
                                elif x_area == 'upper edge':
                                    if y == v_y1:
                                        x_area = 'outside'
                                    elif y == v_y2:
                                        x_area = 'inside'
                                    else:
                                        raise ValueError(f'Unaligned edge? {x_incr=}, {v=}')
                                elif x_area == 'lower edge':
                                    if y == v_y1:
                                        x_area = 'inside'
                                    elif y == v_y2:
                                        x_area = 'outside'
                                    else:
                                        raise ValueError(f'Unaligned edge? {x_incr=}, {v=}')
                                else:
                                    assert x_area == 'inside'
                                    if y == v_y1:
                                        x_area = 'lower edge'
                                    elif y == v_y2:
                                        x_area = 'upper edge'
                                    else:
                                        x_area = 'outside'
                        if x_area == 'outside':
                            return False
                        y_area = 'outside'  # one of 'outside', 'left edge', 'right edge', 'inside'
                        for y_incr in range(y):
                            for h in green_horizontals.get(y_incr, []):
                                h_x1, h_x2 = h
                                if not h_x1 <= x <= h_x2:
                                    continue
                                if y_area == 'outside':
                                    if x == h_x1:
                                        y_area = 'left edge'
                                    elif x == h_x2:
                                        y_area = 'right edge'
                                    else:
                                        y_area = 'inside'
                                elif y_area == 'left edge':
                                    if x == h_x1:
                                        y_area = 'outside'
                                    elif x == h_x2:
                                        y_area = 'inside'
                                    else:
                                        raise ValueError(f'Unaligned edge? {y_incr=}, {h=}')
                                elif y_area == 'right edge':
                                    if x == h_x1:
                                        y_area = 'inside'
                                    elif x == h_x2:
                                        y_area = 'outside'
                                    else:
                                        raise ValueError(f'Unaligned edge? {y_incr=}, {h=}')
                                else:
                                    assert y_area == 'inside'
                                    if x == h_x1:
                                        y_area = 'right edge'
                                    elif x == h_x2:
                                        y_area = 'left edge'
                                    else:
                                        y_area = 'outside'
                        if y_area == 'outside':
                            return False
                return True
            if is_legal_rectangle():
                max_part2_area = area
                print(f'{max_part2_area=} because legal rectangle: {tile1=}, {tile2=}')

    print(f'{file}: largest possible area is {max_part1_area}')
    print(f'{file}: largest allowed area is {max_part2_area}')
