from user_operations import display_all_users

class Book:
    def __init__(self, title, author, genre, publication_date):
        self.__title = title
        self.__author = author
        self.__genre = genre
        self.__publication_date = publication_date
        self.__is_available = True

    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author

    def get_genre(self):
        return self.__genre

    def get_publication_date(self):
        return self.__publication_date

    def is_available(self):
        return self.__is_available

    def borrow(self):
        if self.__is_available:
            self.__is_available = False
            return True
        else:
            return False

    def return_book(self):
        if not self.__is_available:
            self.__is_available = True
            return True
        else:
            return False
        
books = []
display_all_users()
users = []


def add_book():
    title = input("Enter book title: ")
    author_name = input("Enter author name: ")
    genre = input("Enter genre: ")
    publication_date = input("Enter publication date (MM-DD-YYYY): ")
    books.append(Book(title, author_name, genre, publication_date))
    print("Book has been successfully added!")

def return_book():
    title = input("Enter book title to return: ")
    user_id = input("Enter your library ID: ")
    for book in books:
        if book.get_title() == title:
            if book.return_book():
                for user in users:
                    if user.get_library_id() == user_id:
                        if user.return_book(title):
                            print("Book returned successfully!")
                            return
                        else:
                            print("You haven't borrowed this book.")
                            return
                print("User not found.")
                return
            else:
                print("Book is already available.")
                return
    print("Book not found.")

def display_all_books():
    if not books:
        print("No books in the library yet.")
    else:
        for book in books:
            print(f"Title: {book.get_title()}, Available: {book.is_available()}")

def search_book():
    title = input("Enter book title to search: ")
    for book in books:
        if book.get_title() == title:
            print(f"Title: {book.get_title()}")
            print(f"Author: {book.get_author()}")
            print(f"Genre: {book.get_genre()}")
            print(f"Publication Date: {book.get_publication_date()}")
            print(f"Available: {book.is_available()}")
            return
    print("Book not found.")

def borrow_book():
    title = input("Enter book title to borrow: ")
    user_id = input("Enter your library ID: ")
    for book in books:
        if book.get_title() == title:
            if book.borrow():
                for user in users:
                    if user.get_library_id() == user_id:
                        user.borrow_book(title)
                        print("Book borrowed successfully!")
                        return
                print("User not found.")
                return
            else:
                print("Book is not available.")
                return
    print("Book not found.")