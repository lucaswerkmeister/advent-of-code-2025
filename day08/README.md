# Day 8

The [day 8 puzzle][day8] asks you to analyze junction boxes in 3D space and possible connections and circuits between them.

This one was tough, and I had to spend a while debugging it even after getting the correct solution for the sample input.
I did it in Python again, and didn’t feel like introducing any new classes
(though I eventually added type aliases) –
just the basic Python data structures: tuples, dicts, lists, sets.
(I feel like there should be an acronym for those. TDLS, pronounced “toodles”?)
First parse the boxes,
then find the shortest connections between them
(it turns out that iterating through all n*(n+1)/2 combinations, and keeping a running list of the shortest x connections found,
is much faster than trying to repeatedly find the next shortest connection).
Then add those connections together into circuits –
this turns out to be both the bulk of the code and the bulk of the work / debugging effort;
I eventually got there with a lot of debug assertions of invariants that ought to always hold,
until I found the ones that were being violated and could investigate them.
I left a lot of my trial-and-error in the Git history
(and the assertions are still in the final code, though the debug prints aren’t),
if you’re interested in that.

Part 2 is then just more circuit merging
(for which I extracted my code, previously a huge block inside one `process()` function,
into a separate `add_pair_to_circuits()` function).
The implementation is relatively straightforward,
but surprisingly slow – *almost* slow enough that I gave up and tried to optimize it,
but then I got the right solution after all,
and now it’s past 2AM and I *really* don’t feel like spending more time with this code :)
at a guess, it’s probably spending a lot of time interconnecting the same one big circuit more and more while the remaining outlying boxes languish,
and at some point (heuristically determined) it would be smart to switch from finding the next shortest connection
to going through all the remaining unconnected boxes and trying to specifically connect those to the big circuit.

## Usage

```sh
./solve.py input.sample input
```

This time the command line arguments are a *bit* of a lie,
because the program hard-codes the number of connections to use for these two files,
and will raise an error given any other file name.
But at least you can pick if you want to just quickly check the sample input or analyze the full real input.

Solutions to both part 1 and 2 are printed.

[day8]: https://adventofcode.com/2025/day/8
