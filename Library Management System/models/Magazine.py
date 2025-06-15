from models.LibraryItem import LibraryItem 

class Magazine(LibraryItem):
    def _init_(self, title, author, issue_number):
        super()._init_(title, author)
        self.issue_number = issue_number

    def display_info(self):
        print(f"Magazine: {self.title} - Issue {self.issue_number} by {self.author}")