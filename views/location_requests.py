import sqlite3
import json
from models import Location

LOCATIONS = [
    {
        "id": 1,
        "name": "Nashville North",
        "address": "8422 Johnson Pike"
    },
    {
        "id": 2,
        "name": "Nashville South",
        "address": "209 Emory Drive"
    }
]


def create_location(location):
    """Disable error"""
    max_id = LOCATIONS[-1]["id"]
    new_id = max_id + 1
    location["id"] = new_id
    LOCATIONS.append(location)
    return location

def delete_location(id):
    """Disable error"""
    location_index = -1
    for index, location in enumerate(LOCATIONS):
        if location["id"] == id:
            location_index = index
    if location_index >= 0:
        LOCATIONS.pop(location_index)

def update_location(id, new_location):
    """Iterate the locations list, but use enumerate() so that"""
    for index, location in enumerate(LOCATIONS):
        if location["id"] == id:
            LOCATIONS[index] = new_location
            break

def get_single_location(id):
    """Disable error"""
    request_location = None
    for location in LOCATIONS:
        if location["id"] == id:
            request_location = location
    return request_location


def get_all_locations():
    """Open a connection to the database"""
    with sqlite3.connect("./kennel.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        db_cursor.execute("""
        SELECT
            a.id,
            a.name,
            a.address
        FROM location a
        """)

        locations = []
        dataset = db_cursor.fetchall()
        for row in dataset:
            location = Location(row['id'], row['name'], row['address'])
            locations.append(location.__dict__)
    return json.dumps(locations)
