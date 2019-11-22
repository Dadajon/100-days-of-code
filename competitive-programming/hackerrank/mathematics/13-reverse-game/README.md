# Reverse Game

Akash and Akhil are playing a game. They have **_N_** balls numbered from **_0_** to **_N - 1_**. Akhil asks Akash to reverse the position of the balls, i.e., to change the order from say, 0,1,2,3 to 3,2,1,0. He further asks Akash to reverse the position of the balls **_N_** times, each time starting from one position further to the right, till he reaches the last ball. So, Akash has to reverse the positions of the ball starting from 0th position, then from 1st position, then from 2nd position and so on. At the end of the game, Akhil will ask Akash the final position of any ball numbered **_K_**. Akash will win the game, if he can answer. Help Akash.

### Input Format

The first line contains an integer **_T_**, i.e., the number of the test cases.
The next **_T_** lines will contain two integers **_N_** and **_K_**.

### Output Format

Print the final index of ball **_K_** in the array.

### Constraints

- ![equation](https://latex.codecogs.com/gif.latex?1%20%5Cleq%20T%20%5Cleq%2050)
- ![equation](https://latex.codecogs.com/gif.latex?1%20%5Cleq%20N%20%5Cleq%2010%5E5)
- ![equation](https://latex.codecogs.com/gif.latex?1%20%5Cleq%20K%20%5Cleq%20N)


### Sample Input

    2
    3 1
    5 2

### Sample Output

    2
    4

#### Explanation

For first test case, The rotation will be like this:
0 1 2 -> 2 1 0 -> 2 0 1 -> 2 0 1
So, Index of 1 will be 2.
