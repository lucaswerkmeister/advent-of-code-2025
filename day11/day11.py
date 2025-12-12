type Machine = str

def parse_machines(file: str) -> tuple[dict[Machine, list[Machine]], dict[Machine, list[Machine]]]:
    outwards: dict[Machine, list[Machine]] = {}
    with open(file) as f:
        for line in f:
            machine, others = line.strip().split(': ')
            outwards[machine] = others.split(' ')

    inwards: dict[Machine, list[Machine]] = {}
    for machine, others in outwards.items():
        for other in others:
            inwards.setdefault(other, []).append(machine)

    return outwards, inwards

def paths_from_to(
        outwards: dict[Machine, list[Machine]],
        inwards: dict[Machine, list[Machine]],
        src: Machine,  # `from` is a keyword :<
        dst: Machine,
) -> int:
    paths_to_dst: dict[Machine, int] = { dst: 1 }
    worklist = [dst]
    downstreams: dict[Machine, set[Machine]] = {}
    cyclic: set[Machine] = set()
    while worklist:
        machine, worklist = worklist[0], worklist[1:]
        if machine in cyclic:
            continue
        machine_downstreams = downstreams.setdefault(machine, set())
        for other in inwards.get(machine, []):
            other_downstreams = downstreams.setdefault(other, set())
            if other in other_downstreams:
                cyclic.add(other)
                continue
            other_downstreams.add(machine)
            other_downstreams.update(machine_downstreams)
            paths = sum(paths_to_dst.get(sibling, 0) for sibling in outwards[other])
            if paths != paths_to_dst.get(other):
                paths_to_dst[other] = paths
                worklist.append(other)

    return paths_to_dst[src]
