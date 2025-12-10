#!/usr/bin/env python3
import sys

type Diagram = int  # binary encoded
type Button = int  # binary encoded
type JoltageReq = set[int]
type Machine = tuple[Diagram, list[Button], JoltageReq]

def parse_diagram(diagram: str) -> Diagram:
    assert diagram.startswith('[') and diagram.endswith(']')
    return sum(2**i for i, c in enumerate(diagram[1:-1]) if c == '#')

assert parse_diagram('[.###.#]') == 46  # 2 + 4 + 8 + 32

def parse_button(button: str) -> Button:
    assert button.startswith('(') and button.endswith(')')
    return sum(2**int(num) for num in button[1:-1].split(','))

assert parse_button('(1,3)') == 10  # 8 + 2

def parse_joltage_req(joltage_req: str) -> JoltageReq:
    assert joltage_req.startswith('{') and joltage_req.endswith('}')
    return { int(joltage) for joltage in joltage_req[1:-1].split(',') }

assert parse_joltage_req('{3,5,4,7}') == { 3, 5, 4, 7 }

def needed_buttons(machine: Machine) -> int:
    diagram, buttons, _ = machine
    if diagram == 0:
        return 0

    for button in buttons:
        if button == diagram:
            return 1

    for i, button1 in enumerate(buttons):
        for button2 in buttons[i+1:]:
            if button1 ^ button2 == diagram:
                return 2

    for i, button1 in enumerate(buttons):
        for j, button2 in enumerate(buttons[i+1:]):
            for button3 in buttons[j+1:]:
                if button1 ^ button2 ^ button3 == diagram:
                    return 3

    for i, button1 in enumerate(buttons):
        for j, button2 in enumerate(buttons[i+1:]):
            for k, button3 in enumerate(buttons[j+1:]):
                for button4 in buttons[k+1:]:
                    if button1 ^ button2 ^ button3 ^ button4 == diagram:
                        return 4

    for i, button1 in enumerate(buttons):
        for j, button2 in enumerate(buttons[i+1:]):
            for k, button3 in enumerate(buttons[j+1:]):
                for l, button4 in enumerate(buttons[k+1:]):
                    for button5 in buttons[l+1:]:
                        if button1 ^ button2 ^ button3 ^ button4 ^ button5 == diagram:
                            return 5

    for i, button1 in enumerate(buttons):
        for j, button2 in enumerate(buttons[i+1:]):
            for k, button3 in enumerate(buttons[j+1:]):
                for l, button4 in enumerate(buttons[k+1:]):
                    for m, button5 in enumerate(buttons[l+1:]):
                        for button6 in buttons[m+1:]:
                            if button1 ^ button2 ^ button3 ^ button4 ^ button5 ^ button6 == diagram:
                                return 6

    for i, button1 in enumerate(buttons):
        for j, button2 in enumerate(buttons[i+1:]):
            for k, button3 in enumerate(buttons[j+1:]):
                for l, button4 in enumerate(buttons[k+1:]):
                    for m, button5 in enumerate(buttons[l+1:]):
                        for n, button6 in enumerate(buttons[m+1:]):
                            for button7 in buttons[n+1:]:
                                if button1 ^ button2 ^ button3 ^ button4 ^ button5 ^ button6 ^ button7 == diagram:
                                    return 7

    for i, button1 in enumerate(buttons):
        for j, button2 in enumerate(buttons[i+1:]):
            for k, button3 in enumerate(buttons[j+1:]):
                for l, button4 in enumerate(buttons[k+1:]):
                    for m, button5 in enumerate(buttons[l+1:]):
                        for n, button6 in enumerate(buttons[m+1:]):
                            for o, button7 in enumerate(buttons[n+1:]):
                                for button8 in buttons[o+1:]:
                                    if button1 ^ button2 ^ button3 ^ button4 ^ button5 ^ button6 ^ button7 ^ button8 == diagram:
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
            buttons = [parse_button(button_str) for button_str in buttons_str]
            joltage_req = parse_joltage_req(joltage_req_str)
            machines.append((diagram, buttons, joltage_req))

    total_presses = 0
    for machine in machines:
        total_presses += needed_buttons(machine)

    print(f'{file}: {total_presses} presses needed')
