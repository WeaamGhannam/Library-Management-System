from abc import ABC, abstractmethod
class LibraryItem(ABC):
    def __init__(self,title,author):
        self.books = {}
        self.title=title
        self.author=author
        self.available=True

    @abstractmethod
    def display_info(self):
        pass

    def check_availability(self):
        return self.available

    def add_book(self, book):
        if book.book_id not in self.books:
            self.books[book.book_id] = book
            print(f"Book '{book.title}' added successfully.")
        else:
            print(f"Book with ID '{book.book_id}' already exists.")

    def display_books(self):
        if not self.books:
            print("No books in the library.")
            return
        for book_id, book in self.books.items():
            print(book)
    
    def search_book(self, query):
        results = []
        for book in self.books.values():
            if query.lower() in book.title.lower() or query.lower() in book.author.lower():
                results.append(book)
        if results:
            for book in results:
                print(book)
        else:
            print(f"No books found matching '{query}'.")

    def borrow_book(self, book_id):
        if book_id in self.books:
            book = self.books[book_id]
            if book.available:
                book.available = False
                print(f"Book '{book.title}' borrowed successfully.")
            else:
                print(f"Book '{book.title}' is currently unavailable.")
        else:
            print(f"Book with ID '{book_id}' not found.")

    def return_book(self, book_id):
        if book_id in self.books:
            book = self.books[book_id]
            if not book.available:
                book.available = True
                print(f"Book '{book.title}' returned successfully.")
            else:
                print(f"Book '{book.title}' is already available.")
        else:
            print(f"Book with ID '{book_id}' not found.")
    def to_dict(self):
        return {
            "item_id": self.item_id,
            "title": self.title,
            "item_type": self.item_type,
            "borrowed_by": self.borrowed_by,
            "reserved_by": self.reserved_by
        }

