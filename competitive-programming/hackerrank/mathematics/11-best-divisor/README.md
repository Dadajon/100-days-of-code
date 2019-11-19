# Best Divisor

Kristen loves playing with and comparing numbers. She thinks that if she takes two different positive numbers, the one whose digits sum to a larger number is better than the other. If the sum of digits is equal for both numbers, then she thinks the smaller number is better. For example, Kristen thinks that **13** is better than **31** and that **12** is better than **11**.

Given an integer, **_n_**, can you find the divisor of **_n_** that Kristin will consider to be the best?

### Input Format

A single integer denoting **_n_**.

### Constraints

- ![equation](https://latex.codecogs.com/gif.latex?0%20%5Cleq%20n%20%5Cleq%2010%5E5)

### Output Format

Print an integer denoting the best divisor of **_n_**.

### Sample Input 0

    12

### Sample Output 0

    6

### Explanation 0

The set of divisors of **12** can be expressed as **{1, 2, 3, 4, 6, 12}**. The divisor whose digits sum to the largest number is **6** (which, having only one digit, sums to itself). Thus, we print **6** as our answer.
