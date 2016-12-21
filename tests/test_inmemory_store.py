from sample.inmemory_room_store import save, get
from sample.model.Room import Room


def test_save():
    room = Room(1, [])
    save(1, room)
    assert get(1) == room
