import sqlite3
import json
from models import Customer

CUSTOMERS = [
    {
        "id": 1,
        "name": "Jeremiah",
    },
    {
        "id": 2,
        "name": "Michael",
    },
    {
        "id": 3,
        "name": "Mitch",
    },
    {
        "id": 4,
        "name": "Brett",
    }
]


def create_customer(customer):
    """Disable error"""
    max_id = CUSTOMERS[-1]["id"]
    new_id = max_id + 1
    customer["id"] = new_id
    CUSTOMERS.append(customer)
    return customer

def delete_customer(id):
    """Disable error"""
    customer_index = -1
    for index, customer in enumerate(CUSTOMERS):
        if customer["id"] == id:
            customer_index = index
    if customer_index >= 0:
        CUSTOMERS.pop(customer_index)


def update_customer(id, new_customer):
    """Iterate the customers list, but use enumerate() so that"""
    for index, customer in enumerate(CUSTOMERS):
        if customer["id"] == id:
            CUSTOMERS[index] = new_customer
            break

def get_single_customer(id):
    """Disable error"""
    request_customer = None
    for customer in CUSTOMERS:
        if customer["id"] == id:
            request_customer = customer
    return request_customer


def get_all_customers():
    """Open a connection to the database"""
    with sqlite3.connect("./kennel.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        db_cursor.execute("""
        SELECT
            a.id,
            a.name,
            a.address,
            a.email,
            a.password
        FROM customer a
        """)

        customers = []
        dataset = db_cursor.fetchall()
        for row in dataset:
            customer = Customer(row['id'], row['name'],
                                row['address'], row['email'], row['password'])
            customers.append(customer.__dict__)
    return json.dumps(customers)
