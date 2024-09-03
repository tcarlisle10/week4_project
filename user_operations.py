class User:
    def __init__(self, name, library_id):
        self.__name = name
        self.__library_id = library_id
        self.__borrowed_books = []

    def get_name(self):
        return self.__name

    def get_library_id(self):
        return self.__library_id

    def get_borrowed_books(self):
        return self.__borrowed_books

    def borrow_book(self, book_title):
        self.__borrowed_books.append(book_title)

    def return_book(self, book_title):
        if book_title in self.__borrowed_books:
            self.__borrowed_books.remove(book_title)
            return True
        else:
            return False


users = []

def add_user():
    name = input("Enter user name: ")
    library_id = input("Enter library ID: ")
    users.append(User(name, library_id))
    print("User has been successfully added!")

#-----------------------------------------------------------------------------#

def display_all_users():
    if not users:
        print("No users in the library yet.")
    else:
        for user in users:
            print(f"Name: {user.get_name()}, Library ID: {user.get_library_id()}")     

#-----------------------------------------------------------------------------#

def view_user_details():
    library_id = input("Enter library ID: ")
    for user in users:
        if user.get_library_id() == library_id:
            print(f"Name: {user.get_name()}")
            print(f"Library ID: {user.get_library_id()}")
            print(f"Borrowed Books: {user.get_borrowed_books()}")
            return
    print("User not found.")