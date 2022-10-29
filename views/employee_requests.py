import sqlite3
import json
from models import Employees, Location

EMPLOYEES = [
    {
        "id": 1,
        "name": "Shay",
    },
    {
        "id": 2,
        "name": "Krima",
    }
  ,
    {
        "id": 3,
        "name": "Nishaya",
    },
    {
        "id": 42,
        "name": "Jessica",
    }
]

def create_employee(employee):
    """Disable error"""
    max_id = EMPLOYEES[-1]["id"]
    new_id = max_id + 1
    employee["id"] = new_id
    EMPLOYEES.append(employee)
    return employee

def delete_employee(id):
    """delete"""
    with sqlite3.connect("./kennel.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        DELETE FROM employee
        WHERE id = ?
        """, (id, ))

def update_employee(id, new_employee):
    """update"""
    with sqlite3.connect("./kennel.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        UPDATE Employee
            SET
                name = ?,
                address = ?,
                location_id = ?,
        WHERE id = ?
        """, (new_employee['name'], new_employee['address'],
              new_employee['location_id'], id, ))
        rows_affected = db_cursor.rowcount

    if rows_affected == 0:
        return False
    else:
        return True

def get_single_employee(id):
    """ignore error"""
    with sqlite3.connect("./kennel.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        db_cursor.execute("""
        SELECT
            a.id,
            a.name,
            a.address,
            a.location_id
        FROM employee a
        WHERE a.id = ?
        """, (id, ))
        data = db_cursor.fetchone()
        employee = Employees(data['id'], data['name'],
                             data['address'], data['location_id'])
        return json.dumps(employee.__dict__)


def get_all_employees():
    """Open a connection to the database"""
    with sqlite3.connect("./kennel.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        db_cursor.execute("""
            SELECT
                a.id,
                a.name,
                a.address,
                a.location_id,
                l.name location_name,
                l.address location_address
            FROM Employee a
            JOIN Location l
                ON l.id = a.location_id
            """)

        employees = []
        dataset = db_cursor.fetchall()
    for row in dataset:

        employee = Employees(row['id'], row['name'], row['address'], row['location_id'])

        location = Location(row['id'], row['location_name'],
                            row['location_address'])

        employee.location = location.__dict__
        employees.append(employee.__dict__)
    return json.dumps(employees)

def get_employees_by_location(location_id):
    """Ignore error"""
    with sqlite3.connect("./kennel.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        SELECT
            a.id,
            a.name,
            a.address,
            a.location_id
        FROM employee a
        WHERE a.location_id = ?
        """, (location_id, ))

        employees = []
        dataset = db_cursor.fetchall()

        for row in dataset:
            employee = Employees(row['id'], row['name'],
                                  row['address'], row['location_id'])
            employees.append(employee.__dict__)

    return json.dumps(employees)
