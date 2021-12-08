class Customer:
    id = 1
    def __init__(self, name, address, email):
        self.name = name
        self.address = address
        self.email = email
        self.id = Customer.get_next_id()

    # def get_next_id(self):
    #     return self.customer_id
    @staticmethod
    def get_next_id():
        res = Customer.id
        Customer.id += 1
        return res

    def __repr__(self):
        return f"Customer <{self.id}> {self.name}; " \
               f"Address: {self.address}; Email: {self.email}"

