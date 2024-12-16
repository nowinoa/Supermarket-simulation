# Test for Lane - coded by Ainhoa Prada Tello - 001352985
import unittest
from supermarket import Lane, Customer

class TestLaneMethods(unittest.TestCase):

    def setUp(self):
        self.customer1 = Customer(1, 5)
        self.customer2 = Customer(2, 10)
        self.lane1 = Lane(1, 'reg', 'closed')
        self.lane2 = Lane(2, 'slf', 'opened')

    def test_capacity(self):
        # check if the capacity method returns the correct amount
        self.assertEqual(self.lane1.capacity(), 5)
        self.assertEqual(self.lane2.capacity(), 15)

    def test_add_customer(self):
        # check if the add_customer method adds customers to the lanes properly
        self.lane1.add_customer(self.customer1)
        self.assertEqual(len(self.lane1.customers), 1)
        self.assertEqual(self.lane1.customers[0], self.customer1)

    def test_remove_customer(self):
        # check if the remove_customer method deletes customers on the lanes properly
        self.lane2.add_customer(self.customer2)
        removed_customer = self.lane2.remove_customer(self.customer2)
        self.assertEqual(len(self.lane2.customers), 0)
        self.assertEqual(removed_customer.id, 2)

    def test_open_lane(self):
        # When the method is applied the status of the lane changes to opened
        self.lane1.open_lane()
        self.assertEqual(self.lane1.status, 'opened')

    def test_close_lane(self):
        # When the method is applied the status of the lane changes to closed
        self.lane2.close_lane()
        self.assertEqual(self.lane2.status, 'closed')
 

if __name__ == '__main__':
    unittest.main()
