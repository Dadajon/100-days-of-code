# Forming a Magic Square

We define a magic square to be an ![equation](https://latex.codecogs.com/gif.latex?n%20%5Ctimes%20n) matrix of distinct positive integers from **_1_** to ![equation](https://latex.codecogs.com/gif.latex?n%5E2) where the sum of any row, column, or diagonal of length  is always equal to the same number: the magic constant.

You will be given a ![](https://latex.codecogs.com/gif.latex?3%20%5Ctimes%203) matrix **_s_** of integers in the inclusive range ![](https://latex.codecogs.com/gif.latex?%5B1%2C%209%5D). We can convert any digit **_a_** to any other digit **_b_** in the range ![](https://latex.codecogs.com/gif.latex?%5B1%2C%209%5D) at cost of ![](https://latex.codecogs.com/gif.latex?%7C%20a-%20b%7C). Given **_s_**, convert it into a magic square at minimal cost. Print this cost on a new line.

**Note**: The resulting magic square must contain distinct integers in the inclusive range ![](https://latex.codecogs.com/gif.latex?%5B1%2C%209%5D).

For example, we start with the following matrix **_s_**:

    5 3 4
    1 5 8
    6 4 2

We can convert it to the following magic square:

    8 3 4
    1 5 9
    6 7 2

This took three replacements at a cost of ![](https://latex.codecogs.com/gif.latex?%5Cleft%20%7C%205-8%20%5Cright%20%7C+%5Cleft%20%7C8-9%20%5Cright%20%7C+%5Cleft%20%7C%204-7%20%5Cright%20%7C%20%3D%207).

### Function Description

Complete the **_forming_magic_square_** function in the editor below. It should return an integer that represents the minimal total cost of converting the input square to a magic square.

**_forming_magic_square_** has the following parameter(s):

s: a ![](https://latex.codecogs.com/gif.latex?3%5Ctimes%203) array of integers

### Input Format

Each of the lines contains three space-separated integers of row **_s[i]_**.

### Constraints

![](https://latex.codecogs.com/gif.latex?s%5Bi%5D%5Bj%5D%20%5Cin%20%5B1%2C9%5D)

### Output Format

Print an integer denoting the minimum cost of turning matrix **_s_** into a magic square.

### Sample Input 0

    4 9 2
    3 5 7
    8 1 5

### Sample Output 0

    1

### Explanation 0

If we change the bottom right value, **_s[2][2]_**, from **_5_** to **_6_** at a cost of ![](https://latex.codecogs.com/gif.latex?%5Cleft%20%7C%206-5%20%5Cright%20%7C%20%3D%201), **_s_** becomes a magic square at the minimum possible cost.

### Sample Input 1

    4 8 2
    4 5 7
    6 1 6

### Sample Output 1

    4

### Explanation 1

Using 0-based indexing, if we make

-   **_s[0][1] -> 9_** at a cost of **_|9 - 8| = 1_**
-   **_s[1][0] -> 3_** at a cost of **_|3 - 4| = 1_**
-   **_s[2][0] -> 8_** at a cost of **_|8 - 6| = 2_**,

then the total cost will be **_1 + 1 + 2 = 4_**.
