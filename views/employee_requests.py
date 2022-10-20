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
    max_id = EMPLOYEES[-1]["id"]
    new_id = max_id + 1
    employee["id"] = new_id
    EMPLOYEES.append(employee)
    return employee

def delete_employee(id):
    employees_index = -1
    for index, employees in enumerate(EMPLOYEES):
        if employees["id"] == id:
            employees_index = index
    if employees_index >= 0:
        EMPLOYEES.pop(employees_index)

def get_all_employees():
    return EMPLOYEES


def get_single_employee(id):
    request_employee = None
    for employee in EMPLOYEES:
        if employee["id"] == id:
            request_employee = employee
    return request_employee
