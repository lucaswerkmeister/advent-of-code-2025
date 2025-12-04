# Day 4

The [day 4 puzzle][day4] asks you to count how many cells in a rectangular grid have fewer than four neighbors,
and then to remove those cells and iterate that process until there are no more to remove and count how many were removed in total.

I’m sure there are better ways to solve this (mod [Golly][]!),
but I couldn’t be bothered and just put together another Bash script,
using arrays and some string manipulation.
I’d like to think the variable names are tolerably readable.
It’s pretty slow (almost 39 seconds for the full input!), but it works.

## Usage

```sh
./solve input.sample input
```

Each listed input file is processed separately.
The main solution printed at the end (per file) is that for part 2;
it also prints intermediate progress lines,
and the part 1 solution is the number in the first of those lines
(the cells that can be removed in the first iteration).

[day4]: https://adventofcode.com/2025/day/4
[Golly]: https://www.wikidata.org/wiki/Special:GoToLinkedPage/enwiki/Q5580856
