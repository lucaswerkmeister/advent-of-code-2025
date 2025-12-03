# Day 3

The [day 3 puzzle][day3] asks you to find the largest number you can get by picking a number of digits out of a longer string of digits (without reordering).

My initial solution, for part 1, was kind of brute force:
iterate through all the possible first digits, then all the possible second digits,
checking if the first and then second digits appear in the input line.
I decided to implement this in Bash, because I felt like it.

For part 2, the number of digits was raised to 12, which of course made my previous approach unfeasible.
Instead, I realized that the way to solve this puzzle is to start looking for the highest digit in all but the last 11 digits of the line
(i.e. look for a 9, then an 8 if there’s no 9, etc.; but because we’ll have to pick 11 more digits, don’t look at the last ones at all),
and then removing everything up to and including that digit from the line and looking for the highest digit in all but the last 10 digits of the remainder,
and so on – this way we always know we’ve found the optimal leading string of digits so far.
This is also relatively straightforwardly implementable in Bash, so I did just that,
and it happily gave me the right answer very quickly.

## Usage

```sh
./solve input.sample input
```

The preamble of the script defines the length to look for; it’s committed as `length=12` (part 2),
but if you change it to `length=2` you’ll get the right answer for part 1.
The script can process several input files (like my day 1 awk script)
and prints the solution for each.

[day3]: https://adventofcode.com/2025/day/3
