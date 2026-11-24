import sys

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
    }
}

requests = {
    "R01": {
        "book_id": "B02",
        "requester_id": "S103",
        "handover_status": {
            "owner_confirmed": True,
            "requester_confirmed": False
        }
    }
}

def book_listing():
    pass

def request_book():
    pass

def handover_confirmation():
    pass

choice = int(input("Welcome to Book Exchange System choose an option to continue\n1. Book Listing\n2. Request a Book\n3. Handover Confirmation\n0. Exit\n"))

while choice != 0:
    match choice:
        case 1:
            book_listing()
        case 2:
            request_book()
        case 3:
            handover_confirmation()
        case _:
            print("Invalid option")
            
    choice = int(input("\nWelcome to Book Exchange System choose an option to continue\n1. Book Listing\n2. Request a Book\n3. Handover Confirmation\n0. Exit\n"))

sys.exit(0)