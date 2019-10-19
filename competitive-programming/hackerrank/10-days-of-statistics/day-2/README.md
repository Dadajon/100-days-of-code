# Day 2: Basic Probability
### Objective

Check out the [Tutorial](https://www.hackerrank.com/challenges/s10-mcq-1/tutorial) for a breakdown of probability fundamentals!

### Task

In a single toss of 2 fair (evenly-weighted) six-sided dice, find the probability that their sum will be at most 9.

- [ ] 2/3
- [x] 5/6
- [ ] 1/4
- [ ] 1/6

### Solution

There are 6 possibilities on each die. On 2 dice, there are 6 * 6 = 36 possibilities

There are 6 cases where sum >= 10: (4,6), (5,5), (5,6), (6,4), (6,5), (6,6)

This gives us probability (sum >= 10) = 6/36 = 1/6

That means probability (sum <= 9) = 1 - 1/6 = 5/6

# Day 2: More dice

### Task
In a single toss of 2 fair (evenly-weighted) six-sided dice, find the probability that the values rolled by each die will be different and the two dice have a sum of 6.

- [x] 1/9
- [ ] 1/6
- [ ] 2/3
- [ ] 5/6

### Solution
There are 6 possibilities on each die. On 2 dice, there are 6 * 6 = 36 possibilities

There are 4 cases that match the desired criteria: (1,5) (5,1) (2,4) (4,2)

This gives us a probability of 4/36 = 1/9

# Day 2: Compound Event Probability

### Task
There are 3 urns labeled X, Y, and Z.

* Urn X contains 4 red balls and 3 black balls.
* Urn Y contains 5 red balls and 4 black balls.
* Urn Z contains 4 red balls and 4 black balls.

One ball is drawn from each of the 3 urns. What is the probability that, of the 3 balls drawn, 2 are red and 1 is black?

- [ ] 10/63
- [ ] 2/7
- [x] 17/42
- [ ] 31/126

### Solution
Urn X has a 4/7 probability of giving a red ball
Urn Y has a 5/9 probability of giving a red ball
Urn Z has a 1/2 probability of giving a red ball

Urn X has a 3/7 probability of giving a black ball
Urn Y has a 4/9 probability of giving a black ball
Urn Z has a 1/2 probability of giving a black ball

    P(2 red, 1 black) = P(Red Red Black) + P(Red Black Red) + P(Black Red Red)
                      = (4/7)(5/9)(1/2) + (4/7)(4/9)(1/2) + (3/7)(5/9)(1/2)
                      = 20/126 + 16/126 + 15/126
                      = 51/126