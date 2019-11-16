# Cats and a mouse

Two cats and a mouse are at various positions on a line. You will be given their starting positions. Your task is to determine which cat will reach the mouse first, assuming the mouse doesn't move and the cats travel at equal speed. If the cats arrive at the same time, the mouse will be allowed to move and it will escape while they fight.

You are given ***q*** queries in the form of ***x***, ***y***, and ***z*** representing the respective positions for cats ***A*** and ***B***, and for mouse ***C***. Complete the function ***cat_and_mouse*** to return the appropriate answer to each query, which will be printed on a new line.

If cat ***A*** catches the mouse first, print *Cat A*.
If cat  catches the mouse first, print *Cat B*.
If both cats reach the mouse at the same time, print *Mouse C* as the two cats fight and mouse escapes.

For example, cat ***A*** is at position ***x = 2*** and cat ***B*** is at ***y = 5***. If mouse ***C*** is at position ***z = 4***, it is ***2*** units from cat ***A*** and ***1*** unit from cat ***B***. Cat ***B*** will catch the mouse.

### Function Description

Complete the ***cat_and_mouse*** function in the editor below. It should return one of the three strings as described.

***cat_and_mouse*** has the following parameter(s):

* ***cat_x***: an integer, Cat ***A***'s position
* ***cat_y***: an integer, Cat ***B***'s position
* ***mouse_z***: an integer, Mouse 's position

### Input Format

The first line contains a single integer, ***q***, denoting the number of queries.

Each of the ***q*** subsequent lines contains three space-separated integers describing the respective values of ***cat_x*** (cat ***A***'s location), ***cat_y*** (cat ***B***'s location), and ***mouse_z*** (mouse ***C***'s location).

### Constraints
* ![](https://latex.codecogs.com/gif.latex?1%20%5Cleq%20q%20%5Cleq%20100)
* ![](https://latex.codecogs.com/gif.latex?1%20%5Cleq%20cat%5C_%20x%2C%20cat%5C_y%2Cmouse%5C_z%20%5Cleq%20100)

### Output Format

For each query, return *Cat A* if cat ***A*** catches the mouse first, *Cat B* if cat ***B*** catches the mouse first, or *Mouse C* if the mouse escapes.

### Sample Input 0
```
2
1 2 3
1 3 2
```

### Sample Output 0
```
Cat B
Mouse C
```

### Explanation 0
Query 0: The positions of the cats and mouse are shown below:

![](https://s3.amazonaws.com/hr-challenge-images/0/1480434477-7418fccf34-cat.png)

Cat ***B*** will catch the mouse first, so we print *Cat B* on a new line.

Query 1: In this query, cats ***A*** and ***B*** reach mouse ***C*** at the exact same time:

![](https://s3.amazonaws.com/hr-challenge-images/0/1480434557-601bef86ba-cat1.png)

Because the mouse escapes, we print *Mouse C* on a new line.