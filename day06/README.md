# Day 6

The [day 6 puzzle][day6] asks you perform calculations on input given vertically instead of horizontally.

This probably would’ve been very straightforward to do if there was a simple way to “diagonally mirror” an input file on Unixoid systems,
but I’m not aware of one (there’s e.g. `rev` and `tac` to mirror “horizontally” and “vertically”,
but nothing to turn columns into rows and vice versa;
[this article][transposing] claims GNU `datamash` can do it, but I’ve never heard of that and don’t have it installed).
I was lazy again and just used another Bash script with string manipulation;
it’s not the fastest (amusingly, part 1 is substantially slower than part 2,
probably because I’m splitting the input lines into numbers over and over again on account of Bash not having nested arrays),
but it was good enough.
I don’t think I have a lot else to say about it.
(The part 2 solution make use of the fact that all the operators in the input are left-aligned.)

## Usage

```sh
./solve input.sample input
```

The latest version only solves part 2; if you want part 1, check out the earlier commit touching it.
I couldn’t think of a reasonable way to keep both implementations together in the file and reuse some code between them;
they’re effectively separate implementations, and I didn’t feel like keeping them both in the file side-by-side
(with the risk of reused variable names causing issues) –
especially given that part 1 is so slow.

[day6]: https://adventofcode.com/2025/day/6
[transposing]: https://www.thelinuxrain.org/articles/transposing-rows-and-columns-3-methods
