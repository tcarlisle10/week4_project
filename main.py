from user_operations import add_user, display_all_users, view_user_details
from author_operations import add_author, display_all_authors, view_author_details
from book_operation import add_book, display_all_books, borrow_book, search_book, return_book
import os
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')




def library_system():
    clear()
    while True:
        action = input('''
Welcome to the Library Management System with Database Integration!
****
Main Menu:                       
1 - Book Operations
2 - User Operations
3 - Author Operations
4 - Quit
''')
        
        if action == '1':
            clear()
            while True:
                book_action = input('''
Welcome to the User Menu!
****
User Menu:                       
1 - Add a new book
2 - Borrow a book
3 - Return a book
4 - Search for a book
5 - Display all books
6 - Return to Main Menu
''')
                if book_action == '1':
                    clear()
                    add_book() 
                elif book_action == '2':
                    clear()
                    borrow_book()  
                elif book_action == '3':
                    clear()
                    return_book()  
                elif book_action == '4':
                    clear()
                    search_book()
                elif book_action == '5':
                    clear()
                    display_all_books()
                elif book_action == '6':
                    library_system()
        elif action == '2':
            clear()
            while True:
                user_action = input('''
Welcome to the User Menu!
****
User Menu:                       
1 - Add a new user
2 - View user details
3 - Display all users
4 - Return to Main Menu
''')
                if user_action == '1':
                    clear()
                    add_user()
                elif user_action == '2':
                    clear()
                    view_user_details() 
                elif user_action == '3':
                    clear()
                    display_all_users() 
                elif user_action == '4':
                    library_system()

        elif action == '3':
            clear()
            while True:
                author_action = input('''
Welcome to the Author Menu!
****
Author Menu:                       
1 - Add a new author
2 - View author details
3 - Display all authors
4 - Return to Main Menu
''')
                if author_action == '1':
                    clear()
                    add_author() 
                elif author_action == '2':
                    clear()
                    view_author_details() 
                elif author_action == '3':
                    clear()
                    display_all_authors()
                elif author_action == '4':
                    library_system() 
        elif action == '4':
            break
        

library_system()