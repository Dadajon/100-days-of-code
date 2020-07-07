# Append and Delete

You have a string of lowercase English alphabetic letters. You can perform two types of operations on the string:

1. Append a lowercase English alphabetic letter to the end of the string.
2. Delete the last character in the string. Performing this operation on an empty string results in an empty string.

Given an integer, **_k_**, and two strings, **_s_** and **_t_**, determine whether or not you can convert **_s_** to **_t_** by performing exactly **_k_** of the above operations on **_s_**. 
If it's possible, print **Yes**. Otherwise, print **No**.

For example, strings **_s = [a, b, c]_** and **_t = [d, e, f]_**. Our number of moves, **_k=6_**. To convert **_s_** to **_t_**, we first delete all of the characters in **3** moves. Next we add each of the characters of **_t_** in order. On the **6^th** move, you will have the matching string. If there had been more moves available, they could have been eliminated by performing multiple deletions on an empty string. If there were fewer than **6** moves, we would not have succeeded in creating the new string.

### Function Description

Complete the **_appendAndDelete_** function in the editor below. It should return a string, either **_Yes_** or **_No_**.

**_appendAndDelete_** has the following parameter(s):

 - s: the initial string
 - t: the desired string
 - k: an integer that represents the number of operations

### Input Format

The first line contains a string **_s_**, the initial string.
The second line contains a string **_t_**, the desired final string.
The third line contains an integer **_k_**, the number of operations.

### Constraints
- ![equation](https://latex.codecogs.com/svg.latex?%5Cinline%20%5Cfn_phv%201%5Cleq%20%5Cleft%20%7C%20s%20%5Cright%20%7C%20%5Cleq%20100)
- ![equation](https://latex.codecogs.com/svg.latex?%5Cinline%20%5Cfn_phv%201%5Cleq%20%5Cleft%20%7C%20t%20%5Cright%20%7C%20%5Cleq%20100)
- ![equation](https://latex.codecogs.com/svg.latex?%5Cinline%20%5Cfn_phv%201%5Cleq%20k%20%5Cleq%20100)
- **_s_** and **_t_** consist of lowercase English alphabetic letters, **ascii[a-z]**.

### Output Format

Print **Yes** if you can obtain string **_t_** by performing exactly **_k_** operations on **_s_**. Otherwise, print **No**.

### Sample Input 0

```
hackerhappy
hackerrank
9
```

### Sample Output 0

```
Yes
```

### Explanation 0

We perform **5** delete operations to reduce string **_s_** to **_hacker_**. Next, we perform **4** append operations (i.e., **_r_**, **_a_**, **_n_**, and **_k_**), to get **_hackerrank_**. Because we were able to convert **_s_** to **_t_** by performing exactly **_k = 9_** operations, we print **Yes**.

### Sample Input 1

```
aba
aba
7
```

### Sample Output 1

```
Yes
```

### Explanation 1

We perform **4** delete operations to reduce string **_s_** to the empty string (recall that, though the string will be empty after **3** deletions, we can still perform a delete operation on an empty string to get the empty string). Next, we perform **3** append operations (i.e., **_a_**, **_b_**, and **_a_**). Because we were able to convert **_s_** to **_t_** by performing exactly **_k = 7_** operations, we print **Yes**.

### Sample Input 2

```
ashley
ash
2
```

### Sample Output 2

```
No
```

### Explanation 2

To convert **_ashley_** to **_ash_** a minimum of **3** steps are needed. Hence we print **No** as answer.