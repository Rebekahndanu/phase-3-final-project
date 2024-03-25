from sqlalchemy.orm import declarative_base, relationship, sessionmaker
from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey, Table

Base = declarative_base()

event_attendee = Table(
    'event_attendees',
    Base.metadata,
    Column("event_id", Integer(), ForeignKey('events.id'), primary_key=True),
    Column("attendee_id", Integer(), ForeignKey('attendees.id'), primary_key=True),
    extend_existing=True
)

class Venue(Base):
    __tablename__ = 'venues'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    location = Column(String)


    events = relationship("Event", back_populates="venue")

    def __repr__(self):
        return f"Venue(id={self.id}, name='{self.name}', location='{self.location}')"

class Event(Base):
    __tablename__ = 'events'

    id = Column(Integer, primary_key=True)
    event_name = Column(String)
    description = Column(String)
    date = Column(DateTime)
    venue_id = Column(Integer, ForeignKey('venues.id'))

    venue = relationship("Venue", back_populates="events")
    attendees = relationship("Attendee", secondary=event_attendee, back_populates="events")

    def __repr__(self):
        return f"<Event(name='{self.event_name}', description='{self.description}', date='{self.date}', venue_id='{self.venue_id}')>"

class Attendee(Base):
    __tablename__ = 'attendees'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String, unique=True)
    ticket_number = Column(Integer)
    
    events = relationship("Event", secondary=event_attendee, back_populates="attendees")

    def __repr__(self):
        return f"<Attendee(name='{self.name}', email='{self.email}', ticket_number='{self.ticket_number}')>"


