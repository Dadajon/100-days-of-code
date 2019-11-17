# Picking Numbers

Given an array of integers, find and print the maximum number of integers you can select from the array such that the absolute difference between any two of the chosen integers is less than or equal to **1**. For example, if your array is **_a_ = [1, 1, 2, 2, 4, 4, 5, 5, 5]**, you can create two subarrays meeting the criterion: **[1, 1, 2, 2]** and **[4, 4, 5, 5, 5]**. The maximum length subarray has **5** elements.

### Function Description

Complete the **_picking_numbers_** function in the editor below. It should return an integer that represents the length of the longest array that can be created.

**_picking_numbers_** has the following parameter(s):

- a: an array of integers

### Input Format

The first line contains a single integer **_n_**, the size of the array **_a_**.
The second line contains **_n_** space-separated integers **_a_[_i_]**.

### Constraints

- ![equation](https://latex.codecogs.com/gif.latex?2%20%5Cleq%20n%20%5Cleq%20100)
- ![equation](https://latex.codecogs.com/gif.latex?0%20%5Cleq%20a%5Bi%5D%20%5Cleq%20100)
- The answer will be ![equation](https://latex.codecogs.com/gif.latex?%5Cgeq%202).

### Output Format

A single integer denoting the maximum number of integers you can choose from the array such that the absolute difference between any two of the chosen integers is ![equation](https://latex.codecogs.com/gif.latex?%5Cleq%201).

### Sample Input 0

    6
    4 6 5 3 3 1

### Sample Output 0

    3

### Explanation 0

We choose the following multiset of integers from the array: **{4, 3, 3}**. Each pair in the multiset has an absolute difference ![equation](https://latex.codecogs.com/gif.latex?%5Cleq%201) (i.e., **|4 - 3| = 1** and **|3 - 3| = 0**), so we print the number of chosen integers, **3**, as our answer.

### Sample Input 1

    6
    1 2 2 3 1 2

### Sample Output 1

    5

### Explanation 1

We choose the following multiset of integers from the array: **{1, 2, 2, 1, 2}**. Each pair in the multiset has an absolute difference ![equation](https://latex.codecogs.com/gif.latex?%5Cleq%201) (i.e., **|1 - 2| = 1**, **|1 - 1| = 0**, and **|2 - 2| = 0**), so we print the number of chosen integers, **5**, as our answer.
