# Circular Array Rotation

John Watson knows of an operation called a right circular rotation on an array of integers. One rotation operation moves the last array element to the first position and shifts all remaining elements right one. To test Sherlock's abilities, Watson provides Sherlock with an array of integers. Sherlock is to perform the rotation operation a number of times then determine the value of the element at a given position.

For each array, perform a number of right circular rotations and return the value of the element at a given index.

For example, array **_a_ = [3, 4, 5]**, number of rotations, **_k_ = 2** and indices to check, **_m_ = [1, 2]**.

First we perform the two rotations:
**[3, 4, 5] -> [5, 3, 4] -> [4, 5, 3]**

Now return the values from the zero-based indices **1** and **2** as indicated in the **m** array.

- **_a_[1] = 5**
- **_a_[2] = 3**

### Function Description

Complete the ***circular_array_rotation*** function in the editor below. It should return an array of integers representing the values at the specified indices.

***circular_array_rotation*** has the following parameter(s):

- arr: an array of integers to rotate
- rotations: an integer, the rotation count
- queries: an array of integers, the indices to report

### Input Format

The first line contains **3** space-separated integers, ***n***, ***k***, and ***q***, the number of elements in the integer array, the rotation count and the number of queries.
The second line contains ***n*** space-separated integers, where each integer ***i*** describes array element **_a_[i]** (where ![equation](https://latex.codecogs.com/svg.latex?%5Cinline%200%20%5Cleq%20i%20%5Cleq%20n)).
Each of the **q** subsequent lines contains a single integer denoting ***m***, the index of the element to return from ***arr***.

### Constraints

- ![equation](https://latex.codecogs.com/svg.latex?%5Cinline%201%20%5Cleq%20n%20%5Cleq%2010%5E5)
- ![equation](https://latex.codecogs.com/svg.latex?%5Cinline%201%20%5Cleq%20a%5Bi%5D%20%5Cleq%2010%5E5)
- ![equation](https://latex.codecogs.com/svg.latex?%5Cinline%201%20%5Cleq%20k%20%5Cleq%2010%5E5)
- ![equation](https://latex.codecogs.com/svg.latex?%5Cinline%201%20%5Cleq%20q%20%5Cleq%20500)
- ![equation](https://latex.codecogs.com/svg.latex?%5Cinline%200%20%5Cleq%20m%20%3C%20n)

### Output Format

For each query, print the value of the element at index ***m*** of the rotated array on a new line.

### Sample Input 0

    3 2 3
    1 2 3
    0
    1
    2

### Sample Output 0

    2
    3
    1

### Explanation 0

After the first rotation, the array becomes **[3, 1, 2]**.
After the second (and final) rotation, the array becomes **[2, 3, 2]**.

Let's refer to the array's final state as array **_b_ = [2, 3, 1]**. For each query, we just have to print the value of ![equation](https://latex.codecogs.com/svg.latex?%5Cinline%20b_m) on a new line:

1. ![equation](https://latex.codecogs.com/svg.latex?%5Cinline%20m%20%3D%200%2C%20b_0%20%3D%202)
2. ![equation](https://latex.codecogs.com/svg.latex?%5Cinline%20m%20%3D%201%2C%20b_1%20%3D%203)
3. ![equation](https://latex.codecogs.com/svg.latex?%5Cinline%20m%20%3D%202%2C%20b_2%20%3D%201)