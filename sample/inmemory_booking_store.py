bookings = {}


def save(room_id, user_id, slot):
    slot.start_date + slot.end_date + room_id
    bookings[room_id] = room


def delete(room_id):
    return bookings.pop(room_id)


def update(room_id, room):
    save(room_id, room)


def get(room_id):
    return bookings[room_id]