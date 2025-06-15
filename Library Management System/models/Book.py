from models.LibraryItem import LibraryItem 
from User import User

class Book(LibraryItem):
    def __init__(self, title, author, book_id):
        self.title = title
        self.author = author
        self.book_id = book_id
        self.available = True
    def getTitle(self):
        return self.title
    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, ID: {self.book_id}, Available: {self.available}"
    def reserve(self, user):
        if self.reserved_by is None:
            self.reserved_by = User.user_id
            print(f"Book '{self.title}' reserved by {User.name}.")
        else:
            print(f"Book '{self.title}' is already reserved by user ID {self.reserved_by}.")

