import sys

if __name__ == "__main__":
    tests = int(sys.stdin.readline().strip())
    
    phone_book = dict()
    
    for i in range(tests):
        name, contacts = sys.stdin.readline().strip().split()
        phone_book[name] = contacts
    print(phone_book)
    
    query = sys.stdin.readline().strip()
    while query:
        phone_number = phone_book.get(query)
        if phone_number:
            print(query + "=" + phone_number)
        else:
            print("Not found")
        query = sys.stdin.readline().strip()
