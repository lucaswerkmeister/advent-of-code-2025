#!/usr/bin/env python3
import sys

for file in sys.argv[1:]:
    with open(file) as f:
        lines = [line.strip() for line in f.readlines()]
    worlds = { lines[0]: 1 }

    for lineno in range(1, len(lines)):
        line = lines[lineno]
        beam_char = { 1: 'S' }.get(lineno, '|')
        new_worlds = {}
        for previous_line, its_worlds in worlds.items():
            beam_index = previous_line.index(beam_char)
            below_beam_char = line[beam_index]
            if below_beam_char == '.':
                processed_lines = [line[:beam_index] + '|' + line[beam_index+1:]]
            elif below_beam_char == '^':
                processed_lines = [
                    line[:beam_index-1] + '|^.' + line[beam_index+2:],
                    line[:beam_index-1] + '.^|' + line[beam_index+2:],
                ]
            else:
                raise ValueError(f"Unknown char '{char}': {line}")
            for processed_line in processed_lines:
                new_worlds[processed_line] = new_worlds.get(processed_line, 0) + its_worlds
        worlds = new_worlds
        print(f'line {lineno}/{len(lines)} done', file=sys.stderr)

    print(f'{file}: {sum(worlds.values())} worlds')
