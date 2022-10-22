import sqlite3
import json
from models import Employees

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
    """Disable error"""
    employees_index = -1
    for index, employees in enumerate(EMPLOYEES):
        if employees["id"] == id:
            employees_index = index
    if employees_index >= 0:
        EMPLOYEES.pop(employees_index)

def update_employee(id, new_employee):
    """Iterate the employees list, but use enumerate() so that"""
    for index, employee in enumerate(EMPLOYEES):
        if employee["id"] == id:
            EMPLOYEES[index] = new_employee
            break

def get_single_employee(id):
    """Disable error"""
    request_employee = None
    for employee in EMPLOYEES:
        if employee["id"] == id:
            request_employee = employee
    return request_employee


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
            a.location_id
        FROM employee a
        """)

        employees = []
        dataset = db_cursor.fetchall()
        for row in dataset:
            employee = Employees(row['id'], row['name'],
                                row['address'], row['location_id'])
            employees.append(employee.__dict__)
    return json.dumps(employees)
