
def calculate_fine(return_day, return_month, return_year, exp_day, exp_month, exp_year):
    if return_year < exp_year:
        return 0
    elif return_year == exp_year:
        if return_month < exp_month:
            return 0
        elif return_month == exp_month:
            if return_day <= exp_day:
                return 0
            else:
                return (return_day - exp_day) * 15
        else:
            return (return_month - exp_month) * 500
    else:
        return 10000


if __name__ == "__main__":
    returned_day, returned_month, returned_year = [int(item) for item in input().rstrip().split()]
    expected_day, expected_month, expected_year = [int(item) for item in input().rstrip().split()]

    fine = calculate_fine(returned_day, returned_month, returned_year, expected_day, expected_month, expected_year)
    print(fine)