
# Department Book Exchange
# Module: Add & View Books

books = []

# Function to add a new book
def addBook():

    print("\n----- ADD NEW BOOK -----")

    book_id = int(input("Enter Book ID: "))

    # Check for duplicate Book ID
    for book in books:
        if book["book_id"] == book_id:
            print("Book ID already exists!")
            return

    book_name = input("Enter Book Name: ")
    author = input("Enter Author Name: ")
    student_id = int(input("Enter Student ID: "))
    department = input("Enter Department: ")

    new_book = {
        "book_id": book_id,
        "book_name": book_name,
        "author": author,
        "student_id": student_id,
        "department": department,
        "status": "Available"
    }

    books.append(new_book)

    print("\nBook added successfully!")
    print("Book Status: Available")


# Function to view all books
def viewBooks():

    print("\n----- ALL BOOKS -----")

    if len(books) == 0:
        print("No books available.")
        return

    for book in books:
        print("--------------------------------")
        print("Book ID     :", book["book_id"])
        print("Book Name   :", book["book_name"])
        print("Author      :", book["author"])
        print("Student ID  :", book["student_id"])
        print("Department  :", book["department"])
        print("Status      :", book["status"])


# Main menu for testing your module
while True:

    print("\n===== DEPARTMENT BOOK EXCHANGE =====")
    print("1. Add Book")
    print("2. View Books")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        addBook()

    elif choice == "2":
        viewBooks()

    elif choice == "3":
        print("Thank you!")
        break

    else:
        print("Invalid choice. Try again.")
