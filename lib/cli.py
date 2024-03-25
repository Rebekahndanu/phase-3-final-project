from helpers import (
    exit_program,
    list_venues,
    find_venue_by_name,
    find_venue_by_id,
    create_venue,
    update_venue,
    delete_venue,
    list_events,
    find_events_by_name,
    find_events_by_id,
    create_event,
    update_event,
    delete_event,
    list_event_attendees
)

def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            list_venues()
            input("Press enter to continue")
        elif choice == "2":
            name = input("Enter venue name: ")
            find_venue_by_name(name)
        elif choice == "3":
            venue_id = input("Enter venue ID: ")
            find_venue_by_id()
        elif choice == "4":
            create_venue()
        elif choice == "5":
            update_venue()
        elif choice == "6":
            delete_venue()
        elif choice == "7":
            list_events()
        elif choice == "8":
            name = input("Enter event name: ")
            find_events_by_name(name)
        elif choice == "9":
            event_id = input("Enter event ID: ")
            find_events_by_id(event_id)
        elif choice == "10":
            create_event()
        elif choice == "11":
            update_event()
        elif choice == "12":
            delete_event()
        elif choice == "13":
            list_event_attendees()
        else:
            print("Invalid choice")


def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. List venues")
    print("2. Find venues by name")
    print("3. Find venues by ID")
    print("4. Create a new venue")
    print("5. Update a venue")
    print("6. Delete a venue")
    print("7. List events")
    print("8. Find events by name")
    print("9. Find events by ID")
    print("10. Create a new event")
    print("11. Update an event")
    print("12. Delete an event")
    print("13. List event attendees")


if __name__ == "__main__":
    main()
