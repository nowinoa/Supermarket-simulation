#F2 - Coded by Ashmitha Aloshious - 001306808
class Customer:
    def __init__(self, id, basket):
        self.id = id
        self.basket = basket
        self.checkout = 0
        self.lottery_result = None

    def checkout_time(self, lane_type):
        if lane_type == 'slf':
            checkout_time = self.basket * 6
        else:
            checkout_time = self.basket * 4

        self.checkout = int(checkout_time)
        return self.checkout
    
    def get_items_in_basket(self, identifier):
        for customer in self.customers:
            if customer['identifier'] == identifier:
                return customer['items_in_basket']
        return None

    def lottery_function(self):
        if self.basket < 10:
            self.lottery_result = 'Hard luck, no lottery ticket this time!'
        else:
            self.lottery_result = 'Wins a lottery!, lucky'
        return self.lottery_result
    

    def customer_info(self):
        print(
            f'{self.id} --> items in basket: {self.basket}, checkout: {self.checkout}, Lottery Result: {self.lottery_function()}')
        