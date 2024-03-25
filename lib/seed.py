from models import create_engine, Base, sessionmaker, Venue, Event, Attendee
from faker import Faker
from datetime import datetime, timedelta
from random import sample

engine = create_engine('sqlite:///events.db')
Base.metadata.create_all(engine)

sessioncreator = sessionmaker(bind=engine)
mysession = sessioncreator()

fake = Faker()

if __name__ == '__main__':

    mysession.query(Venue).delete()
    mysession.query(Event).delete()
    mysession.query(Attendee).delete()
    mysession.commit()

    # Generating data for the Venue table
    for i in range(10): 
        venue = Venue(name=fake.company(), location=fake.address())
        mysession.add(venue)
    mysession.commit()


    # Define functions for generating random dates and times
    def random_date(start_date, end_date):
        time_between_dates = end_date - start_date
        days_between_dates = time_between_dates.days
        random_number_of_days = fake.random_int(min=0, max=days_between_dates)
        return start_date + timedelta(days=random_number_of_days)

    def random_time():
        return fake.time()

    # Generating data for the Event table
    for i in range(20): 
        start_date = datetime.now()
        end_date = start_date + timedelta(days=30)  
        event = Event(event_name=fake.word().capitalize(), 
                    description=fake.sentence(),
                    date=random_date(start_date, end_date),
                    venue_id=fake.random_int(min=1, max=10))  
        mysession.add(event)

    mysession.commit()

    # Generating data for the Attendee table
    for i in range(30): 
        attendee = Attendee(name=fake.name(), email=fake.email(), ticket_number=fake.random_int(min=1000, max=9999))
        mysession.add(attendee)

    mysession.commit()

    # Associate attendees with events (generate data for event_attendees table)
    events = mysession.query(Event).all()
    attendees = mysession.query(Attendee).all()
    for event in events:
        # Assuming each event has between 1 to 10 attendees
        num_attendees = fake.random_int(min=1, max=10)  
        selected_attendees = sample(attendees, num_attendees)
        event.attendees.extend(selected_attendees)

    mysession.commit()