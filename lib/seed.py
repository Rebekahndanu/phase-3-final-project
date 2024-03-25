from models import create_engine, Base, sessionmaker, Venue, Event, Attendee
from faker import Faker
from datetime import datetime, timedelta

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

    # Generating fake data for the Venue table
    for i in range(10): 
        venue = Venue(name=fake.company(), location=fake.address())
        mysession.add(venue)
    mysession.commit()


    # Define some helper functions for generating random dates and times
    def random_date(start_date, end_date):
        time_between_dates = end_date - start_date
        days_between_dates = time_between_dates.days
        random_number_of_days = fake.random_int(min=0, max=days_between_dates)
        return start_date + timedelta(days=random_number_of_days)

    def random_time():
        return fake.time()

    # Generating fake data for the Event table
    for i in range(20):  # You can adjust this number to generate more or fewer events
        start_date = datetime.now()
        end_date = start_date + timedelta(days=30)  # Events within the next 30 days
        event = Event(event_name=fake.word().capitalize(), 
                    description=fake.sentence(),
                    date=random_date(start_date, end_date),
                    venue_id=fake.random_int(min=1, max=10))  # Assuming 10 venues exist
        mysession.add(event)

    mysession.commit()

    # Generating fake data for the Attendee table
    for i in range(30):  # You can adjust this number to generate more or fewer attendees
        attendee = Attendee(name=fake.name(), email=fake.email(), ticket_number=fake.random_int(min=1000, max=9999))
        mysession.add(attendee)

    mysession.commit()