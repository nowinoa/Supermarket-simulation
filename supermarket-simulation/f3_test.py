# Test for Supermarket - coded by Ainhoa Prada Tello - 001352985
import unittest
from supermarket import Supermarket 
import time

class TestSupermarket(unittest.TestCase):

    def test_generate_random_customers(self):
        # Checks the methods generate random customers which creates up to 30 customers 
        # and checks if the total customers is greater than 0
        supermarket = Supermarket(id='Market_1')
        supermarket.generate_random_customers()
        self.assertGreater(len(supermarket.total_customers), 0)

    def test_assign_customers(self):
        # checks if the customers are being assigned to the lanes by checking the lane.customer length property of every lane
        supermarket = Supermarket(id='Market_1')
        supermarket.generate_random_customers()
        customer = supermarket.total_customers[0] 
        supermarket.setup_lanes()
        supermarket.assign_customers(customer)
        self.assertTrue(any(len(lane.customers) > 0 for lane in supermarket.lanes))


    def test_customer_checkout(self):
        # Checks that the customer is beign checked out from the lane when the checkout is completed
        supermarket = Supermarket(id='Market_1')
        supermarket.generate_random_customers()
        customer = supermarket.total_customers[0]
        supermarket.setup_lanes()
        supermarket.assign_customers(customer)

        # Simulate time passing
        for _ in range(4):  # Simulate 2 minutes (4 iterations with sleep of 30 seconds)
            time.sleep(30)
            supermarket.customer_checkout()

        # Check that all lanes are empty
        self.assertFalse(any(len(lane.customers) > 0 for lane in supermarket.lanes))

if __name__ == '__main__':
    unittest.main()
