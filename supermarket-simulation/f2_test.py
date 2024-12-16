import unittest
import random

class CustomerDetails:
    def __init__(self):
        self.customer_id = f"CD{random.randint(1, 100)}"
        self.no_of_items = random.randint(1, 30)

    def get_no_of_items_in_basket(self):
        return self.no_of_items

    def lottery_ticket_award(self):
        return self.no_of_items >= 10

    def display_lottery_ticket(self):
        return "wins a lottery ticket" if self.lottery_ticket_award() else "hard luck, no lottery ticket this time!"

    def display_customer_details(self, checkout_lane_time):
        time_regular = checkout_lane_time.calculate_checkout_time('regular')
        time_self_service = checkout_lane_time.calculate_checkout_time('self-service')
        lottery_status = self.display_lottery_ticket()

        heading = "Lucky Customer" if self.lottery_ticket_award() else "Customer Details"

        return f"### {heading} ###\n{self.customer_id} -> items in the basket: {self.no_of_items}, {lottery_status}\ntime to process at regular till: {time_regular} Secs\ntime to process at self-service till: {time_self_service} Secs"

class CheckoutLaneTime:
    def __init__(self, customer):
        self.customer = customer

    def calculate_checkout_time(self, lane_type):
        regular_service_till = 4
        self_service_till = 6

        if lane_type == 'regular':
            return self.calculate_time(regular_service_till)
        elif lane_type == 'self-service':
            return self.calculate_time(self_service_till)
        return "Invalid checkout lane type"

    def calculate_time(self, service_till):
        return self.customer.get_no_of_items_in_basket() * service_till

class RegularLaneTime(CheckoutLaneTime):
    pass

class SelfServiceLaneTime(CheckoutLaneTime):
    pass

class TestCustomerDetails(unittest.TestCase):
    def setUp(self):
        self.customer1 = CustomerDetails()
        self.customer2 = CustomerDetails()
        self.checkout_lane1 = RegularLaneTime(self.customer1)
        self.checkout_lane2 = SelfServiceLaneTime(self.customer2)

    def test_get_no_of_items_in_basket(self):
        self.assertGreaterEqual(self.customer1.get_no_of_items_in_basket(), 1)
        self.assertLessEqual(self.customer1.get_no_of_items_in_basket(), 30)

    def test_lottery_ticket_award(self):
        self.assertIn(self.customer1.lottery_ticket_award(), [True, False])

    def test_calculate_checkout_time(self):
        time_regular = self.checkout_lane1.calculate_checkout_time('regular')
        time_self_service = self.checkout_lane2.calculate_checkout_time('self-service')

        self.assertIsInstance(time_regular, (int, float))
        self.assertIsInstance(time_self_service, (int, float))

    def test_display_customer_details(self):
        expected_output = "### Lucky Customer ###"  # Corrected the expected heading

        actual_output = self.customer1.display_customer_details(self.checkout_lane1)
        self.assertIn(expected_output, actual_output)

if __name__ == '__main__':
    unittest.main()
