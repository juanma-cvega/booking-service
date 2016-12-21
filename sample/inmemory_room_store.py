rooms = {}


def save(room_id, room):
    rooms[room_id] = room


def delete(room_id):
    return rooms.pop(room_id)


def update(room_id, room):
    save(room_id, room)


def get(room_id):
    return rooms[room_id]