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
    """delete"""
    with sqlite3.connect("./kennel.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        DELETE FROM location
        WHERE id = ?
        """, (id, ))

def update_location(id, new_location):
    """update"""
    with sqlite3.connect("./kennel.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        UPDATE Location
            SET
                address = ?,
                name = ?
        WHERE id = ?
        """, (new_location['name'], new_location['address'], id, ))
        rows_affected = db_cursor.rowcount

    if rows_affected == 0:
        return False
    else:
        return True

def get_single_location(id):
    """ignore error"""
    with sqlite3.connect("./kennel.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        db_cursor.execute("""
        SELECT
            a.id,
            a.name,
            a.address
        FROM location a
        WHERE a.id = ?
        """, (id, ))
        data = db_cursor.fetchone()
        location = Location(data['id'], data['name'], data['address'])
        return json.dumps(location.__dict__)


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
