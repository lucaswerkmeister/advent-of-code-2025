# Day 11

The [day 11 puzzle][day11] asks you to count paths in a graph.

I quickly concluded that there must be no cycles along the path from the source to the destination,
because the puzzle didn’t specify how those should be counted,
so if that was the case the answer would be “there are ∞ paths” and that wouldn’t be very interesting.
That doesn’t mean that the input is cycle-free –
indeed, while the sample inputs are, the real input very much isn’t! –
but as soon as we detect a cycle, we can discard that whole part of the graph,
because it’s certainly not going to be part of the solution.

I then wrote some Python code to parse the graph,
track reverse edges as well (in my code, “outwards” is the puzzle input and “inwards” is the inverse of that),
and count the number of paths to the `out` node.
It starts with the `out` node, which has one path to itself,
and then looks through all the nodes that lead directly to it,
and then all the nodes leading to those, and so on.
Each node is assigned a number of paths that lead from it to the `out` node,
which is the sum of the numbers of all the other nodes that node has “outwards” edges to;
if a node’s number changes, add all of its “inwards” neighbors back to the work list,
to (re)calculate their numbers.
Also, to avoid getting stuck in cycles, track a set of “downstream” nodes of each node;
if a node’s “downstreams” include itself, we’ve hit a cycle and can ignore that node from now on.
(I don’t think I explained this very well, but the algorithm makes intuitive sense to me and hopefully the code isn’t too unreadable ^^)

This code gave me the correct answer for the sample input pretty quickly,
but then got stuck on the real input for a while;
to debug the cycle detection, I jotted down my own graph and translated that into a second sample input file,
which is also included in this repository.
(I should do this more often!)
Eventually I got it working and it gave me the right solution:
the number of different paths from `you` to `out`.

Part 2 then asks you to count the paths from a different starting node (`svr`)
which also traverse two other nodes (`dac` and `fft`, but in any order).
I was a bit nervous about this at first,
but after sleeping over it, I realized it’s not so bad.
First of all, “in any order” is kinda misleading: only one of those orders can actually occur,
otherwise we’re back to having a cycle and the answer being “∞”.
Also, we don’t actually have to materialize the paths (there are trillions of them, it turns out!) to check if they include those nodes;
given that the path segments between the nodes are independent,
the total number is just the product of the number of paths from `svr` to `dac`, from `dac` to `fft`, and from `fft` to `out`,
plus the same product with `dac` and `fft` swapped.
(Per the cycle argument, one of those summands will be zero.)
So I refactored the code to turn the graph traversal into a function which takes the source and destination as arguments,
and then the whole thing worked itself out very nicely and gave me the correct answer right away.

## Usage

```sh
./part1.py input.part1.sample input
./part2.py input.part2.sample input
```

Each script prints the solution for one part of the puzzle for each given input file.
(They’re separate scripts because the sample inputs are different.)

[day11]: https://adventofcode.com/2025/day/11
