
# Department Book Exchange
# Phase 1 - Confirm Handover

# Sample students
students = [
    {"student_id": 1, "name": "Rahul"},
    {"student_id": 2, "name": "Amit"}
]

# Sample books
books = [
    {
        "book_id": 101,
        "title": "Python Programming",
        "owner": 1,
        "status": "Requested"
    }
]

# Sample requests
requests = [
    {
        "request_id": 1,
        "book_id": 101,
        "requester": 2,
        "status": "Accepted",
        "owner_confirmed": False,
        "requester_confirmed": False
    }
]


def confirm_handover(books, requests, students):

    print("\n===== CONFIRM HANDOVER =====")

    request_id = int(input("Enter Request ID: "))

    # Find request
    selected_request = None

    for request in requests:
        if request["request_id"] == request_id:
            selected_request = request
            break

    if selected_request is None:
        print("Request not found!")
        return

    if selected_request["status"] != "Accepted":
        print("Handover is allowed only for accepted requests.")
        return

    # Find book
    book = None

    for b in books:
        if b["book_id"] == selected_request["book_id"]:
            book = b
            break

    if book is None:
        print("Book not found!")
        return

    # Find students
    owner = None
    requester = None

    for student in students:
        if student["student_id"] == book["owner"]:
            owner = student

        if student["student_id"] == selected_request["requester"]:
            requester = student

    if owner is None or requester is None:
        print("Student record not found!")
        return

    print("\nBook:", book["title"])
    print("Owner:", owner["name"])
    print("Requester:", requester["name"])

    print("\n1. Book Owner")
    print("2. Book Requester")

    choice = input("Who is confirming the handover? ")

    if choice == "1":

        if selected_request["owner_confirmed"]:
            print("Owner has already confirmed!")

        else:
            selected_request["owner_confirmed"] = True
            print("Owner confirmation successful!")

    elif choice == "2":

        if selected_request["requester_confirmed"]:
            print("Requester has already confirmed!")

        else:
            selected_request["requester_confirmed"] = True
            print("Requester confirmation successful!")

    else:
        print("Invalid choice!")
        return

    # Check both confirmations
    if (selected_request["owner_confirmed"]
            and selected_request["requester_confirmed"]):

        book["status"] = "Closed"
        selected_request["status"] = "Completed"

        print("\nHandover completed successfully!")
        print("Book listing is now CLOSED.")

    else:
        print("\nWaiting for the other person's confirmation.")

    print("\nOwner confirmed:", selected_request["owner_confirmed"])
    print("Requester confirmed:", selected_request["requester_confirmed"])
    print("Book status:", book["status"])


# Main program
while True:

    print("\n===== DEPARTMENT BOOK EXCHANGE =====")
    print("1. Confirm Handover")
    print("2. View Handover Status")
    print("3. Exit")

    option = input("Enter your choice: ")

    if option == "1":
        confirm_handover(books, requests, students)

    elif option == "2":

        for request in requests:
            print("\nRequest ID:", request["request_id"])
            print("Owner Confirmed:", request["owner_confirmed"])
            print("Requester Confirmed:", request["requester_confirmed"])
            print("Request Status:", request["status"])

    elif option == "3":
        print("Thank you for using Department Book Exchange!")
        break

    else:
        print("Invalid choice! Please try again.")
