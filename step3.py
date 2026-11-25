# ==================================
# MODULE: REQUEST A BOOK
# Department Book Exchange
# Phase 1 - Procedural Programming
# File: step3.py
# ==================================

# Sample student records
students = {
    "S101": "Rahul",
    "S102": "Priya",
    "S103": "Anita",
    "S104": "Kiran"
}

# Sample book listings
books = {
    "B001": {
        "title": "Python Crash Course",
        "owner_id": "S103",
        "owner": "Anita",
        "status": "Available"
    },
    "B002": {
        "title": "Data Structures",
        "owner_id": "S101",
        "owner": "Rahul",
        "status": "Available"
    },
    "B003": {
        "title": "Database Management",
        "owner_id": "S102",
        "owner": "Priya",
        "status": "Requested"
    }
}

# Stores all book requests
request_log = []


def show_available_books():
    """Display all books whose status is Available."""
    print("\n--- Available Books ---")
    found = False

    for book_id, book in books.items():
        if book["status"] == "Available":
            print(f"\nBook ID: {book_id}")
            print(f"Title: {book['title']}")
            print(f"Owner: {book['owner']}")
            print(f"Owner ID: {book['owner_id']}")
            found = True

    if not found:
        print("No books are currently available.")


def request_book():
    """Validate the student and book, update status, and log the request."""
    print("\n--- Request a Book ---")
    show_available_books()

    student_id = input("\nEnter your Student ID: ").strip().upper()

    if student_id not in students:
        print("Error: Invalid Student ID!")
        return

    book_id = input("Enter the Book ID to request: ").strip().upper()

    if book_id not in books:
        print("Error: Book ID not found!")
        return

    book = books[book_id]

    if book["status"] != "Available":
        print("Sorry! This book is not available.")
        return

    if book["owner_id"] == student_id:
        print("You cannot request your own book!")
        return

    # Update the book status
    book["status"] = "Requested"

    # Add the request to the log
    request = {
        "student_id": student_id,
        "student_name": students[student_id],
        "book_id": book_id,
        "book_title": book["title"],
        "owner_id": book["owner_id"],
        "owner": book["owner"],
        "status": "Requested"
    }
    request_log.append(request)

    print("\nBook requested successfully!")
    print("Student:", students[student_id])
    print("Book:", book["title"])
    print("Owner:", book["owner"])
    print("Status: Requested")


def view_request_log():
    """Display all recorded book requests."""
    print("\n--- Request Log ---")

    if not request_log:
        print("No requests have been made.")
        return

    for request in request_log:
        print(f"\nStudent: {request['student_name']} ({request['student_id']})")
        print(f"Book: {request['book_title']} ({request['book_id']})")
        print(f"Owner: {request['owner']}")
        print(f"Status: {request['status']}")
        print("------------------------")


# Run this module independently for testing.
# Remove this block when integrating with the group's main.py file.
if __name__ == "__main__":
    request_book()
    view_request_log()
