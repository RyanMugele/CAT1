class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def mark_as_borrowed(self):
        if not self.is_borrowed:
            self.is_borrowed = True
            print(f"{self.title} by {self.author} is now marked as borrowed.")
        else:
            print(f"{self.title} is already borrowed.")

    def mark_as_returned(self):
        if self.is_borrowed:
            self.is_borrowed = False
            print(f"{self.title} by {self.author} has been returned.")
        else:
            print(f"{self.title} is not currently borrowed.")

class LibraryMember:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []

    def borrow_book(self, book):
        if book.is_borrowed:
            print(f"Sorry, {book.title} is currently unavailable.")
        else:
            book.mark_as_borrowed()
            self.borrowed_books.append(book)
            print(f"{self.name} has borrowed {book.title}.")

    def return_book(self, book):
        if book in self.borrowed_books:
            book.mark_as_returned()
            self.borrowed_books.remove(book)
            print(f"{self.name} has returned {book.title}.")
        else:
            print(f"{self.name} did not borrow {book.title}.")

    def list_borrowed_books(self):
        if not self.borrowed_books:
            print(f"{self.name} has no borrowed books.")
        else:
            print(f"{self.name} has borrowed the following books:")
            for book in self.borrowed_books:
                print(f"- {book.title} by {book.author}")


# Create some books and a library member for testing
book1 = Book("1984", "George Orwell")
book2 = Book("To Kill a Mockingbird", "Harper Lee")
member = LibraryMember("Alice", "M001")

# Interactive loop
def library_system():
    while True:
        print("\nLibrary Management System")
        print("1. Borrow a book")
        print("2. Return a book")
        print("3. List borrowed books")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            title = input("Enter the title of the book you want to borrow: ")
            if title == book1.title:
                member.borrow_book(book1)
            elif title == book2.title:
                member.borrow_book(book2)
            else:
                print("Book not found.")

        elif choice == "2":
            title = input("Enter the title of the book you want to return: ")
            if title == book1.title:
                member.return_book(book1)
            elif title == book2.title:
                member.return_book(book2)
            else:
                print("Book not found.")

        elif choice == "3":
            member.list_borrowed_books()

        elif choice == "4":
            print("Exiting the system.")
            break

        else:
            print("Invalid option. Please try again.")

# Run the interactive system
library_system()
