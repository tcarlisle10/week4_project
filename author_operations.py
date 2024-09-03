class Author:
    def __init__(self, name, biography):
        self.__name = name
        self.__biography = biography

    def get_name(self):
        return self.__name

    def get_biography(self):
        return self.__biography
    

authors = []

def add_author():
    name = input("Enter author name: ")
    biography = input("Enter author biography: ")
    authors.append(Author(name, biography))
    print("Author has been successfully added!")

#-----------------------------------------------------------------------------#

def display_all_authors():
    if not authors:
        print("No authors found in library.")
    else:
        for author in authors:
            print(f"Name: {author.get_name()}")

#-----------------------------------------------------------------------------#

def view_author_details():
    name = input("Enter author name: ")
    for author in authors:
        if author.get_name() == name:
            print(f"Name: {author.get_name()}")
            print(f"Biography: {author.get_biography()}")
            return
    print("Author not found.")