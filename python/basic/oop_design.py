
'''
    Class naming convention is PascalCase
    
    Should the apply discount simple return or also update the product price? 
        If it should also update, include an expression to do that
    Include a condition to make sure the discount is only applied once

    Included __repr__ to get the string representation of the object, 
    which makes it easier to inspect during testing
'''

#Class Implementation
class Product:
    def __init__(self, name, price, has_applied_discount=False):
        self.name = name
        self.price = price
        self.has_applied_discount = has_applied_discount

    def apply_discount(self, percent):
        if not self.has_applied_discount:
            discounted_price = self.price * percent / 100
            self.price -= discounted_price
            self.has_applied_discount = True
        return self.price
    
    def __repr__(self):
        return f"Product(name='{self.name}', price={self.price:.2f})"
    

p = Product("Monitor", 300)
print(p)                    
print(p.apply_discount(20)) 
print(p.apply_discount(20)) 
print(p)                    