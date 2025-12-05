# Day 5

The [day 5 puzzle][day5] asks you evaluate integer ranges.

I started by implementing the first part,
which asks how many out of a list of IDs are in at least one of the ranges,
in Bash, mostly out of convenience.
It wasn’t super performant, but it was fast enough (half a second).

Part 2 asks how many IDs are included in the ranges overall.
I quickly added this to my Bash implementation and started running it,
but when it didn’t print a result for a few seconds,
I looked more closely at the input and noticed that some of the ranges are quite big
(`units 'log([last]-[first])/log(2)'` for a random range reported 41.something,
i.e. a 41-bit difference between the start end end point),
so my approach of iterating through the IDs was never going to work.
That said, I really didn’t feel like implementing complex range checks
(surely some of them overlap, otherwise it would be too easy!) in Bash.

So I rewrote my Bash script in Python.
Reading the input was a *bit* tricky –
apparently, if you have an open file,
iterate over its lines,
break out of that loop,
and then try to iterate over it,
it won’t give you the rest of the lines,
so I had to use `f.readline()` with the walrus operator instead –
but otherwise it wasn’t too bad.
And here I could use the [intervaltree][] library,
which I’d previously worked with in [SpeedPatrolling][]
and which could manage the intervals for me
(with the caveat that the puzzle ranges are inclusive while intervaltree intervals are exclusive).
Annoyingly, `len(intervaltree)` doesn’t give me the number of elements covered by the interval tree,
but at least I could use `intervaltree.merge_overlaps()` to take care of potentially overlapping intervals,
and then just iterate over the remaining ones and add up their sizes.

## Usage

```sh
./solve input.sample  # Bash
./solve.py input.sample input  # python
```

Both implementations take a list of input files, process them separately, and print out the part 1 and then part 2 solutions;
in theory, you can call the Bash implementation with `input`, but don’t expect it to ever print out part 2 :D

[day5]: https://adventofcode.com/2025/day/5
[intervaltree]: https://pypi.org/project/intervaltree/
[SpeedPatrolling]: https://gitlab.wikimedia.org/toolforge-repos/speedpatrolling/
