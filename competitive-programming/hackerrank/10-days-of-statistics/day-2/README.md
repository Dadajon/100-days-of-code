# Day 2: Basic Probability
### Objective

In this challenge, we practice calculating probability. Check out the Tutorial tab for a breakdown of probability fundamentals!

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
### Objective

In this challenge, we practice calculating probability. We recommend you review the previous challenge's Tutorial before attempting this problem.

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

### Objective
In this challenge, we practice calculating the probability of a compound event. We recommend you review today's Probability Tutorial before attempting this challenge.

### Task
There are 3 urns labeled X, Y, and Z.

* Urn  contains  red balls and  black balls.
* Urn  contains  red balls and  black balls.
* Urn  contains  red balls and  black balls.

One ball is drawn from each of the  urns. What is the probability that, of the  balls drawn,  are red and  is black?

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