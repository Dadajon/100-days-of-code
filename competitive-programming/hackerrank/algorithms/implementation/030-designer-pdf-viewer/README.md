# Designer PDF Viewer

When you select a contiguous block of text in a PDF viewer, the selection is highlighted with a blue rectangle. In this PDF viewer, each word is highlighted independently. For example:

![image](https://s3.amazonaws.com/hr-challenge-images/22869/1471640108-6c01750b16-PDF-highighting.png)

In this challenge, you will be given a list of letter heights in the alphabet and a string. Using the letter heights given, determine the area of the rectangle highlight in ![equation](https://latex.codecogs.com/gif.latex?mm%5E2) assuming all letters are ![equation](https://latex.codecogs.com/gif.latex?1mm) wide.

For example, the highlighted ![equation](https://latex.codecogs.com/gif.latex?word%20%3D%20torn). Assume the heights of the letters are ![equation](https://latex.codecogs.com/gif.latex?t%3D2%2Co%3D1%2Cr%3D1) and ![equation](https://latex.codecogs.com/gif.latex?n%3D1). The tallest letter is **2** high and there are **4** letters. The hightlighted area will be ![equation](https://latex.codecogs.com/gif.latex?2%20%5Ctimes%204%20%3D%208mm%5E2) so the answer is **8**.

### Function Description

Complete the ***designer_pdf_viewer*** function in the editor below. It should return an integer representing the size of the highlighted area.

***designer_pdf_viewer*** has the following parameter(s):

- h: an array of integers representing the heights of each letter
- word: a string

### Input Format

The first line contains **26** space-separated integers describing the respective heights of each consecutive lowercase English letter, ASCII[a-z].
The second line contains a single word, consisting of lowercase English alphabetic letters.

### Constraints

- ![equation](https://latex.codecogs.com/gif.latex?1%20%5Cleq%20h%5B%3F%5D%20%5Cleq%207), where **?** is an English lowercase letter.
- ***word*** contains no more than **10** letters.

### Output Format

Print a single integer denoting the area in ![equation](https://latex.codecogs.com/gif.latex?mm%5E2) of highlighted rectangle when the given word is selected. Do not print units of measure.

### Sample Input 0

    1 3 1 3 1 4 1 3 2 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5
    abc

### Sample Output 0

    9

### Explanation 0

We are highlighting the word abc:

Letter heights are ![equation](https://latex.codecogs.com/gif.latex?a%3D1%2C%20b%3D3) and ![equation](https://latex.codecogs.com/gif.latex?c%3D1). The tallest letter, **b**, is ***3mm*** high. The selection area for this word is ![equation](https://latex.codecogs.com/gif.latex?3%20%5Ctimes%201mm%20%5Ctimes%203mm%20%3D%209mm%5E2).

**Note:** Recall that the width of each character is **1mm**.

### Sample Input 1

    1 3 1 3 1 4 1 3 2 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 7
    zaba

### Sample Output 1

    28

### Explanation 1

The tallest letter in ***zaba*** is ***z*** at **7**. The selection area for this word is ![equation](https://latex.codecogs.com/gif.latex?4%20%5Ctimes%201mm%20%5Ctimes%207mm%20%3D%2028mm%5E2).
