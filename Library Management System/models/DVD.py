from models.LibraryItem import LibraryItem 
from models.Reservable import Reservable
class DVD(LibraryItem, Reservable):
    def _init_(self, title, author, duration):
        super()._init_(title, author)
        self.duration = duration  # in minutes

    def display_info(self):
        print(f"DVD: {self.title} by {self.author} - Duration: {self.duration} minutes")

    def reserve(self, user):
        if self.available:
            self.available = False
            print(f"{user} has reserved the DVD '{self.title}'.")
        else:
            print(f"Sorry, the DVD '{self.title}' is currently unavailable.")