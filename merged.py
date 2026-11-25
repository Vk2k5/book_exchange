import sys

students = {
    "S101": "Rahul",
    "S102": "Priya",
    "S103": "Anita",
    "S104": "Kiran",
    "S105": "Arjun",
    "S106": "Meera",
    "S107": "Rohan",
    "S108": "Sneha",
    "S109": "Vikram",
    "S110": "Neha"
}

listings = {
    "B01": {
        "book_name": "Introduction to Algorithms",
        "possessed_by": "S101",
        "status": "Available"
    },
    "B02": {
        "book_name": "Clean Code",
        "possessed_by": "S102",
        "status": "Requested"
    },
    "B03": {
        "book_name": "Python Programming",
        "possessed_by": "S103",
        "status": "Available"
    },
    "B04": {
        "book_name": "Database Management Systems",
        "possessed_by": "S104",
        "status": "Requested"
    },
    "B05": {
        "book_name": "Operating System Concepts",
        "possessed_by": "S105",
        "status": "Available"
    }
}

requests = {
    "R01": {
        "book_id": "B02",
        "requester_id": "S106",
        "handover_status": {
            "owner_confirmed": True,
            "requester_confirmed": False
        }
    },
    "R02": {
        "book_id": "B04",
        "requester_id": "S107",
        "handover_status": {
            "owner_confirmed": False,
            "requester_confirmed": False
        }
    },
    "R03": {
        "book_id": "B01",
        "requester_id": "S108",
        "handover_status": {
            "owner_confirmed": True,
            "requester_confirmed": True
        }
    },
    "R04": {
        "book_id": "B03",
        "requester_id": "S109",
        "handover_status": {
            "owner_confirmed": False,
            "requester_confirmed": True
        }
    },
    "R05": {
        "book_id": "B05",
        "requester_id": "S110",
        "handover_status": {
            "owner_confirmed": False,
            "requester_confirmed": False
        }
    }
}


def addBook():
    book_name = input("Enter Book Name: ")
    student_id = input("Enter Student ID: ")

    book_id = "B" + str(len(listings) + 1).zfill(2)

    listings[book_id] = {
        "book_name": book_name,
        "possessed_by": student_id,
        "status": "Available"
    }

    print("Book added successfully!")
    print("Book ID:", book_id)


def viewBooks():
    print("\n----- ALL BOOKS -----")

    for book_id in listings:
        print("--------------------")
        print("Book ID:", book_id)
        print("Book Name:", listings[book_id]["book_name"])
        print("Student ID:", listings[book_id]["possessed_by"])
        print("Status:", listings[book_id]["status"])


def requestBook():
    print("\n--- Request a Book ---")
    print("\n--- Available Books ---")

    for book_id in listings:
        if listings[book_id]["status"] == "Available":
            print("Book ID:", book_id)
            print("Book Name:", listings[book_id]["book_name"])
            print("Owner ID:", listings[book_id]["possessed_by"])

    student_id = input("\nEnter your Student ID: ").strip().upper()

    if student_id not in students:
        print("Invalid Student ID!")
        return

    book_id = input("Enter Book ID: ").strip().upper()

    if book_id not in listings:
        print("Book ID not found!")
        return

    if listings[book_id]["status"] != "Available":
        print("Book is not available!")
        return

    if listings[book_id]["possessed_by"] == student_id:
        print("You cannot request your own book!")
        return

    request_id = "R" + str(len(requests) + 1).zfill(2)

    requests[request_id] = {
        "book_id": book_id,
        "requester_id": student_id,
        "handover_status": {
            "owner_confirmed": False,
            "requester_confirmed": False
        }
    }

    listings[book_id]["status"] = "Requested"

    print("\nBook requested successfully!")
    print("Student:", students[student_id])
    print("Book:", listings[book_id]["book_name"])
    print("Request ID:", request_id)
    print("Status: Requested")


def viewRequests():
    print("\n----- REQUEST LOG -----")

    if len(requests) == 0:
        print("No requests have been made.")
        return

    for request_id in requests:
        book_id = requests[request_id]["book_id"]
        student_id = requests[request_id]["requester_id"]

        print("--------------------")
        print("Request ID:", request_id)
        print("Student:", students[student_id])
        print("Student ID:", student_id)
        print("Book:", listings[book_id]["book_name"])
        print("Book ID:", book_id)
        print("Owner ID:", listings[book_id]["possessed_by"])
        print("Owner Confirmed:",
              requests[request_id]["handover_status"]["owner_confirmed"])
        print("Requester Confirmed:",
              requests[request_id]["handover_status"]["requester_confirmed"])


def handoverConfirmation():
    print("\n===== CONFIRM HANDOVER =====")

    request_id = input("Enter Request ID: ").strip().upper()

    if request_id not in requests:
        print("Request not found!")
        return

    selected_request = requests[request_id]

    book_id = selected_request["book_id"]

    if book_id not in listings:
        print("Book not found!")
        return

    book = listings[book_id]

    if book["status"] != "Requested":
        print("Handover is allowed only for requested books.")
        return

    owner_id = book["possessed_by"]
    requester_id = selected_request["requester_id"]

    if owner_id not in students or requester_id not in students:
        print("Student record not found!")
        return

    print("\nBook:", book["book_name"])
    print("Owner:", students[owner_id])
    print("Requester:", students[requester_id])

    print("\n1. Book Owner")
    print("2. Book Requester")

    choice = input("Who is confirming the handover? ")

    match choice:
        case "1":
            if selected_request["handover_status"]["owner_confirmed"]:
                print("Owner has already confirmed!")
            else:
                selected_request["handover_status"]["owner_confirmed"] = True
                print("Owner confirmation successful!")

        case "2":
            if selected_request["handover_status"]["requester_confirmed"]:
                print("Requester has already confirmed!")
            else:
                selected_request["handover_status"]["requester_confirmed"] = True
                print("Requester confirmation successful!")

        case _:
            print("Invalid choice!")
            return

    if (selected_request["handover_status"]["owner_confirmed"]
            and selected_request["handover_status"]["requester_confirmed"]):

        book["status"] = "Closed"

        print("\nHandover completed successfully!")
        print("Book listing is now CLOSED.")

    else:
        print("\nWaiting for the other person's confirmation.")

    print("\nOwner confirmed:",
          selected_request["handover_status"]["owner_confirmed"])
    print("Requester confirmed:",
          selected_request["handover_status"]["requester_confirmed"])
    print("Book status:", book["status"])


choice = -1

while choice != 0:
    print("\n===== BOOK EXCHANGE SYSTEM =====")
    print("1. Add Book")
    print("2. Request a Book")
    print("3. View Existing Listings")
    print("4. View Existing Requests")
    print("5. Handover Confirmation")
    print("0. Exit")

    choice = input("Enter your choice: ")

    match choice:
        case "1":
            addBook()

        case "2":
            requestBook()

        case "3":
            viewBooks()

        case "4":
            viewRequests()

        case "5":
            handoverConfirmation()

        case "0":
            print("Thank you for using Book Exchange System!")
            sys.exit(0)

        case _:
            print("Invalid choice!")