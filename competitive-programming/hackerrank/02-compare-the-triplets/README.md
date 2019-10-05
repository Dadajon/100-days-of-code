# **Compare the Triplets**

Alice and Bob each created one problem for HackerRank. A reviewer rates the two challenges, awarding points on a scale from **1** to **100** for three categories: problem clarity, originality, and difficulty.

We define the rating for Alice's challenge to be the triplet ![](https://latex.codecogs.com/svg.latex?a%3D%20%5Cleft%20%28%20a%5Cleft%20%5B%200%20%5Cright%20%5D%20%5Cright%20%2Ca%5Cleft%20%5B%201%20%5Cright%20%5D%2Ca%5Cleft%20%5B%202%20%5Cright%20%5D%29%2C), and the rating for Bob's challenge to be the triplet ![](https://latex.codecogs.com/svg.latex?b%3D%20%5Cleft%20%28%20b%5Cleft%20%5B%200%20%5Cright%20%5D%20%5Cright%20%2Cb%5Cleft%20%5B%201%20%5Cright%20%5D%2Cb%5Cleft%20%5B%202%20%5Cright%20%5D%29%2C).

Your task is to find their comparison points by comparing ![](https://latex.codecogs.com/svg.latex?a%5Cleft%20%5B%200%20%5Cright%20%5D) with ![](https://latex.codecogs.com/svg.latex?b%5Cleft%20%5B%200%20%5Cright%20%5D), ![](https://latex.codecogs.com/svg.latex?a%5Cleft%20%5B%201%20%5Cright%20%5D) with ![](https://latex.codecogs.com/svg.latex?b%5Cleft%20%5B%201%20%5Cright%20%5D), and ![](https://latex.codecogs.com/svg.latex?a%5Cleft%20%5B%202%20%5Cright%20%5D) with ![](https://latex.codecogs.com/svg.latex?b%5Cleft%20%5B%202%20%5Cright%20%5D).

* If ![](https://latex.codecogs.com/svg.latex?a%5Cleft%20%5B%20i%20%5Cright%20%5D%3E%20b%5Cleft%20%5B%20i%5Cright%20%5D), then Alice is awarded **1** point.
* If ![](https://latex.codecogs.com/svg.latex?a%5Cleft%20%5B%20i%20%5Cright%20%5D%3C%20b%5Cleft%20%5B%20i%5Cright%20%5D), then Bob is awarded **1** point.
* If ![](https://latex.codecogs.com/svg.latex?a%5Cleft%20%5B%20i%20%5Cright%20%5D%3D%20b%5Cleft%20%5B%20i%5Cright%20%5D), then neither person receives a point.

Comparison points is the total points a person earned.

Given ***a*** and ***b***, determine their respective comparison points.

For example, ![](https://latex.codecogs.com/svg.latex?a%3D%20%5Cleft%20%5B%201%2C2%2C3%20%5Cright%20%5D) and ![](https://latex.codecogs.com/svg.latex?b%3D%20%5Cleft%20%5B%203%2C2%2C1%20%5Cright%20%5D). For elements ![](https://latex.codecogs.com/svg.latex?0), Bob is awarded a point because ![](https://latex.codecogs.com/svg.latex?a%5Cleft%20%5B%200%20%5Cright%20%5D%3C%20b%5Cleft%20%5B%200%5Cright%20%5D). For the equal elements ![](https://latex.codecogs.com/svg.latex?a%5Cleft%5B1%20%5Cright%20%5D) and ![](https://latex.codecogs.com/svg.latex?b%5Cleft%5B1%20%5Cright%20%5D), no points are earned. Finally, for elements ![](https://latex.codecogs.com/svg.latex?2), ![](https://latex.codecogs.com/svg.latex?a%5Cleft%5B2%20%5Cright%20%5D%3Eb%5B2%5D) so Alice receives a point. Your return array would be ![](https://latex.codecogs.com/svg.latex?%5B1%2C1%5D) with Alice's score first and Bob's second.

## **Function Description**

Complete the function compareTriplets in the editor below. It must return an array of two integers, the first being Alice's score and the second being Bob's.

***compareTriplets*** has the following parameter(s):

* a: an array of integers representing Alice's challenge rating
* b: an array of integers representing Bob's challenge rating

## **Input Format**

The first line contains **3** space-separated integers, ![](https://latex.codecogs.com/svg.latex?a%5B0%5D), ![](https://latex.codecogs.com/svg.latex?a%5B1%5D), and ![](https://latex.codecogs.com/svg.latex?a%5B2%5D), describing the respective values in triplet ![](https://latex.codecogs.com/svg.latex?a).
The second line contains **3** space-separated integers, ![](https://latex.codecogs.com/svg.latex?b%5B0%5D), ![](https://latex.codecogs.com/svg.latex?b%5B1%5D), and ![](https://latex.codecogs.com/svg.latex?b%5B2%5D), describing the respective values in triplet ![](https://latex.codecogs.com/svg.latex?b).

## **Constraints**
* ![](https://latex.codecogs.com/svg.latex?1%5Cleqslant%20a%5Bi%5D%5Cleqslant100)
* ![](https://latex.codecogs.com/svg.latex?1%5Cleqslant%20b%5Bi%5D%5Cleqslant100)

## **Output Format**

Return an array of two integers denoting the respective comparison points earned by Alice and Bob.

### **Sample Input 0**

    5 6 7
    3 6 10

### **Sample Output 0**

    1 1

### **Explanation 0**

In this example:
  
* ![](https://latex.codecogs.com/svg.latex?a%3D%28a%5B0%5D%2Ca%5B1%5D%2Ca%5B2%5D%29%3D%285%2C6%2C7%29)
* ![](https://latex.codecogs.com/svg.latex?b%3D%28b%5B0%5D%2Cb%5B1%5D%2Cb%5B2%5D%29%3D%283%2C6%2C10%29)

Now, let's compare each individual score:

* ![](https://latex.codecogs.com/svg.latex?a%5B0%5D%3Eb%5B0%5D), so Alice receives **1** point.
* ![](https://latex.codecogs.com/svg.latex?a%5B1%5D%3Db%5B1%5D), so nobody receives a point.
* ![](https://latex.codecogs.com/svg.latex?a%5B2%5D%3Cb%5B2%5D), so Bob receives **1** point.

Alice's comparison score is **1**, and Bob's comparison score is **1**. Thus, we return the array ![](https://latex.codecogs.com/svg.latex?%5B1%2C1%5D).

### **Sample Input 1**

    17 28 30
    99 16 8

### **Sample Output 1**

    2 1

### **Explanation 1**

Comparing the ![](https://latex.codecogs.com/svg.latex?0%5E%7Bth%7D) elements, ![](https://latex.codecogs.com/svg.latex?17%3C99) so Bob receives a point.
Comparing the ![](https://latex.codecogs.com/svg.latex?1%5E%7Bst%7D) and ![](https://latex.codecogs.com/svg.latex?2%5E%7Bnd%7D) elements, ![](https://latex.codecogs.com/svg.latex?28%3E16) and ![](https://latex.codecogs.com/svg.latex?30%3E8) so Alice receives two points.

The return array is ![](https://latex.codecogs.com/svg.latex?%5B2%2C1%5D).