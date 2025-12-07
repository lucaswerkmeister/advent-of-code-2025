# Day 7

The [day 7 puzzle][day7] asks you to follow a particle through a network of beam splitters.

I went for Python straight away, which turned out to be a good choice, I think.
Part 1 was pretty straightforward – just some string manipulation,
updating the current line based on the character above it in the previous line.
By keeping the whole state around, I could even print it for debugging,
though I don’t think I ended up needing that.

Part 2 was trickier: here you have to count all the possible paths through the network.
I first adapted my part 1 code to follow and track all of these paths,
but while it worked for the sample input, it quickly became clear that,
even with some optimizations (check the Git history, I committed them ^^),
this wouldn’t work for the real input:
there’s just too many options and not enough memory to hold them in.
(Around 70 to 80 lines through the 140ish-line input, my Python processes started hitting ca. 14 GiB of memory usage.)
Also, this approach is of course very wasteful:
while there can be many different ways to reach any given line,
and we need to know how many ways there are,
the development from that line does not depend on its previous history,
and we should really just calculate it once instead of potentially millions of times.
Fortunately, turning the code into a version that tracks a dict mapping lines to the number of worlds which reach that line
turned out to be pretty easy and gave me the right solution straight away,
basically instantly (a dozen milliseconds or so) \o/

## Usage

```sh
./solve.py input.sample input
```

The latest version only solves part 2; if you want part 1, look at the Git history.
Like in day 6, I couldn’t think of a reasonable way to keep both implementations together in the file and reuse some code between them.

[day7]: https://adventofcode.com/2025/day/7
