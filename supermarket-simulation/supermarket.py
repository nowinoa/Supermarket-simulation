import random
import time
from datetime import datetime, timedelta
from customer import Customer
from lane import Lane

# F3 - coded by Ainhoa Prada Tello - 001352985
class Supermarket(Customer, Lane):

    def __init__(self, id):
        Customer.__init__(self, id, random.randint(1, 30))
        Lane.__init__(self, id, 'supermarket', 'opened')
        self.total_customers = []
        self.lanes = []
        self.seconds = 0
        self.minutes = 0
        self.timestamp = f'{self.minutes:02d}:{self.seconds:02d}'


    def get_total_customers(self):
        return self.total_customers

    def get_lanes(self):
        return self.lanes

    def get_sim_seconds(self):
        return self.seconds
    
    def get_sim_minutes(self):
        return self.minutes

    def set_timestamp(self, t):
        self.timestamp = t

    def remove_customer_from_total(self, customer):
        """If the customer exists remove it from the total"""
        try:
            self.total_customers.remove(customer)
        except ValueError:
            print(f"Customer {customer.identifier} not found in the list.")

    def setup_lanes(self):
        """Set up supermarket lanes"""
        L1 = Lane(1, 'reg', 'opened')
        L2 = Lane(2, 'reg', 'closed')
        L3 = Lane(3, 'reg', 'closed')
        L4 = Lane(4, 'reg', 'closed')
        L5 = Lane(5, 'slf', 'opened')

        self.lanes = [L1, L2, L3, L4, L5]

    def generate_random_customers(self):
        """Generate a random customer up to 10 with a unique id (Customer-1,100)"""
        num_customers = random.randint(1, 10)
        used_ids = set()

        for i in range(num_customers):
            # Generate a unique ID
            while True:
                customer_id = f'Customer_{random.randint(1, 100)}'
                if customer_id not in used_ids:
                    break

            # Create and add the customer to the list
            basket = random.randint(1, 30)
            customer = Customer(id=customer_id, basket=basket)
            checkout = customer.checkout_time('slf') if basket < 10 else customer.checkout_time('reg')
            customer.checkout = checkout
            used_ids.add(customer_id)
            self.total_customers.append(customer)

    def clear_all_lanes(self):
        for lane in self.lanes:
            lane.customers = []

    def assign_customers(self, customer):
        """If the customer has less than ten items and the self service is not saturated then add to the lane if not add to regular lane"""
        if customer.basket < 10:
            # Assign customers with less than 10 items to the self-service lane
            if len(self.lanes[4].customers) < self.lanes[4].capacity():
                self.lanes[4].add_customer(customer)
            else:
                # If self-service lane is saturated, assign to regular lanes
                self.assign_to_regular_lane(customer)
        else:
            # Assign customers with 10 or more items to regular lanes
            self.assign_to_regular_lane(customer)

    def assign_to_regular_lane(self, customer):
        """If the lane is saturated open the next lane"""
        regular_lanes = self.lanes[:4]
        all_lanes_saturated = all(len(lane.customers) >= lane.capacity() for lane in regular_lanes)

        if all_lanes_saturated:
            shortest_lane = min(regular_lanes, key=lambda lane: len(lane.customers))
            shortest_lane.add_customer(customer)
        else:
            for lane in regular_lanes:  # Only consider regular lanes
                if lane.status == 'opened' and len(lane.customers) < lane.capacity():
                    lane.add_customer(customer)
                    break
                elif lane.status == 'closed':
                    lane.open_lane()
                    lane.add_customer(customer)
                    break

    def customer_checkout(self):
        """remove customers from lanes when the checkout is completed and close lanes if empty"""
        opened_lanes = [lane for lane in self.lanes if lane.status == 'opened']
        for l in opened_lanes:
            if l.type == 'reg' and len(l.customers) > 0:
                first_customer = l.customers[0]
                checkout_time = first_customer.checkout
                if checkout_time < 30:
                    removed_customer = l.remove_customer(first_customer)
                    self.remove_customer_from_total(removed_customer)
                    if len(l.customers) == 0:
                        l.close_lane()
                else:
                    checkout_time -= 30
                    first_customer.checkout = checkout_time
            elif l.type == 'slf' and len(l.customers) > 0:
                for customer in l.customers[:8]:  # Process the first 8 customers
                    checkout_time = customer.checkout

                    if checkout_time < 30:
                        removed_customer = l.remove_customer(customer)
                        self.remove_customer_from_total(removed_customer)
                    else:
                        checkout_time -= 30
                        customer.checkout = checkout_time

    def display_info(self):
        print(f'### Total customers at {self.timestamp} : {len(self.total_customers)} ###')
        for c in self.total_customers:
            c.customer_info()
        for l in self.lanes:
            l.display_lanes()



def start_simulation():
    # initialice simulation
    supermarket = Supermarket(id='Market_1')
    supermarket.setup_lanes()
    sim_seconds = supermarket.get_sim_seconds()
    sim_minutes = supermarket.get_sim_minutes()
    customers = supermarket.get_total_customers()
    lanes = supermarket.get_lanes()
    
    # start counter
    while sim_minutes < 5:
        if len(customers) > 30:
            print('Max-capacity is full!!')
        elif len(customers) < 30:
            supermarket.generate_random_customers()

        supermarket.clear_all_lanes()

        for customer in customers:
            supermarket.assign_customers(customer)

        supermarket.display_info()

        sim_seconds += 30
        while sim_seconds >= 60:
            sim_seconds -= 60
            sim_minutes += 1
        timestamp = f'{sim_minutes:02d}:{sim_seconds:02d}'
        supermarket.set_timestamp(timestamp)
        supermarket.customer_checkout()

        time.sleep(30)
    supermarket.display_info()
    print("Simulation ended")


def start_simulation_prompt():
    while True:
        response = input("Would you like to start the simulation? (Yes/No): ").lower()
        if response == 'yes':
            return True
        elif response == 'no':
            return False
        else:
            print("Invalid response. Please enter 'Yes' or 'No'.")

if start_simulation_prompt():
    start_simulation()
else:
    print("Simulation canceled.")


