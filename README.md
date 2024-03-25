# EVENT MANAGEMENT SYSTEM
## Introduction
My project is about an event management sytem displaying relationships between the venues, events and the attendees.

## Tree
.
├── lib
│   ├── alembic.ini
│   ├── cli.py
│   ├── events.db
│   ├── helpers.py
│   ├── migrations
│   │   ├── env.py
│   │   ├── README
│   │   ├── script.py.mako
│   │   └── versions
│   │       └── 09dd296c9b65_created_all_my_tables_and_their_.py
│   ├── models.py
│   ├── __pycache__
│   │   ├── helpers.cpython-38.pyc
│   │   └── models.cpython-38.pyc
│   └── seed.py
├── Pipfile
├── Pipfile.lock
└── README.md

## models.py
- My models.py file contains my all my classes together with my tables.
- I have three classes, ie, Event, Attendee, Venue
- I have four tables, ie, events, attendees, venues and an association class between events and tables called events_attendees

## seed.py
- This file contains all the code i used to be able to generate data ro populate my tables through faker

## cli.py
- cli.py is the command-line interface script for interacting with the event management system.
- It allows users to perform various operations such as listing venues, creating new venues, updating existing venues, deleting venues, listing events, finding events by name or ID, updating events, creating new events, listing event attendees, and exiting the program.
- The script utilizes functions from helpers.py to execute these operations.

## helpers.py
- It contains helper functions used in the event management system.
- It includes functions for listing venues, creating, updating, and deleting venues, listing events, finding events by name or ID, updating events, and listing event attendees.

## events.db
- It is the SQLite database file used to store data for the event management system.
- It contains tables for venues, events, attendees, and an association table for events and attendees.

## Technologies used
1. Programming languages - Python
2. libraries ad frameworks - SQLAlchemy and Faker
3. Database - sqlite
4. Dependancy management - Pipenv

## Features
- Users can create new venues by providing the venue name and location.
- Display a list of all venues stored in the database.
- Allow users to update the details of existing venues, such as name and location.
- Users can delete venues, removing them from the system.
- Users can create new events by specifying the event name, description, date, and associated venue.
- Display a list of all events stored in the database, including details such as name, description, date, and venue.
- Users can search for events by their name, retrieving relevant matches.
- Allow users to search for events by their unique identifier (ID).
- Users can update the details of existing events, such as name, description, date, and venue.



