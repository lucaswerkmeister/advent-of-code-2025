#!/usr/bin/env python3
from functools import reduce
import sys
from typing import Literal

type Diagram = list[Literal[0, 1]]
type Button = list[Literal[0, 1]]
type JoltageReq = list[int]
type Machine = tuple[Diagram, list[Button], JoltageReq]

def parse_diagram(diagram: str) -> Diagram:
    assert diagram.startswith('[') and diagram.endswith(']')
    return [1 if c == '#' else 0 for c in diagram[1:-1]]

assert parse_diagram('[.###.#]') == [0, 1, 1, 1, 0, 1]

def parse_button(button: str, diagram: Diagram) -> Button:
    assert button.startswith('(') and button.endswith(')')
    nums = { int(num) for num in button[1:-1].split(',') }
    return [1 if i in nums else 0 for i in range(len(diagram))]

assert parse_button('(0,3,4)', [0, 1, 1, 1, 0, 1]) == [1, 0, 0, 1, 1, 0]

def parse_joltage_req(joltage_req: str, diagram: Diagram) -> JoltageReq:
    assert joltage_req.startswith('{') and joltage_req.endswith('}')
    joltages = [int(joltage) for joltage in joltage_req[1:-1].split(',')]
    assert len(joltages) == len(diagram)
    return joltages

assert parse_joltage_req('{10,11,11,5,10,5}', [0, 1, 1, 1, 0, 1]) == [10, 11, 11, 5, 10, 5]

def xor_lists(*lists: list[list[int]]) -> list[int]:
    return [reduce(lambda i1, i2: i1 ^ i2, elems, 0) for elems in zip(*lists)]

assert xor_lists([0, 1, 0, 1], [0, 0, 1, 1]) == [0, 1, 1, 0]

def add_lists(*lists: list[list[int]]) -> list[int]:
    return [sum(elems) for elems in zip(*lists)]

assert add_lists([1, 2, 3], [2, 4, 1]) == [3, 6, 4]

def needed_buttons(machine: Machine) -> int:
    diagram, buttons, _ = machine
    if sum(diagram) == 0:
        return 0

    for button in buttons:
        if button == diagram:
            return 1

    for i, button1 in enumerate(buttons):
        for button2 in buttons[i+1:]:
            if xor_lists(button1, button2) == diagram:
                return 2

    for i, button1 in enumerate(buttons):
        for j, button2 in enumerate(buttons[i+1:]):
            for button3 in buttons[j+1:]:
                if xor_lists(button1, button2, button3) == diagram:
                    return 3

    for i, button1 in enumerate(buttons):
        for j, button2 in enumerate(buttons[i+1:]):
            for k, button3 in enumerate(buttons[j+1:]):
                for button4 in buttons[k+1:]:
                    if xor_lists(button1, button2, button3, button4) == diagram:
                        return 4

    for i, button1 in enumerate(buttons):
        for j, button2 in enumerate(buttons[i+1:]):
            for k, button3 in enumerate(buttons[j+1:]):
                for l, button4 in enumerate(buttons[k+1:]):
                    for button5 in buttons[l+1:]:
                        if xor_lists(button1, button2, button3, button4, button5) == diagram:
                            return 5

    for i, button1 in enumerate(buttons):
        for j, button2 in enumerate(buttons[i+1:]):
            for k, button3 in enumerate(buttons[j+1:]):
                for l, button4 in enumerate(buttons[k+1:]):
                    for m, button5 in enumerate(buttons[l+1:]):
                        for button6 in buttons[m+1:]:
                            if xor_lists(button1, button2, button3, button4, button5, button6) == diagram:
                                return 6

    for i, button1 in enumerate(buttons):
        for j, button2 in enumerate(buttons[i+1:]):
            for k, button3 in enumerate(buttons[j+1:]):
                for l, button4 in enumerate(buttons[k+1:]):
                    for m, button5 in enumerate(buttons[l+1:]):
                        for n, button6 in enumerate(buttons[m+1:]):
                            for button7 in buttons[n+1:]:
                                if xor_lists(button1, button2, button3, button4, button5, button6, button7) == diagram:
                                    return 7

    for i, button1 in enumerate(buttons):
        for j, button2 in enumerate(buttons[i+1:]):
            for k, button3 in enumerate(buttons[j+1:]):
                for l, button4 in enumerate(buttons[k+1:]):
                    for m, button5 in enumerate(buttons[l+1:]):
                        for n, button6 in enumerate(buttons[m+1:]):
                            for o, button7 in enumerate(buttons[n+1:]):
                                for button8 in buttons[o+1:]:
                                    if xor_lists(button1, button2, button3, button4, button5, button6, button7, button8) == diagram:
                                        return 8

    raise ValueError(f'Needs more than 8 buttons: {machine}')

for file in sys.argv[1:]:
    machines: list[Machine] = []
    with open(file) as f:
        for line in f:
            parts = line.strip().split(' ')
            diagram_str, rest = parts[0], parts[1:]
            buttons_str, joltage_req_str = rest[:-1], rest[-1]
            diagram = parse_diagram(diagram_str)
            buttons = [parse_button(button_str, diagram) for button_str in buttons_str]
            joltage_req = parse_joltage_req(joltage_req_str, diagram)
            machines.append((diagram, buttons, joltage_req))

    total_presses = 0
    for machine in machines:
        total_presses += needed_buttons(machine)

    print(f'{file}: {total_presses} presses needed')
