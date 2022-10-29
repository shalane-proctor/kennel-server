class Animal():
    """_summary_
    """

    def __init__(self, id, name, breed, customer_id, status, location_id):
        self.id = id
        self.name = name
        self.breed = breed
        self.customer_id = customer_id
        self.status = status
        self.location_id = location_id
        self.location = None
        self.customer = None
