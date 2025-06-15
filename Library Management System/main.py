import json
from models.LibraryItem import LibraryItem
from models.Library import Library
from models.User import User
from models.Book import Book
from models.DVD import DVD
from models.Magazine import Magazine

# Load users from JSON
def load_users(file_path):
    try:
        with open(file_path, 'r') as f:
            data = json.load(f)
            return [User(**u) for u in data]
    except FileNotFoundError:
        return []

# Load items from JSON
def load_items(file_path):
    try:
        with open(file_path, 'r') as f:
            data = json.load(f)
            items = []
            for item in data:
                if item["type"] == "Book":
                    items.append(Book(item["title"], item["author"], item["genre"]))
                elif item["type"] == "DVD":
                    items.append(DVD(item["title"], item["author"], item["duration"]))
                elif item["type"] == "Magazine":
                    items.append(Magazine(item["title"], item["author"], item["issue_number"]))
            return items
    except FileNotFoundError:
        return []

# Save users to JSON
def save_users(users, file_path):
    with open(file_path, 'w') as f:
        data = [{"user_id": User.user_id, "name": User.name} for U in User]
        json.dump(data, f, indent=4)

# Save items to JSON
def save_items(items, file_path):
    def serialize_item(item):
        base = {
            "title": item.title,
            "author": item.author,
            "available": item.available
        }
        if isinstance(item, Book):
            base["type"] = "Book"
            base["genre"] = item.genre
        elif isinstance(item, DVD):
            base["type"] = "DVD"
            base["duration"] = item.duration
        elif isinstance(item, Magazine):
            base["type"] = "Magazine"
            base["issue_number"] = item.issue_number
        return base

    with open(file_path, 'w') as f:
        json.dump([serialize_item(i) for i in items], f, indent=4)


class main():
    LibraryItem = LibraryItem()
    Library = Library()
    LibraryItem.items = load_items("items.json")
    LibraryItem.user = load_users("users.json")

    def display_menu():
     print("\nLibrary Management System Menu:")
     print("1. View all available items")
     print("2. Search item by title or type")
     print("3. Register a new user")
     print("4. Borrow an item")
     print("5. Reserve an item")
     print("6. Return an item")
     print("7. Exit and Save")

    while True:
        display_menu()
        choice = input("Enter your choice (1-7): ")

        if choice == "1":
            print("\nAvailable Items:")
            for item in Library.items:
                if item.borrowed_by is None:
                    print(f"{item.item_id} - {item.title} ({type(item)._name_})")
        elif choice == "2":
            query = input("Enter item title or type (Book/DVD): ").strip().lower()
            found = False
            for item in Library.items:
                if query in item.title.lower() or query in type(item)._name_.lower():
                    print(f"{item.item_id} - {item.title} ({type(item)._name_})")
                    found = True
            if not found:
                print("No items matched your search.")
        elif choice == "3":
            user_id = input("Enter new user ID: ")
            name = input("Enter user name: ")
            Library.add_user(User(user_id, name))
        elif choice == "4":
            user_id = input("Enter your user ID: ")
            item_id = input("Enter item ID to borrow: ")
            Library.borrow_item(user_id, item_id)
        elif choice == "5":
            user_id = input("Enter your user ID: ")
            item_id = input("Enter item ID to reserve: ")
            Library.reserve_item(user_id, item_id)
        elif choice == "6":
            user_id = input("Enter your user ID: ")
            item_id = input("Enter item ID to return: ")
            Library.return_item(user_id, item_id)
        elif choice == "7":
            print("Saving and exiting...")
            Library.save_all()
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 7.")

if __name__ == "_main_":
    main()