# Sequence Equation

Given a sequence of ***n*** integers, ***p(1),p(2),...,p(n)*** where each element is distinct and satisfies ![equation](https://latex.codecogs.com/svg.latex?%5Cinline%201%20%5Cleq%20p%28x%29%20%5Cleq%20n). For each ***x*** where ![equation](https://latex.codecogs.com/svg.latex?%5Cinline%201%20%5Cleq%20x%20%5Cleq%20n), find any integer ***y*** such that ![equation](https://latex.codecogs.com/svg.latex?%5Cinline%20p%28p%28x%29%29%20%5Cequiv%20x) and print the value of ***y*** on a new line.

For example, assume the sequence **_p_ = [5, 2, 1, 3, 4]**. Each value of ***x*** between **1** and **5**, the length of the sequence, is analyzed as follows:

1. ![equation](https://latex.codecogs.com/svg.latex?%5Cinline%20x%3D1%20%5Cequiv%20p%5B3%5D%2C%20p%5B4%5D%20%3D%203), so ![equation](https://latex.codecogs.com/svg.latex?%5Cinline%20p%5Bp%5B4%5D%5D%20%3D%201)
2. ![equation](https://latex.codecogs.com/svg.latex?%5Cinline%20x%20%3D%202%20%5Cequiv%20p%5B2%5D%2C%20p%5B2%5D%20%3D%202), so ![equation](https://latex.codecogs.com/svg.latex?%5Cinline%20p%5Bp%5B2%5D%5D%20%3D%202)
3. ![equation](https://latex.codecogs.com/svg.latex?%5Cinline%20x%20%3D%203%20%5Cequiv%20p%5B4%5D%2C%20p%5B5%5D%20%3D%204), so ![equation](https://latex.codecogs.com/svg.latex?%5Cinline%20p%5Bp%5B5%5D%5D%20%3D%203)
4. ![equation](https://latex.codecogs.com/svg.latex?%5Cinline%20x%20%3D%204%20%5Cequiv%20p%5B5%5D%2C%20p%5B1%5D%20%3D5), so ![equation](https://latex.codecogs.com/svg.latex?%5Cinline%20p%5Bp%5B1%5D%5D%20%3D%204)
5. ![equation](https://latex.codecogs.com/svg.latex?%5Cinline%20x%3D5%20%5Cequiv%20p%5B1%5D%2C%20p%5B3%5D%20%3D%201), so ![equation](https://latex.codecogs.com/svg.latex?%5Cinline%20p%5Bp%5B3%5D%5D%20%3D%205)

The values for ***y*** are **[4, 2, 5, 1, 3]**.

### Function Description

Complete the ***permutation_equation*** function in the editor below. It should return an array of integers that represent the values of ***y***.

***permutation_equation*** has the following parameter(s):

- permut_arr: an array of integers

### Input Format

The first line contains an integer ***n***, the number of elements in the sequence.

The second line contains ***n*** space-separated integers ![equation](https://latex.codecogs.com/svg.latex?%5Cinline%20p%5Bi%5D) where ![equation](https://latex.codecogs.com/svg.latex?%5Cinline%201%20%5Cleq%20i%20%5Cleq%20n).

### Constraints

- ![equation](https://latex.codecogs.com/svg.latex?%5Cinline%201%20%5Cleq%20n%5Cleq%2050)
- ![equation](https://latex.codecogs.com/svg.latex?%5Cinline%201%20%5Cleq%20p%5Bi%5D%20%5Cleq%2050), where ![equation](https://latex.codecogs.com/svg.latex?%5Cinline%201%20%5Cleq%20i%20%5Cleq%20n).
- Each element in the sequence is distinct.

### Output Format

For each ***x*** from **1** to ***n***, print an integer denoting any valid ***y*** satisfying the equation ![equation](https://latex.codecogs.com/svg.latex?%5Cinline%20p%28p%28y%29%29%20%5Cequiv%20x) on a new line.

### Sample Input 0

    3
    2 3 1

### Sample Output 0

    2
    3
    1

### Explanation 0

Given the values of ![equation](https://latex.codecogs.com/svg.latex?%5Cinline%20p%5B1%5D%20%3D%202%2C%20p%5B2%5D%20%3D3), and ![equation](https://latex.codecogs.com/svg.latex?%5Cinline%20p%283%29%20%3D%201), we calculate and print the following values for each ***x*** from **1** to ***n***:

1. ![equation](https://latex.codecogs.com/svg.latex?%5Cinline%20x%20%3D%201%20%5Cequiv%20p%5B3%5D%20%3D%20p%5Bp%5B2%5D%5D%3Dp%5Bp%5By%5D%5D), so we print the value of ***y = 2*** on a new line.
2. ![equation](https://latex.codecogs.com/svg.latex?%5Cinline%20x%20%3D%202%20%5Cequiv%20p%5B1%5D%20%3D%20p%5Bp%5B3%5D%5D%3Dp%5Bp%5By%5D%5D), so we print the value of ***y = 3*** on a new line.
3. ![equation](https://latex.codecogs.com/svg.latex?%5Cinline%20x%20%3D%203%20%5Cequiv%20p%5B2%5D%20%3D%20p%5Bp%5B1%5D%5D%3Dp%5Bp%5By%5D%5D), so we print the value of ***y = 1*** on a new line.

### Sample Input 1

    5
    4 3 5 1 2

### Sample Output 1

    1
    3
    5
    4
    2