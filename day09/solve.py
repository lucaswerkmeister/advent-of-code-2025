#!/usr/bin/env python3
import math
import sys

OUTSIDE = 0
INSIDE = 1
UPPER_EDGE = 2
LOWER_EDGE = 3
LEFT_EDGE = 4
RIGHT_EDGE = 5

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
    done = 0
    total = len(red_tiles) * (len(red_tiles) - 1) // 2
    for i, tile1 in enumerate(red_tiles):
        for tile2 in red_tiles[i+1:]:
            done += 1
            print(f'{done}/{total}')
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
                print(f'is_legal_rectangle: x∈({x1},{x2}), y∈({y1},{y2})')
                for x in range(x1 + 1, x2):
                    for y in range(y1 + 1, y2):
                        if x not in green_verticals and y not in green_horizontals:
                            continue
                        x_area = OUTSIDE  # one of OUTSIDE, UPPER_EDGE, LOWER_EDGE, INSIDE
                        for x_incr in range(x):
                            for v in green_verticals.get(x_incr, []):
                                v_y1, v_y2 = v
                                if not v_y1 <= y <= v_y2:
                                    continue
                                if x_area == OUTSIDE:
                                    if y == v_y1:
                                        x_area = UPPER_EDGE
                                    elif y == v_y2:
                                        x_area = LOWER_EDGE
                                    else:
                                        x_area = INSIDE
                                elif x_area == UPPER_EDGE:
                                    if y == v_y1:
                                        x_area = OUTSIDE
                                    elif y == v_y2:
                                        x_area = INSIDE
                                    else:
                                        raise ValueError(f'Unaligned edge? {x_incr=}, {v=}')
                                elif x_area == LOWER_EDGE:
                                    if y == v_y1:
                                        x_area = INSIDE
                                    elif y == v_y2:
                                        x_area = OUTSIDE
                                    else:
                                        raise ValueError(f'Unaligned edge? {x_incr=}, {v=}')
                                else:
                                    assert x_area == INSIDE
                                    if y == v_y1:
                                        x_area = LOWER_EDGE
                                    elif y == v_y2:
                                        x_area = UPPER_EDGE
                                    else:
                                        x_area = OUTSIDE
                        if x_area == OUTSIDE:
                            return False
                        y_area = OUTSIDE  # one of OUTSIDE, LEFT_EDGE, RIGHT_EDGE, INSIDE
                        for y_incr in range(y):
                            for h in green_horizontals.get(y_incr, []):
                                h_x1, h_x2 = h
                                if not h_x1 <= x <= h_x2:
                                    continue
                                if y_area == OUTSIDE:
                                    if x == h_x1:
                                        y_area = LEFT_EDGE
                                    elif x == h_x2:
                                        y_area = RIGHT_EDGE
                                    else:
                                        y_area = INSIDE
                                elif y_area == LEFT_EDGE:
                                    if x == h_x1:
                                        y_area = OUTSIDE
                                    elif x == h_x2:
                                        y_area = INSIDE
                                    else:
                                        raise ValueError(f'Unaligned edge? {y_incr=}, {h=}')
                                elif y_area == RIGHT_EDGE:
                                    if x == h_x1:
                                        y_area = INSIDE
                                    elif x == h_x2:
                                        y_area = OUTSIDE
                                    else:
                                        raise ValueError(f'Unaligned edge? {y_incr=}, {h=}')
                                else:
                                    assert y_area == INSIDE
                                    if x == h_x1:
                                        y_area = RIGHT_EDGE
                                    elif x == h_x2:
                                        y_area = LEFT_EDGE
                                    else:
                                        y_area = OUTSIDE
                        if y_area == OUTSIDE:
                            return False
                return True
            if is_legal_rectangle():
                max_part2_area = area
                print(f'{max_part2_area=} because legal rectangle: {tile1=}, {tile2=}')

    print(f'{file}: largest possible area is {max_part1_area}')
    print(f'{file}: largest allowed area is {max_part2_area}')
    if file == 'input.sample':
        assert max_part1_area == 50
        assert max_part2_area == 24
