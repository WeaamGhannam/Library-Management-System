class User:
    def _init_(self, user_id, name):
        self.user_id = user_id
        self.name = name
        self.borrowed_items = []

    def borrow_item(self, item):
        self.borrowed_items.append(item)

    def return_item(self, item):
        if item in self.borrowed_items:
            self.borrowed_items.remove(item)

    def _str_(self):
        return f"{self.name} (ID: {self.user_id})"