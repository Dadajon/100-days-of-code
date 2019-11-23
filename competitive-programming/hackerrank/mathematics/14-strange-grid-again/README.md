# Strange Grid Again

A strange grid has been recovered from an old book. It has **5** columns and infinite number of rows. The bottom row is considered as the first row. First few rows of the grid are like this:

    ..............
    
    ..............

    20 22 24 26 28

    11 13 15 17 19

    10 12 14 16 18

    1  3  5  7  9

    0  2  4  6  8

The grid grows upwards forever!

Your task is to find the integer in **_c_th** column in **_r_th** row of the grid.

### Input Format

There will be two integers r and c separated by a single space.

### Constraints

- ![equation](https://latex.codecogs.com/gif.latex?1%20%5Cleq%20r%20%5Cleq%202*10%5E9)
- ![equation](https://latex.codecogs.com/gif.latex?1%20%5Cleq%20c%20%5Cleq%205)

Rows are indexed from bottom to top and columns are indexed from left to right.

### Output Format

Output the answer in a single line.

### Sample Input

    6 3

### Sample Output

    25

### Explanation

The number in the 6th row and 3rd column is 25.
