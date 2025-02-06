
class Room:
    def __init__(self, room_number, price):
        self.room_number = room_number
        self.price = price
        self.bookings = []

    def book(self, check_in, check_out):
        self.bookings.append((check_in, check_out))

    def is_available(self, check_in, check_out):
        for booking in self.bookings:
            if not (check_out <= booking[0] or check_in >= booking[1]):
                return False
        return True