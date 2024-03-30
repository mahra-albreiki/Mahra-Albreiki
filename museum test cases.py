from museum import *

# test cases

# Test case: Composition relationship
ticket1 = Ticket("Adult", 63)  # Create a ticket for an adult visitor
visitor1 = Visitor("Mahra", 18)  # Create a visitor named Mahra aged 18
visitor1.buy_ticket(ticket1)  # 'Mahra' buys the ticket
print(f"{visitor1.name} has bought a {visitor1.ticket.ticket_type} ticket for {visitor1.ticket.price} AED.")

# Test case: Aggregation relationship
location1 = Location("Permanent Gallery")  # Create a location object for a permanent gallery
exhibition1 = Exhibition("Impressionism Exhibition", "3 months", location1)  # Create an exhibition
artwork1 = Artwork("Starry Night", "Vincent van Gogh", "1889", "Iconic painting", location1)  # Create an artwork
exhibition1.add_artwork(artwork1)  # Add the artwork to the exhibition
print(f"{exhibition1.name} includes the artwork: {artwork1.title}")

# Test case: Inheritance relationship
museum1 = Museum("Louvre Museum", "Abu Dhabi")  # Create a museum object
print(f"{museum1.name} is located in {museum1.location}.")

# Additional test cases for different scenarios
# Adult ticket
adult_ticket = Ticket("Adult", 63)
print(f"Adult ticket price: {adult_ticket.price} AED")

# Child ticket (below 18)
child_ticket = Ticket("Child", 63, visitor_age=12)
print(f"Child ticket price: {child_ticket.price} AED")

# Senior ticket (above 60)
senior_ticket = Ticket("Senior", 63, visitor_age=70)
print(f"Senior ticket price: {senior_ticket.price} AED")

# Teacher ticket
teacher_ticket = Ticket("Teacher", 63, occupation="Teacher")
print(f"Teacher ticket price: {teacher_ticket.price} AED")

# Student ticket
student_ticket = Ticket("Student", 63, occupation="Student")
print(f"Student ticket price: {student_ticket.price} AED")

# Group ticket (50% discount)
group_ticket = Ticket("Group", 63)
print(f"Group ticket price: {group_ticket.price} AED")

# Special event ticket (individual price)
special_event_ticket = Ticket("Special Event", 100)
print(f"Special Event ticket price: {special_event_ticket.price} AED")

# Test case: Bidirectional association between Visitor and Exhibition
visitor1.visit_exhibition(exhibition1)  # Visitor Mahra visits the exhibition
print(f"{visitor1.name} visited the {exhibition1.name} exhibition.")
