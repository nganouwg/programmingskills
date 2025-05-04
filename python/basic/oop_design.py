
#Class Implementation
class product(object):
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def apply_discount(self, percent):
        discounted_price = self.price * percent / 100
        return self.price - discounted_price
    

