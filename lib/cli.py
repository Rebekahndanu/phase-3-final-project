from helpers import (
    exit_program,
    list_venues,
    create_venue,
    delete_venue,
    list_events,
    find_events_by_name,
    find_events_by_id,
    update_event,
    list_attendees,
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
            create_venue()
            input("Press enter to continue")
        elif choice == "3":
            delete_venue()
            input("Press enter to continue")
        elif choice == "4":
            list_events()
            input("Press enter to continue")
        elif choice == "5":
            name = input("Enter event name: ")
            find_events_by_name(name)
            input("Press enter to continue")
        elif choice == "6":
            event_id = input("Enter event ID: ")
            find_events_by_id(event_id)
            input("Press enter to continue")
        elif choice == "7":
            update_event()
            input("Press enter to continue")
        elif choice == "8":
            list_attendees()
            input("Press enter to continue")
        else:
            print("Invalid choice")


def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. List venues")
    print("2. Create a new venue")
    print("3. Delete a venue")
    print("4. List events")
    print("5. Find events by name")
    print("6. Find events by ID")
    print("7. Update events")
    print("8. List event attendees")


if __name__ == "__main__":
    main()
