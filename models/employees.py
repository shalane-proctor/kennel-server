from pickle import NONE


class Employees():
    """_summary_
    """
    def __init__(self, id, name, address, location_id):
        self.id = id
        self.name = name
        self.address = address
        self.location_id = location_id
        self.location = NONE
