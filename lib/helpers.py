from models import Venue
from seed import mysession

def list_venues():
    venues = mysession.query(Venue).all()
    for venue in venues:
        print(venue)

def delete_venue():
    venue_id = int(input("Enter the ID of the venue you want to delete: "))
    venue = mysession.query(Venue).filter_by(id=venue_id).first()
    if venue:
        venue_name = venue.name
        mysession.delete(venue)
        mysession.commit()
        print(f"Venue '{venue_name}' (ID: {venue_id}) deleted successfully.")
    else:
        print(f"Venue with ID {venue_id} not found.")

def find_venue_by_name(name):
    pass

def find_venue_by_id():
    pass
    

def create_venue():
    venue_name = input("Enter the venues name: ")
    venue_location = input("Enter the location: ")
    venue = Venue(name=venue_name, location = venue_location)
    mysession.add(venue)
    mysession.commit()
    print(f"New venue {venue_name} created successfully")

def update_venue():
    venue_id = int(input("Enter the ID of the venue you want to update: "))
    venue = find_venue_by_id()
    if venue:
        new_name = input("Enter the new name for the venue (leave blank to keep current): ").strip()
        new_location = input("Enter the new location for the venue (leave blank to keep current): ").strip()

        # Update the venue's attributes if new values are provided
        if new_name:
            venue.name = new_name
        if new_location:
            venue.location = new_location

        mysession.commit()
        print(f"Venue with ID {venue_id} updated successfully.")
    else:
        print(f"Venue with ID {venue_id} not found.")
    
    

def list_events():
    pass

def find_events_by_name(name):
    pass

def find_events_by_id(event_id):
    pass

def create_event():
    pass

def update_event():
    pass

def delete_event():
    pass

def list_event_attendees():
    pass

def exit_program():
    print("Goodbye!")
    exit()
