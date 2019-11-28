# Viral Advertising

HackerLand Enterprise is adopting a new viral advertising strategy. When they launch a new product, they advertise it to exactly **5** people on social media.

On the first day, half of those **5** people (i.e., ![equation](https://latex.codecogs.com/svg.latex?%5Cinline%20floor%28%5Cfrac%7B5%7D%7B2%7D%29%3D2)) like the advertisement and each shares it with **3** of their friends. At the beginning of the second day, ![equation](https://latex.codecogs.com/svg.latex?%5Cinline%20floor%28%5Cfrac%7B5%7D%7B2%7D%29%20%5Ctimes%203%3D2%20%5Ctimes%203) people receive the advertisement.

Each day, ![equation](https://latex.codecogs.com/svg.latex?%5Cinline%20floor%28%5Cfrac%7Brecipients%7D%7B2%7D%29) of the recipients like the advertisement and will share it with **3** friends on the following day. Assuming nobody receives the advertisement twice, determine how many people have liked the ad by the end of a given day, beginning with launch day as day **1**.

For example, assume you want to know how many have liked the ad by the end of the **5th** day.

    Day Shared Liked Cumulative
    1      5     2       2
    2      6     3       5
    3      9     4       9
    4     12     6      15
    5     18     9      24

The cumulative number of likes is **24**.

### Function Description

Complete the ***viral_advertising*** function in the editor below. It should return the cumulative number of people who have liked the ad at a given time.

***viral_advertising*** has the following parameter(s):

n: the integer number of days

### Input Format

A single integer, , denoting a number of days.

### Constraints

- ![equation](https://latex.codecogs.com/svg.latex?%5Cinline%201%20%5Cleq%20n%20%5Cleq%2050)

### Output Format

Print the number of people who liked the advertisement during the first **n** days.

### Sample Input

    3

### Sample Output

    9

### Explanation

This example is depicted in the following diagram:

![image](https://s3.amazonaws.com/hr-challenge-images/26216/1475677928-3788004924-strangead.png)

**2** people liked the advertisement on the first day, **3** people liked the advertisement on the second day and **4** people liked the advertisement on the third day, so the answer is **2 + 3 + 4 = 9**.