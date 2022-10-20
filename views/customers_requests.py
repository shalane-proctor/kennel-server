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
    max_id = CUSTOMERS[-1]["id"]
    new_id = max_id + 1
    customer["id"] = new_id
    CUSTOMERS.append(customer)
    return customer

def delete_customer(id):
    customer_index = -1
    for index, customer in enumerate(CUSTOMERS):
        if customer["id"] == id:
            customer_index = index
    if customer_index >= 0:
        CUSTOMERS.pop(customer_index)

def get_all_customers():
    return CUSTOMERS

def get_single_customer(id):
    request_customer = None
    for customer in CUSTOMERS:
        if customer["id"] == id:
            request_customer = customer
    return request_customer
