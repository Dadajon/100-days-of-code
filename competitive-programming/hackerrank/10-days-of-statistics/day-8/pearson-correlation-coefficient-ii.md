# Day 8: Pearson Correlation Coefficient II

The regression line of *y* on *x* is *3x-4y+8=0*, and the regression line of *x* on *y* is *4x+3y+7=0*. 
What is the value of the Pearson correlation coefficient?

**Note:** If you haven't seen it already, you may find our [Pearson Correlation Coefficient Tutorial](https://www.hackerrank.com/challenges/s10-pearson-correlation-coefficient/tutorial) 
helpful in answering this question.

- [ ] 1
- [ ] -1
- [ ] 3/4
- [ ] -4/3
- [ ] 4/3
- [x] -3/4

## Solution
regression X:

    3x + 4y + 8 = 0
    4y = -3x - 8
    y = -3x/4 - 8/4
    y = -3x/4 - 4 (reverse signal)
    y = -3x/4 - 4
    bx = -3/4

regression Y:

    4x + 3y + 7 = 0
    4x = -3y - 7
    x = -3x/4 - 7/4 (reverse signal)
    x =  -3x/4 - 7/4
    by = -3/4

Finally:

    r² = bx * by
    r² = -3/4 * -3/4
    r² = 9/16
    r +/- 3/4

    if bx = by then
    r = -3/4