Requirements:
All LibraryItem and User instances should initially be read from respective data files (e.g.,
items.json, users.json).
When the administrator adds a new item or user, the updated information should be saved back to
these files upon exiting the system.
1. Abstract Classes and Interfaces:
Create an abstract class LibraryItem with attributes like title, author, and methods like
display_info() and check_availability().
Subclasses: Book, Magazine, DVD each with specific attributes and behaviors.
Create an interface-like abstract class Reservable with method reserve(user) and implement
it in Book and DVD.
2. Class Composition and Relationships:
Create a User class with attributes like user_id, name, borrowed_items.
Create a Library class to manage items and users. It should allow:
Adding/removing items
Adding/removing users
Borrowing and returning items
Reserving items using the Reservable interface

3. Exception Handling:
Handle the following scenarios with try-except:
Borrowing an unavailable item
Reserving an item that is already reserved
Invalid user inputs (nonexistent users or items)
File errors when saving/loading data (optional bonus)

W6_Abstract_Interface_Exeception.md 2025-05-30

11 / 12
Use finally to ensure consistent application flow.
4. Custom Exceptions:
Create and raise custom exceptions like ItemNotAvailableError, UserNotFoundError,
ItemNotFoundError.
5. File Structure:
Organize your project using multiple files:
main.py: contains the CLI interface or main loop
models/: directory with library_item.py, book.py, user.py, etc.
exceptions/: directory with custom exceptions

6. System Interaction Scenario:
Upon launching main.py, the system should:
Load existing items from items.json and users from users.json.
Present a CLI menu with options:
1. View all available items
2. Search item by title or type
3. Register a new user
4. Borrow an item
5. Reserve an item
6. Return an item
7. Exit and Save
