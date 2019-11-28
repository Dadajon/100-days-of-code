# Save the Prisoner!

A jail has a number of prisoners and a number of treats to pass out to them. Their jailer decides the fairest way to divide the treats is to seat the prisoners around a circular table in sequentially numbered chairs. A chair number will be drawn from a hat. Beginning with the prisoner in that chair, one candy will be handed to each prisoner sequentially around the table until all have been distributed.

The jailer is playing a little joke, though. The last piece of candy looks like all the others, but it tastes awful. Determine the chair number occupied by the prisoner who will receive that candy.

For example, there are **4** prisoners and **6** pieces of candy. The prisoners arrange themselves in seats numbered **1** to **4**. Let's suppose two is drawn from the hat. Prisoners receive candy at positions **2, 3, 4, 1, 2, 3**. The prisoner to be warned sits in chair number **3**.

### Function Description

Complete the ***save_the_prisoner*** function in the editor below. It should return an integer representing the chair number of the prisoner to warn.

***save_the_prisoner*** has the following parameter(s):

- n: an integer, the number of prisoners
- m: an integer, the number of sweets
- s: an integer, the chair number to begin passing out sweets from

### Input Format

The first line contains an integer, **t**, denoting the number of test cases.
The next **t** lines each contain **3** space-separated integers:
- n: the number of prisoners
- m: the number of sweets
- s: the chair number to start passing out treats at

### Constraints

- ![equation](https://latex.codecogs.com/svg.latex?%5Cinline%201%20%5Cleq%20t%20%5Cleq%20100)
- ![equation](https://latex.codecogs.com/svg.latex?%5Cinline%201%20%5Cleq%20n%20%5Cleq%2010%5E9)
- ![equation](https://latex.codecogs.com/svg.latex?%5Cinline%201%20%5Cleq%20m%20%5Cleq%2010%5E9)
- ![equation](https://latex.codecogs.com/svg.latex?%5Cinline%201%20%5Cleq%20s%20%5Cleq%20n)

### Output Format

For each test case, print the chair number of the prisoner who receives the awful treat on a new line.

### Sample Input 0

    2
    5 2 1
    5 2 2

### Sample Output 0

    2
    3

### Explanation 0

In first query, there are **_n_ = 5** prisoners and **_m_ = 2** sweets. Distribution starts at seat number **_s_ = 1**. Prisoners in seats numbered **1** and **2** get sweets. Warn prisoner **2**.

In the second query, distribution starts at seat **2** so prisoners in seats **2** and **3** get sweets. Warn prisoner **3**.

### Sample Input 1

    2
    7 19 2
    3 7 3

### Sample Output 1

    6
    3

### Explanation 1

In the first test case, there are **_n_ = 7** prisoners, **_m_ = 19** sweets and they are passed out starting at chair **_s_ = 2**. The candies go all around twice and there are **5** more candies passed to each prisoner from seat **2** to seat **6**.

In the second test case, there are **_n_ = 3** prisoners, **_m_ = 7** candies and they are passed out starting at seat **_s_ = 3**. They go around twice, and there is one more to pass out to the prisoner at seat **3**.