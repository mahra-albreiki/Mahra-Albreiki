# Creating artwork class
class Artwork:
    def __init__(self, title, artist, creation_date, historical_impact, location):
        self.title = title  # Title of the artwork
        self.artist = artist  # Artist of the artwork
        self.creation_date = creation_date  # Date of creation of the artwork
        self.historical_impact = historical_impact  # Historical impact or value of the artwork
        self.location = location  # Location of the artwork

# Creating location class
class Location:
    def __init__(self, location_type):
        self.location_type = location_type  # Type of location (e.g., Permanent Gallery, Exhibition Hall, Outdoor Space)

# Creating visitor class
class Visitor:
    def __init__(self, name, age):
        self.name = name  # Name of the visitor
        self.age = age  # Age of the visitor
        self.ticket = None  # Composition relationship: Visitor has a Ticket
        self.visited_exhibitions = []  # List to store visited exhibitions

    def buy_ticket(self, ticket):
        self.ticket = ticket  # Assign the purchased ticket to the visitor

    def visit_exhibition(self, exhibition):
        self.visited_exhibitions.append(exhibition)  # Add exhibition to the list of visited exhibitions

# Creating ticket class
class Ticket:
    def __init__(self, ticket_type, base_price, visitor_age=None, occupation=None, event_type=None):
        self.ticket_type = ticket_type  # Type of ticket (e.g., Adult, Child)
        self.price = self.calculate_price(base_price, visitor_age, occupation, event_type)  # Price of the ticket

    def calculate_price(self, base_price, visitor_age, occupation, event_type):
        if event_type == "Special Event":  # Special Events have individual ticket prices
            return base_price
        elif visitor_age is not None and visitor_age < 18:  # Children below 18 get a free ticket
            return 0
        elif visitor_age is not None and visitor_age >= 60:  # Seniors above 60 get a free ticket
            return 0
        elif occupation in ["Teacher", "Student"]:  # Teachers and students get a free ticket
            return 0
        elif self.ticket_type == "Group":  # Groups receive a 50% discount
            return base_price / 2
        else:
            return base_price  # All other visitors pay the base price

# Creating exhibition class
class Exhibition:
    def __init__(self, name, time, location):
        self.name = name  # Name of the exhibition
        self.time = time  # Time of the exhibition
        self.location = location  # Location of the exhibition
        self.artworks = []  # Aggregation relationship: Exhibition has artworks

    def add_artwork(self, artwork):
        self.artworks.append(artwork)  # Add artwork to the exhibition

# Creating event class
class Event:
    def __init__(self, name, time, location, ticket_price):
        self.name = name  # Name of the event
        self.time = time  # Duration of the event
        self.location = location  # Location of the event
        self.ticket_price = ticket_price  # Price of tickets for the event

# Creating museum class (Inheritance)
class Museum(Exhibition, Event):
    def __init__(self, name, location):
        super().__init__(name, None, location)  # Call superclass constructors
        self.location = location  # Location of the museum
        self.exhibitions = []  # Aggregation relationship: Museum has exhibitions
        self.events = []  # Aggregation relationship: Museum has events

    def host_exhibition(self, exhibition):
        self.exhibitions.append(exhibition)  # Add exhibition to the museum

    def host_event(self, event):
        self.events.append(event)  # Add event to the museum
