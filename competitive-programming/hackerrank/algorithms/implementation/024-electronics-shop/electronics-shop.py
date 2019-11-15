def get_money_spent(keyboards, drives, b):
    """
    Given the price lists for the store's keyboards and USB drives, and Monica's budget, find and print the amount of money Monica will spend.
    If she doesn't have enough money to both a keyboard and a USB drive, print -1 instead. She will buy only the two required items.
    :param keyboards: an array of integers representing keyboard prices
    :param drives: an array of integers representing drive prices
    :param b: the units of currency in Monica's budget
    :return: the maximum total price for the two items within Monica's budget, or -1 if she cannot afford both items.
    """
    max_spending = -1
    for keyboard_price in keyboards:
        for drive_price in drives:
            if max_spending < keyboard_price + drive_price <= b:
                max_spending = keyboard_price + drive_price
    return max_spending


if __name__ == '__main__':
    bnm = input().split()

    budget = int(bnm[0])
    keyboard_models = int(bnm[1])
    drive_models = int(bnm[2])

    keyboard_prices = list(map(int, input().rstrip().split()))
    drive_prices = list(map(int, input().rstrip().split()))

    money_spent = get_money_spent(keyboard_prices, drive_prices, budget)

    print(str(money_spent) + '\n')
