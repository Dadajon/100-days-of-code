# Sherlok and divisors
Watson gives an integer *N* to Sherlock and asks him: What is the number of divisors of *N* that are divisible by 2?.

### Input Format

First line contains *T*, the number of testcases. This is followed by *T* lines each containing an integer *N*.

### Output Format

For each testcase, print the required answer in one line.


### Constraints
![equation](https://latex.codecogs.com/svg.latex?1%20%5Cleq%20T%20%5Cleq%20100)

![equation](https://latex.codecogs.com/svg.latex?1%20%5Cleq%20T%20%5Cleq%2010%5E9)


### Sample Input
```
2
9
8
```

### Sample Output
```
0
3
```


### Explanation
9 has three divisors 1, 3 and 9 none of which is divisible by 2.

8 has four divisors 1,2,4 and 8, out of which three are divisible by 2. 


| Test case | Expected outpit |
|:---:|:---:|
| 100 |  |
| 1458 | 7 |
| 2916 | 14 |
| 5832 | 21 |
| 11664 | 28 |
| 23328 | 35 |
| 46656 | 42 |
| 93312 | 49 |
| 186624 | 56 |
| 373248 | 63 |
| 746496 | 70 |
| 1492992 | 77 |
| 2985984 | 84 |
| 5971968 | 91 |
| 11943936 | 98 |
| 23887872 | 105 |
| ... | ... |
