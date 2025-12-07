#!/usr/bin/env python3
import sys

for file in sys.argv[1:]:
    with open(file) as f:
        lines = [line.strip() for line in f.readlines()]
    processed_lines = [lines[0]]

    beam_splits = 0
    for lineno in range(1, len(lines)):
        line = lines[lineno]
        previous_line = processed_lines[lineno-1]
        processed_line = line
        for index, char in enumerate(line):
            previous_char = previous_line[index]
            if previous_char not in {'|', 'S'}:
                continue
            if char == '.':
                processed_line = processed_line[:index] + '|' + processed_line[index+1:]
            elif char == '^':
                processed_line = processed_line[:index-1] + '|^|' + processed_line[index+2:]
                beam_splits += 1
        processed_lines.append(processed_line)

    print('\n'.join(processed_lines), file=sys.stderr)
    print(f'{file}: {beam_splits} beam splits')
