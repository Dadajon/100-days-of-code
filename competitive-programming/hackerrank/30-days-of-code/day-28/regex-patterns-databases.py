import re

if __name__ == '__main__':
    N = int(input())

    pattern = r"@gmail\.com$"
    regex = re.compile(pattern)
    first_names = []

    for _ in range(N):
        first_name_email_id = input().split()
        first_name = first_name_email_id[0]
        email_id = first_name_email_id[1]

        if regex.search(email_id):
            first_names.append(first_name)

    first_names.sort()

    for name in first_names:
        print(name)