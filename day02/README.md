# Day 2

The [day 2 puzzle][day2] asks you to count repeated numbers.
(I’m not sure if there’s an English term for this;
in German I’d call these „Schnapszahlen“,
which [English Wiktionary][Schnapszahl] translates as “repdigit”,
but according to [Wikipedia][repdigit], that’s restricted to repetions of a single digit.)

This sounded like a problem where a naive implementation in an interpreted language would be quite slow,
so I decided to go for Rust.
Putting together the input parsing code was fiddly and not very fun;
hopefully I’ll at least be able to reuse parts of it on future days.
(Reading the file was partly based on [clean-recently-used][].)
I then added a function for each part, taking a reference to the input and returning the solution.

For part one, we had to sum all numbers in a range that repeated the same substring twice,
e.g. “123123” (repeats “123” twice).
I didn’t want to incur the overhead of formatting the number back to a string and doing string stuff there,
so instead I used the fact that two-digit repeated numbers must be multiples of 11,
four-digit ones multiples of 101, and so forth;
I did a big `match` for all the possible lengths (as numeric ranges), returning the right modulo for each,
and then checked that the number modulo that is zero before adding it up.
This performed very satisfactorily and gave me the correct answer right away.

For part two, we now had to consider all numbers that repeated the same substring any number of times.
This is more of the same, except there are more modulos to check
(so I moved the check inside the match branches):
A six-digit number (6 = 2 * 3) may be two repetitions of a three-digit number (multiple of 1001) or three repetitions of a two-digit number (multiple of 10101);
a seven-digit number (7 is prime) must be seven repetitions of the same digit (multiple of 1111111);
an eight-digit number (8 = 2 * 2 * 2) may be two repetitions of a four-digit number (multiple of 10001) or four repetitions of a two-digit number (multiple of 1010101);
and so on, based on the factorization of the number length and the different ways to split those factors into two sets
(the rectangularization of the number? I don’t know).
This was a bit tedious to think through and write out,
but then performed very well again and still gave me the correct answer on the first try, which felt great.

There’s presumably a more mathematical way to solve this without iterating through the input ranges at all.
(Just generate the candidates, as multiples of 11, 101, 1001 etc., and check how many ranges each candidate is in?)

It also hurts a bit to consider that as a regex, this was expressible *so* tersely (`^(.+)+$`).
I expect that if I look at other people’s solutions,
I’ll quickly discover that this version could perform quite well enough after all.

## Usage

```sh
cargo run
```

If you want, you can add `--release` (after building both, the release version is measurably faster on my system, but building it probably costs a lot more than you’re saving).
The `input` file name (in the current working directory) is hard-coded –
to test the sample input, edit the source code to read `input.sample` instead.

[day2]: https://adventofcode.com/2025/day/2
[Schnapszahl]: https://en.wiktionary.org/wiki/Schnapszahl
[repdigit]: https://en.wikipedia.org/wiki/Repdigit
[clean-recently-used]: https://github.com/lucaswerkmeister/clean-recently-used/
