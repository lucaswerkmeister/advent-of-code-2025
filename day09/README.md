# Day 9

The [day 9 puzzle][day9] asks you to find the largest rectangle within a polygon.

My part 1 solution is not worth talking about, I think – nothing special in there.
I’m currently stumped on part 2 – I have code that I think ought to give the right solution, but is clearly *vastly* too slow.

For part 2, we’re given a polygon composed of horizontal and vertical edges,
and have to find the largest rectangle inside the polygon which also has two opposite corners that are vertices of the polygon.
(I *think* that last part is a real limitation –
with a complicated enough polygon I suspect you can construct a situation where the largest interior rectangle has corners that merely lie on the edges of the polygon.
But I’m not sure.)
I briefly tried to “materialize” the full grid with the polygon inside it (a list of lists of bools),
but it quickly became clear that this wouldn’t work, it would require far too much RAM.

My current approach is to iterate over all possible rectangles (i.e. pairs of edges),
and (if they’re larger than the current best result) over all points within them,
testing that each point is inside the polygon.
To test if a point is in the polygon, I remembered a trick I read somewhere else –
you draw lines from the exterior of the polygon to the point inside and count how many times they’re crossing the polygon’s edges;
if it’s even, then the point is outside, if it’s odd, it’s inside.
I’m not sure how exactly that works for a general polygon,
but if all the edges are horizontal or vertical,
then it should be enough to do that test twice, once parallel to the X axis and once parallel to the Y axis,
and so that’s what my code does.
It yields the correct result for the sample input,
and I tried to optimize it a little bit by not checking points that aren’t aligned with any edges
(I know they’re not going to change the result on their own).

However, this is clearly going nowhere:

<details>
<summary>partial calculation</summary>

```
$ time ./solve.py input
1/122760
max_part2_area=1220 because dx=1<=2 or dy=1220<=2
2/122760
3/122760
4/122760
5/122760
6/122760
7/122760
8/122760
max_part2_area=945112 because legal rectangle: tile1=(97585, 50248), tile2=(97390, 55069)
9/122760
10/122760
11/122760
12/122760
13/122760
14/122760
15/122760
16/122760
17/122760
18/122760
19/122760
20/122760
21/122760
22/122760
23/122760
24/122760
25/122760
26/122760
27/122760
28/122760
29/122760
30/122760
31/122760
32/122760
^CTraceback (most recent call last):
  File "/home/lucas/git/advent-of-code-2025/day09/./solve.py", line 135, in <module>
    if is_legal_rectangle():
       ~~~~~~~~~~~~~~~~~~^^
  File "/home/lucas/git/advent-of-code-2025/day09/./solve.py", line 99, in is_legal_rectangle
    for h in green_horizontals.get(y_incr, []):
             ~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^
KeyboardInterrupt

real    105m24,268s
user    104m53,938s
sys     0m0,351s
```

</details>

This seems slow enough that some optimization isn’t going to cut it –
I probably need a completely fresh approach.
(Perhaps using some library, I don’t know.)

## Usage

```sh
./solve.py input.sample input
```

This attempts to print the solutions to part 1 and 2 for each file.

[day9]: https://adventofcode.com/2025/day/9
