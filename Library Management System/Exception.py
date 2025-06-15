class LibraryError(Exception):
    pass
class UserNotFoundError(LibraryError):
    def __init__(self, user_id):
        super().__init__(f"{user_id}was not found")
class ItemNotFoundError(LibraryError):
    def __init__(self, item_id):
        super().__init__(f"{item_id}was not found")
class ItemNotAvailableError(LibraryError):
    def __init__(self, title):
        super().__init__(f"{title} is currently unavailable")