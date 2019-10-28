from abc import ABCMeta, abstractmethod
class Book(object, metaclass=ABCMeta):
    def __init__(self,title,author):
        self.title=title
        self.author=author   
    @abstractmethod
    def display(): pass


class MyBook(Book):
    def __init__(self, my_book_title, my_book_author, my_book_price):
        super().__init__(title=my_book_title, author=my_book_author)
        self.my_book_price = my_book_price

    def display(self):
        print("Title:", self.title)
        print("Author:", self.author)
        print("Price:", self.my_book_price)


title=input()
author=input()
price=int(input())
new_novel=MyBook(title,author,price)
new_novel.display()