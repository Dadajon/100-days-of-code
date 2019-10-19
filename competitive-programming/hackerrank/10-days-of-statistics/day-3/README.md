# Day 3: Conditional Probability
### Objective
Check out the [Tutorial](https://www.hackerrank.com/challenges/s10-mcq-4/tutorial) tab for learning materials!
### Task
Suppose a family has 2 children, one of which is a boy. What is the probability that both children are boys?

- [x] 1/3
- [ ] 1/2
- [ ] 2/3
- [ ] 1/9

### Solution
There are 4 possible scenarios: (B, B), (B, G), (G, B), (G, G)

We know that 1 child is a boy, so now we have 3 scenarios: (B, B), (B, G), (G, B)

When asked, "what is the probability that both children are boys", the only scenario that matches this is: (B, B). That is, only 1 of the 3 scenarios satisfies the critera, so there is a 1/3 chance that both children are boys.

# Day 3: Cards of the Same Suit
### Combinations and permutations
Check out the [Tutorial](https://www.hackerrank.com/challenges/s10-mcq-5/tutorial) tab for learning materials!

### Task
You draw 2 cards from a standard 52-card deck without replacing them. What is the probability that both cards are of the same suit?
- [ ] 1/156 
- [ ] 1/39
- [ ] 12/39
- [x] 12/51

### Solution
There are 13(52/4) of each suit(A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K) in a deck.

First we draw 1 card and see what suit it is. Whatever suit it is, there are 12 of the same matching suit remaining in the 51-card deck. Therefore, when we draw the 2nd card, there is a 12/51 chance that it is the same suit.

# Day 3: Drawing Marbles
### Task
A bag contains 3 red marbles and 4 blue marbles. Then, 2 marbles are drawn from the bag, at random, without replacement. If the first marble drawn is red, what is the probability that the second marble is blue?

- [ ] 1/12
- [ ] 7/12
- [ ] 1/6
- [x] 2/3

### Solution
After drawing the first marble, we are left with 2 red marbles and 4 blue marbles. Now we calculate the probability of drawing a blue marble as :

    P(B) = (# of blue marbles) / (total # of marbles)
         = 4 / (2 + 4)
         = 2 / 3
