#!/usr/bin/env python3
from intervaltree import IntervalTree
import sys

for file in sys.argv[1:]:
    intervals = IntervalTree()
    with open(file) as f:
        while line := f.readline():
            line = line.strip()
            if not line:
                break
            first, dash, last = line.partition('-')
            begin = int(first)
            end = int(last) + 1  # ranges are inclusive, intervals exclusive
            intervals.addi(begin, end)

        fresh_available = 0
        while line := f.readline():
            line = line.strip()
            id = int(line)
            if intervals.at(id):
                fresh_available += 1
        
    print(f'{file}: {fresh_available} fresh IDs available')

    intervals.merge_overlaps()

    fresh_possible = 0
    for interval in intervals:
        fresh_possible += interval.end - interval.begin

    print(f'{file}: {fresh_possible} fresh IDs possible')
