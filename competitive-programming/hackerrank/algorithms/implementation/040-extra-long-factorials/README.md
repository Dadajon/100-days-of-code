# Extra Long Factorials

The factorial of the integer ***n***, written ***n!***, is defined as:

![equation](https://latex.codecogs.com/svg.latex?n%21%20%3D%20n%20%5Ctimes%20%28n-1%29%20%5Ctimes%20%28n-2%29%20%5Ctimes%20...%20%5Ctimes%203%20%5Ctimes%202%20%5Ctimes%201)

Calculate and print the factorial of a given integer.

For example, if **_n_ = 30**, we calculate ![equation](https://latex.codecogs.com/svg.latex?30%20%5Ctimes%2029%20%5Ctimes%2028%20%5Ctimes%20...%20%5Ctimes%202%20%5Ctimes%201) and get **2.6525286e+32**.

### Function Description

Complete the ***extra_long_factorials*** function in the editor below. It should print the result and return.

***extra_long_factorials*** has the following parameter(s):

- n: an integer

**Note:** Factorials of **_n_ > 20** can't be stored even in a **64 - _bit_** long long variable. Big integers must be used for such calculations. Languages like Java, Python, Ruby etc. can handle big integers, but we need to write additional code in C/C++ to handle huge values.

We recommend solving this challenge using BigIntegers.

### Input Format

Input consists of a single integer **_n_**

### Constraints

![equation](https://latex.codecogs.com/svg.latex?1%20%5Cleq%20n%20%5Cleq%20100)

### Output Format

Print the factorial of **_n_**.

### Sample Input

    25

### Sample Output

    15521210043330985984000000

### Explanation

![equation](https://latex.codecogs.com/svg.latex?25%21%20%3D%2025%20%5Ctimes%2024%20%5Ctimes%2023%20%5Ctimes%20...%20%5Ctimes%203%20%5Ctimes%202%20%5Ctimes%201)

