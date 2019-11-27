if __name__ == "__main__":
    t = int(input().strip())
    
    for _ in range(t):
        n = int(input().strip())
        mul_of_3 = (n - 1) // 3
        mul_of_5 = (n - 1) // 5
        mul_of_15 = (n - 1) // 15
        result = (3 * mul_of_3 * (mul_of_3 + 1) // 2
                  + 5 * mul_of_5 * (mul_of_5 + 1) // 2
                  - 15 * mul_of_15 * (mul_of_15 + 1) // 2)
        print(result)
