# Restaurant

Martha is interviewing at Subway. One of the rounds of the interview requires her to cut a bread of size ![equation](https://latex.codecogs.com/gif.latex?l%20%5Ctimes%20b) into smaller identical pieces such that each piece is a square having maximum possible side length with no left over piece of bread.

### Input Format

The first line contains an integer **_T_**. **_T_** lines follow. Each line contains two space separated integers **_l_** and **_b_** which denote length and breadth of the bread.

### Constraints
- ![equation](https://latex.codecogs.com/gif.latex?1%20%5Cleq%20T%20%5Cleq%201000)
- ![equation](https://latex.codecogs.com/gif.latex?1%20%5Cleq%20l%2Cb%20%5Cleq%201000)

### Output Format

**_T_** lines, each containing an integer that denotes the number of squares of maximum size, when the bread is cut as per the given condition.

### Sample Input 0

    2
    2 2
    6 9

### Sample Output 0

    1
    6

### Explanation 0

The 1st testcase has a bread whose original dimensions are ![equation](https://latex.codecogs.com/gif.latex?2%20%5Ctimes%202), the bread is uncut and is a square. Hence the answer is 1.

The 2nd testcase has a bread of size ![equation](https://latex.codecogs.com/gif.latex?6%20%5Ctimes%209). We can cut it into 54 squares of size ![equation](https://latex.codecogs.com/gif.latex?1%20%5Ctimes%201), 6 of size ![equation](https://latex.codecogs.com/gif.latex?3%20%5Ctimes%203). For other sizes we will have leftovers. Hence, the number of squares of maximum size that can be cut is 6.
