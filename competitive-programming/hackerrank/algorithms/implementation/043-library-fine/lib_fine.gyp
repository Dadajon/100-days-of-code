def library_fine(return_day, return_month, return_year,
                 expect_day, expect_month, expect_year):
    if return_year > expect_year:
        return 10000
    if return_year < expect_year:
        return 0
    if return_month > expect_month:
        return 500 * (return_month - expect_month)
    if return_month < expect_month:
        return 0
    if return_day > expect_day:
        return 15 * (return_day - expect_day)
    return 0


if __name__ == '__main__':
    returned_date = input().split()
    returned_day = int(returned_date[0])
    returned_month = int(returned_date[1])
    returned_year = int(returned_date[2])

    expected_date = input().split()
    expected_day = int(expected_date[0])
    expected_month = int(expected_date[1])
    expected_year = int(expected_date[2])

    result = library_fine(returned_day, returned_month, returned_year,
                          expected_day, expected_month, expected_year)

    print(str(result) + '\n')
