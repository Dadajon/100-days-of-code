# Drawing books

Brie’s Drawing teacher asks her class to open their books to a page number. Brie can either start turning pages from the front of the book or from the back of the book. She always turns pages one at a time. When she opens the book, page  is always on the right side:

![](https://s3.amazonaws.com/hr-challenge-images/0/1481920803-d2b54f38f0-book.png)

When she flips page ***1***, she sees pages ***2*** and ***3*** Each page except the last page will always be printed on both sides. The last page may only be printed on the front, given the length of the book. If the book is ***n*** pages long, and she wants to turn to page ***p***, what is the minimum number of pages she will turn? She can start at the beginning or the end of the book.

Given ***n*** and ***p***, find and print the minimum number of pages Brie must turn in order to arrive at page ***p***.

### Function Description
Complete the ***page_count*** function in the editor below. It should return the minimum number of pages Brie must turn.

***page_count*** has the following parameter(s):

***num_p***: the number of pages in the book
***goal_p***: the page number to turn to
Input Format

The first line contains an integer ***num_p***, the number of pages in the book.
The second line contains an integer, ***goal_p***, the page that Brie's teacher wants her to turn to.

### Constraints
* ![](https://latex.codecogs.com/gif.latex?1%20%5Cleqslant%20n%20%5Cleqslant%2010%5E5)
* ![](https://latex.codecogs.com/gif.latex?1%20%5Cleqslant%20p%20%5Cleqslant%20n)

### Output Format

Print an integer denoting the minimum number of pages Brie must turn to get to page ***p***.

### Sample Input 0
```
6
2
```

### Sample Output 0
```
1
```

### Explanation 0

If Brie starts turning from page **1**, she only needs to turn **1** page:

![](https://s3.amazonaws.com/hr-challenge-images/22564/1467398713-1decf68d06-UntitledDiagram6.png)

If Brie starts turning from page **6**, she needs to turn **2** pages:

![](https://s3.amazonaws.com/hr-challenge-images/22564/1467397150-52d0a8213b-UntitledDiagram3.png)

Because we want to print the minumum number of page turns, we print **1** as our answer.

### Sample Input 1
```
5
4
```

### Sample Output 1
```
0
```

### Explanation 1

If Brie starts turning from page **1**, she needs to turn **2** pages:

![](https://s3.amazonaws.com/hr-challenge-images/22564/1467398281-32b69f6fa9-UntitledDiagram4.png)

If Brie starts turning from page **5**, she doesn't need to turn any pages:

![](https://s3.amazonaws.com/hr-challenge-images/22564/1467398392-5d9ac72e45-UntitledDiagram5.png)

Because we want to print the minimum number of page turns, we print **0** as our answer.