from models.book import *

book1 = Book("The Shining", "Stephen King", "Horror",False)
book2 = Book("Harry Potter", "J.K Rowling", "Adventure", True)
book3 = Book("The Hobbit", "J.R.R Tolkien", "Fantasy",False)

books =[book1, book2, book3]

def add_book(book):
    books.append(book)

def remove_book(index):
    books.pop(index)