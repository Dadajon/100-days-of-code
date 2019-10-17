
def solve(cost, tip_p, tax_p):
    cost = cost
    tip = cost * tip_p / 100
    tax = cost * tax_p / 100
    result = round(cost + tip + tax)
    print(result)


if __name__ == '__main__':
    meal_cost = float(input())

    tip_percent = int(input())

    tax_percent = int(input())

    solve(meal_cost, tip_percent, tax_percent)
