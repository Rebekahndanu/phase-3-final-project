from models import Venue, Event, Attendee
from seed import mysession
from datetime import datetime

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
    
def create_venue():
    venue_name = input("Enter the venues name: ")
    venue_location = input("Enter the location: ")
    venue = Venue(name=venue_name, location = venue_location)
    mysession.add(venue)
    mysession.commit()
    print(f"New venue {venue_name} created successfully")
    

def list_events():
    events = mysession.query(Event).all()
    for event in events:
        print(event)

def find_events_by_name(name):
    events = mysession.query(Event).filter(Event.event_name == name).all()
    if events:
        for event in events:
            print(event)
    else:
        print(f"No events found with the name '{name}'.")

def find_events_by_id(event_id):
    event = mysession.query(Event).filter(Event.id == event_id).first()
    if event:
        print(event)
    else:
        print(f"No event found with ID '{event_id}'.")

def update_event():
    event_id = int(input("Enter the ID of the event you want to update: "))
    event = mysession.query(Event).filter_by(id=event_id).first()
    
    if event:
        event_name = input(f"Enter the new name for the event (current name: {event.event_name}): ")
        event_description = input(f"Enter the new description for the event (current description: {event.description}): ")
        event_date = input(f"Enter the new date for the event (current date: {event.date}): ")
        venue_id = int(input(f"Enter the new venue ID for the event (current venue ID: {event.venue_id}): "))
        
        try:
            event_date = datetime.strptime(event_date, "%Y-%m-%d %H:%M:%S")
        except ValueError:
            print("Invalid date format. Please enter the date in YYYY-MM-DD HH:MM:SS format.")
            return
        
        event.event_name = event_name
        event.description = event_description
        event.date = event_date
        event.venue_id = venue_id
        
        mysession.commit()
        print(f"Event '{event_name}' (ID: {event_id}) updated successfully.")
    else:
        print(f"Event with ID {event_id} not found.")


def list_attendees():
    attendees = mysession.query(Attendee).all()
    for attendee in attendees:
        print(attendee)

def exit_program():
    print("Goodbye!")
    exit()
