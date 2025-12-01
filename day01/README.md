# Day 1

The [day 1 puzzle][day1] asks you to turn the dial of a safe and count how often it passes or rests on zero.

This sounded like another great [awk][] job for me,
so I threw out my aspirations to maybe do all of this year in Rust,
and started hacking together a script to process the input line by line.
Part 1 was very straightforward (modulo);
part 2 needed a few more attempts to make sure I was counting clicks correctly,
not double-counting them after the dial ended up resting on zero,
and also making sure the input was actually integral!

## Usage

```sh
./solve input.sample input
```

The script can process any number of files in sequence,
and prints the part 1 + 2 answers for each.
There’s also a commented-out line that may be useful for debugging.

[day1]: https://adventofcode.com/2025/day/1
[awk]: https://en.wikipedia.org/wiki/AWK
