# Beautiful Days at the Movies

Lily likes to play games with integers. She has created a new game where she determines the difference between a number and its reverse. For instance, given the number **12**, its reverse is **21**. Their difference is **9**. The number **120** reversed is **21**, and their difference is **99**.

She decides to apply her game to decision making. She will look at a numbered range of days and will only go to a movie on a beautiful day.

Given a range of numbered days, **[*i ... j*]** and a number ***k***, determine the number of days in the range that are beautiful. Beautiful numbers are defined as numbers where ![equation](https://latex.codecogs.com/gif.latex?%7C%20i%20-reverse%28i%29%7C) is evenly divisible by ***k***. If a day's value is a beautiful number, it is a beautiful day. Print the number of beautiful days in the range.

### Function Description

Complete the ***beautiful_days*** function in the editor below. It must return the number of beautiful days in the range.

***beautiful_days*** has the following parameter(s):

- start_day: the starting day number
- end_day: the ending day number
- divisor_k: the divisor

### Input Format

A single line of three space-separated integers describing the respective values of ***start_day***, ***end_day***, and ***divisor_k***.

### Constraints

- ![equation](https://latex.codecogs.com/gif.latex?1%20%5Cleq%20i%20%5Cleq%20j%20%5Cleq%202%20%5Ctimes10%5E6)
- ![equation](https://latex.codecogs.com/gif.latex?1%20%5Cleq%20k%20%5Cleq%2010%5E9)

### Output Format

Print the number of beautiful days in the inclusive range between ***start_day*** and ***end_day***.

### Sample Input

    20 23 6

### Sample Output

    2

### Explanation

Lily may go to the movies on days ***20***, ***21***, ***22***, and ***23***. We perform the following calculations to determine which days are beautiful:

- Day ***20*** is beautiful because the following evaluates to a whole number: ![equation](https://latex.codecogs.com/png.latex?%5Cinline%20%5Cfrac%7B%7C20-02%7C%7D%7B6%7D%20%3D%20%5Cfrac%7B18%7D%7B6%7D%20%3D%203)
- Day ***21*** is not beautiful because the following doesn't evaluate to a whole number: ![equation](https://latex.codecogs.com/png.latex?%5Cinline%20%5Cfrac%7B%7C21-12%7C%7D%7B6%7D%20%3D%20%5Cfrac%7B9%7D%7B6%7D%20%3D%201.5)
- Day ***22*** is beautiful because the following evaluates to a whole number: ![equation](https://latex.codecogs.com/png.latex?%5Cinline%20%5Cfrac%7B%7C22-22%7C%7D%7B6%7D%20%3D%20%5Cfrac%7B0%7D%7B6%7D%20%3D%200)
- Day ***23*** is not beautiful because the following doesn't evaluate to a whole number: ![equation](https://latex.codecogs.com/png.latex?%5Cinline%20%5Cfrac%7B%7C23-32%7C%7D%7B6%7D%20%3D%20%5Cfrac%7B9%7D%7B6%7D%20%3D%201.5)

Only two days, **20** and **22**, in this interval are beautiful. Thus, we print **2** as our answer.
