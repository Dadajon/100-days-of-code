# Jumping on the Clouds: Revisited

Aerith is playing a cloud hopping game. In this game, there are sequentially numbered clouds that can be thunderheads or cumulus clouds. Her character must jump from cloud to cloud until it reaches the start again.

To play, Aerith is given an array of clouds, **_c_** and an energy level **_e_ = 100**. She starts from **_c_[0]** and uses **1** unit of energy to make a jump of size **_k_** to cloud **_c_[(_i_+_k_)%_n_]**. If Aerith lands on a thundercloud, **_c_[_i_] = 1**, her energy (**_e_**) decreases by **2** additional units. The game ends when Aerith lands back on cloud **0**.

Given the values of **_n_**, **_k_**, and the configuration of the clouds as an array **_c_**, can you determine the final value of **_e_** after the game ends?

For example, give **_c_ = [0, 0, 1, 0]** and **_k_ = 2**, the indices of her path are **0 -> 2 -> 0**. Her energy level reduces by **1** for each jump to **98**. She landed on one thunderhead at an additional cost of **2** energy units. Her final energy level is **96**.

**Note:** Recall that ***%*** refers to the [modulo operation](https://en.wikipedia.org/wiki/Modulo_operation). In this case, it serves to make the route circular. If Aerith is at **_c_[_n_ - 1]** and jumps **1**, she will arrive at **_c_[0]**.

### Function Description

Complete the **_jumping_on_clouds_** function in the editor below. It should return an integer representing the energy level remaining after the game.

**_jumping_on_clouds_** has the following parameter(s):

- cloud_types: an array of integers representing cloud types
- jump_length: an integer representing the length of one jump

### Input Format

The first line contains two space-separated integers, **_n_** and **_k_**, the number of clouds and the jump distance.

The second line contains **_n_** space-separated integers **_c_[_i_]** where ![equation](https://latex.codecogs.com/svg.latex?%5Cinline%200%20%5Cleq%20i%20%3C%200). Each cloud is described as follows:

- If **_c_[_i_] = 0**, then cloud **_i_** is a cumulus cloud.
- If **_c_[_i_] = 1**, then cloud **_i_** is a thunderhead.

### Constraints

- ![equation](https://latex.codecogs.com/svg.latex?%5Cinline%202%20%5Cleq%20n%20%5Cleq%2025)
- ![equation](https://latex.codecogs.com/svg.latex?%5Cinline%201%20%5Cleq%20k%20%5Cleq%20n)
- ![equation](https://latex.codecogs.com/svg.latex?%5Cinline%20n%20%5C%25%20k%20%3D%200)
- ![equation](https://latex.codecogs.com/svg.latex?%5Cinline%20c%5Bi%5D%20%5Cin%20%5C%7B0%2C%201%5C%7D)

### Output Format

Print the final value of **_e_** on a new line.

### Sample Input 0

    8 2
    0 0 1 0 0 1 1 0

### Sample Output 0

    92

### Explanation

In the diagram below, red clouds are thunderheads and purple clouds are cumulus clouds:

![image](https://s3.amazonaws.com/hr-challenge-images/0/1462454878-26f414ec0f-may4.png)

Observe that our thunderheads are the clouds numbered **2**, **5**, and **6**. Aerith makes the following sequence of moves:

1. Move: ![move](https://latex.codecogs.com/svg.latex?%5Cinline%200%20%5Crightarrow%202), Energy: ![energy](https://latex.codecogs.com/svg.latex?%5Cinline%20e%20%3D%20100%20-%201%20-%202%20%3D%2097).
2. Move: ![move](https://latex.codecogs.com/svg.latex?%5Cinline%202%20%5Crightarrow%204), Energy: ![energy](https://latex.codecogs.com/svg.latex?%5Cinline%20e%20%3D%2097%20-%201%20%3D%2096).
3. Move: ![move](https://latex.codecogs.com/svg.latex?%5Cinline%204%20%5Crightarrow%206), Energy: ![energy](https://latex.codecogs.com/svg.latex?%5Cinline%20e%20%3D%2096%20-%201%20-%202%20%3D%2093).
4. Move: ![move](https://latex.codecogs.com/svg.latex?%5Cinline%206%20%5Crightarrow%200), Energy: ![energy](https://latex.codecogs.com/svg.latex?%5Cinline%20e%20%3D%2093%20-%201%20%3D%2092).


### Sample Input 1

    10 3
    1 1 1 0 1 1 0 0 0 0

### Sample Output 1

    80
