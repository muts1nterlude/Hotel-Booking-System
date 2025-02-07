from user import User
from hotel import Hotel
from room import Room

if __name__ == "__main__":
    user1 = User("Mutsawashe Mutasa", "mutsawavic@gmail.com", "password123")

    hotel1 = Hotel("Grand Hotel", "New York")

    room101 = Room(101, 150)
    room102 = Room(102, 200)
    hotel1.add_room(room101)
    hotel1.add_room(room102)

    if user1.login("mutsawavic@gmail.com", "password123"):
        print("Login successful!")
        
        check_in = "2025-10-01"
        check_out = "2025-10-03"
        available_rooms = hotel1.search_rooms(check_in, check_out)

        if available_rooms:
            print("Available rooms:")
            for room in available_rooms:
                print(f"Room Number: {room.room_number}, Price: ${room.price}")

            selected_room = available_rooms[0]
            selected_room.book(check_in, check_out)
            user1.add_booking(selected_room)

            print(f"Room {selected_room.room_number} booked from {check_in} to {check_out}.")
        else:
            print("No rooms available for the selected dates.")
    else:
        print("Login failed. Please check your credentials.")