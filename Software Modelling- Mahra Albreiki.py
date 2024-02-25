class Passenger:
    def __init__(self, name, passport, email):
        # Initialize Passenger attributes
        self.name = name
        self.passport = passport
        self.email = email

    def set_name(self, name):
        # Setter method for name attribute
        self.name = name

    def get_name(self):
        # Getter method for name attribute
        return self.name

    # Similarly, implementing setter and getter methods for passport and email


class Flight:
    def __init__(self, flight_num, departure, arrival, departure_time, arrival_time, gate):
        # Initialize Flight attributes
        self.flight_num = flight_num
        self.departure = departure
        self.arrival = arrival
        self.departure_time = departure_time
        self.arrival_time = arrival_time
        self.gate = gate

    def set_flight_num(self, flight_num):
        # Setter method for flight_num attribute
        self.flight_num = flight_num

    def get_flight_num(self):
        # Getter method for flight_num attribute
        return self.flight_num

    # Similarly, implementing it to setter and getter methods for departure, arrival, departure_time, and arrival_time


class BoardingPass:
    def __init__(self, passenger, flight, seat):
        # Initialize BoardingPass attributes
        self.passenger = passenger
        self.flight = flight
        self.seat = seat

    def set_passenger(self, passenger):
         # Setter method for passenger attribute
        self.passenger = passenger

    def get_passenger(self):
        # Getter method for passenger attribute
        return self.passenger

    # Similarly, implement setter and getter methods for flight and seat

    # Function to generate and return boarding pass details
    def generate_boarding_pass_details(self):
        # Placeholder function to generate boarding pass details
        pass


class Seat:
    def __init__(self, seat_number, seat_class, is_reserved):
        # Initialize Seat attributes
        self.seat_number = seat_number
        self.seat_class = seat_class
        self.is_reserved = is_reserved

    def set_seat_number(self, seat_number):
        # Setter method for seat_number attribute
        self.seat_number = seat_number

    def get_seat_number(self):
        # Getter method for seat_number attribute
        return self.seat_number

    # Similarly, implement setter and getter methods for seat_class and is_reserved

    # Function to reserve a seat
    def reserve_seat(self):
        # Placeholder function to reserve a seat
        pass

    # Function to cancel seat reservation
    def cancel_reservation(self):
        # Placeholder function to cancel seat reservation
        pass


# Creating Passenger object
passenger1 = Passenger("JAMES SMITH", "AB123456", "JAMES.SMITH@example.com")

# Creating Flight object
flight1 = Flight("NA4321", "CHICAGO ORD", "NEW YORK JFK", "06-DEC-20 11:40", "13:30", "Gate 03")

# Creating Seat object
seat1 = Seat("09A", "First", False)

# Creating BoardingPass object
boarding_pass1 = BoardingPass(passenger1, flight1, seat1)

# Displaying Boarding Pass Details
print("Passenger Name:", boarding_pass1.get_passenger().get_name())
print("Flight Number:", boarding_pass1.flight.get_flight_num())
print("Departure Destination:", boarding_pass1.flight.departure)
print("Arrival Destination:", boarding_pass1.flight.arrival)
print("Departure Time:", boarding_pass1.flight.departure_time)
print("Arrival Time:", boarding_pass1.flight.arrival_time)
print("Gate Number:", boarding_pass1.flight.gate)
print("Seat Number:", boarding_pass1.seat.get_seat_number())