from abc import abstractmethod

class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password
        self.bookings = []

    def login(self, email, password):
        return self.email == email and self.password == password

    def add_booking(self, room):
        self.bookings.append(room)