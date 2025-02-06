from room import Room

class Hotel:
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.rooms = []

    def add_room(self, room):
        self.rooms.append(room)

    def search_rooms(self, check_in, check_out):
        available_rooms = []
        for room in self.rooms:
            if room.is_available(check_in, check_out):
                available_rooms.append(room)
        return available_rooms