#!/usr/bin/env python3
import sys

for file in sys.argv[1:]:
    with open(file) as f:
        lines = [line.strip() for line in f.readlines()]
    worlds = [[lines[0]]]

    for lineno in range(1, len(lines)):
        line = lines[lineno]
        new_worlds = []
        for world in worlds:
            previous_line = world[-1]
            processed_lines = None
            for index, char in enumerate(line):
                previous_char = previous_line[index]
                if previous_char not in {'|', 'S'}:
                    continue
                if char == '.':
                    processed_lines = [line[:index] + '|' + line[index+1:]]
                elif char == '^':
                    processed_lines = [
                        line[:index-1] + '|^.' + line[index+2:],
                        line[:index-1] + '.^|' + line[index+2:],
                    ]
                else:
                    raise ValueError(f"Unknown char '{char}': {line}")
                break  # only one beam can be active
            assert processed_lines is not None, f"no tachyon beam found in previous line: {line}"
            for processed_line in processed_lines:
                new_worlds.append(world + [processed_line])
        worlds = new_worlds
        print(f'line {lineno}/{len(lines)} done', file=sys.stderr)

    print(f'{file}: {len(worlds)} worlds')
