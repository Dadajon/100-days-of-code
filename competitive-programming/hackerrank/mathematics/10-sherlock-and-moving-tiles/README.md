# Sherlock and Moving Tiles

Sherlock is given **2** square tiles, initially both of whose sides have length **_L_** placed in an **_x - y_** plane; so that the bottom left corner of each square coincides with the the origin and their sides are parallel to the axes.

At **_t = 0_**, both squares start moving along line **_y = x_** (along the positive **_x_** and **_y_**) with velocities **_S1_** and **_S2_**.

For each query of form **_qi_**, Sherlock has to report the time at which the overlapping area of tiles is equal to **_qi_**.

![graph](https://s3.amazonaws.com/hr-challenge-images/5519/1422784979-db005a0a44-drawing-3.svg)

**Note:** Assume all distances in meter, time in seconds and velocities in meter per second unless otherwise specified.

### Input Format

First line contains integers . Next line contains , the number of queries. Each of the next  lines consists of one integer  in one line.

### Constraints

- ![equation](https://latex.codecogs.com/gif.latex?1%20%5Cleq%20L%2C%20S_1%2C%20S_2%20%5Cleq%2010%5E9)
- ![equation](https://latex.codecogs.com/gif.latex?1%20%5Cleq%20Q%20%5Cleq%2010%5E5)
- ![equation](https://latex.codecogs.com/gif.latex?1%20%5Cleq%20q_i%20%5Cleq%20L%5E2)
- ![equation](https://latex.codecogs.com/gif.latex?S_1%20%5Cne%20S_2)

### Output Format

For each query, print the required answer in one line. Your answer will be considered correct if it is at most **0.0001** away from the true answer. See the explanation for more details.

### Sample Input

    10 1 2
    2
    50
    100

### Sample Output

    4.1421
    0.0000

### Explanation

For the first case, note that the answer is around 4.1421356237..., so any of the following will be accepted:

    4.1421356237
    4.14214
    4.14215000
    4.1421
    4.1422
