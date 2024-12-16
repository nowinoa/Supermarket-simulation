# F1 - coded by Ainhoa Prada Tello - 001352985
class Lane():
    def __init__(self, id, type, status):
        self.id = id
        self.type = type
        self.status = status
        self.timestamp = "00:00"
        self.customers = []

    def capacity(self):
        """Get the capacity of a lane"""
        if self.type == 'reg':
            return 5
        else:
            return 15
        
    def set_timestamp(self, timestamp):
        """set timestamp with given time"""
        self.timestamp = timestamp

    def add_customer(self, customer):
        """add a customer to the lane"""
        self.customers.append(customer)

    def remove_customer(self, customer):
        """remove customer from lane and return the removed customer"""
        self.customers.remove(customer)
        print(f'{customer.id} has been removed in {customer.checkout_time(self.type)}')
        return customer

    def open_lane(self):
        """open lane - modify status"""
        self.status = 'opened'

    def close_lane(self):
        """close lane -modify status"""
        self.status = 'closed'

    def display_lanes(self):
        """Display lanes: L1 --> Status: Opened, Customers: * * * * (being this the number of customers on the lane)"""
        first_customer_id = self.customers[0].id if self.customers else None
        customer_symbols = ['*' for _ in self.customers]
        if self.type == 'slf':
            customers = self.customers[:8]
            customer_ids = [c.id for c in customers]
            print(
                f'L{self.id} --> Status: {self.status}, Customers: {", ".join(customer_symbols)},  First Customer ID: {customer_ids} ')
        else:
            print(
                f'L{self.id} --> Status: {self.status}, Customers: {", ".join(customer_symbols)}, First Customer ID: {first_customer_id}')
            







