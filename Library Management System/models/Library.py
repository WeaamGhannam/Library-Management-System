import json
from models.LibraryItem import LibraryItem
from models.User import User
from Exception import Exception

class Library:
    def _init_(self, items_file="items.json", users_file="users.json"):
        self.items_file = items_file
        self.users_file = users_file
        self.items = self.load_items()
        self.users = self.load_users()

    def load_items(self):
        try:
            with open(self.items_file, "r") as file:
                return [LibraryItem.from_dict(item) for item in json.load(file)]
        except FileNotFoundError:
            print(f"Warning: '{self.items_file}' not found. Starting with empty items list.")
            return []
        except json.JSONDecodeError:
            print(f"Error: Could not parse '{self.items_file}'. Starting with empty items list.")
            return []

    def load_users(self):
        try:
            with open(self.users_file, "r") as file:
                return [User.from_dict(user) for user in json.load(file)]
        except FileNotFoundError:
            print(f"Warning: '{self.users_file}' not found. Starting with empty users list.")
            return []
        except json.JSONDecodeError:
            print(f"Error: Could not parse '{self.users_file}'. Starting with empty users list.")
            return []

    def save_items(self):
        file = None
        try:
            with open(self.items_file, "w") as file:
                json.dump([item.to_dict() for item in self.items], file, indent=4)
        except IOError:
            print(f"Error: Failed to save items to '{self.items_file}'.")
        finally:
         if file:
            file.close()
        print("Item save attempt completed.\n")

    def save_users(self):
        file = None
        try:
            with open(self.users_file, "w") as file:
                json.dump([user.to_dict() for user in self.users], file, indent=4)
        except IOError:
            print(f"Error: Failed to save users to '{self.users_file}'.")
        finally:
         if file:
            file.close()
        print("User save attempt completed.\n")

    def save_all(self):
        self.save_items()
        self.save_users()

    def add_item(self, item):
        self.items.append(item)
        print(f"Item '{item.title}' added.")

    def remove_item(self, item_id):
        item = self.get_item(item_id)
        if item:
            self.items.remove(item)
            print(f"Item '{item.title}' removed.")
        else:
            print(f"Error: Item '{item_id}' not found.")

    def add_user(self, user):
        self.users.append(user)
        print(f"User '{User.name}' added.")

    def remove_user(self, user_id):
        user = self.get_user(user_id)
        if user:
            self.users.remove(user)
            print(f"User '{User.name}' removed.")
        else:
            print(f"Error: User '{user_id}' not found.")

    def borrow_item(self, user_id, item_id):
        try:
            user = self.get_user(user_id)
            item = self.get_item(item_id)
            if not user or not item:
                raise ValueError("Invalid user ID or item ID.")

            if item.borrowed_by is not None:
                raise Exception(f"Item '{item.title}' is already borrowed by user ID {item.borrowed_by}.")

            item.borrowed_by = user_id
            User.borrowed_items.append(item_id)
            print(f"Item '{item.title}' borrowed by {User.name}.")

        except Exception as e:
            print("Borrowing Error:", e)
        finally:
            print("Barrow attempt completed.\n")

    def return_item(self, user_id, item_id):
        try:
            user = self.get_user(user_id)
            item = self.get_item(item_id)
            if not user or not item:
                raise ValueError("Invalid user ID or item ID.")

            if item.borrowed_by != user_id:
                raise Exception(f"Item '{item.title}' was not borrowed by {user.name}.")

            item.borrowed_by = None
            user.borrowed_items.remove(item_id)
            print(f"Item '{item.title}' returned by {user.name}.")

        except Exception as e:
            print("Return Error:", e)
        finally:
            print("return process completed.\n")

    def reserve_item(self, user_id, item_id):
        try:
            user = self.get_user(user_id)
            item = self.get_item(item_id)
            if not user or not item:
                raise ValueError("Invalid user ID or item ID.")

            if hasattr(item, "reserve") and callable(item.reserve):
                if item.reserved_by is not None:
                    raise Exception(f"Item '{item.title}' is already reserved by user ID {item.reserved_by}.")
                item.reserve(user)
            else:
                raise TypeError(f"Item '{item.title}' cannot be reserved.")

        except Exception as e:
            print("Reservation Error:", e)
        finally:
            print("Reservation process completed.\n")

    def get_item(self, item_id):
        return next((item for item in self.items if item.item_id == item_id), None)

    def get_user(self, user_id):
        return next((user for user in self.users if user.user_id == user_id), None)