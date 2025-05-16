

import re
import math
import pandas as pd

def symmetric_difference(a, b):

    set_a = set(a)
    set_b = set(b)

    return set_a ^ set_b

a = [1, 2, 3, 4]
b = [3, 4, 5, 6]
print(symmetric_difference(a, b))


def clean_sentence(text:str):

    new_text = re.sub(r"[.,!]", "", text)
    words = new_text.lower().split()
    return list(set(words))

print(clean_sentence("Hello, world! Hello Python."))


df = pd.DataFrame({
    "Department": ["Sales", "Sales", "HR", "HR", "IT", "IT"],
    "Employee": ["Alice", "Bob", "Carol", "Dave", "Eve", "Frank"],
    "Salary": [70000, 80000, 60000, 65000, 90000, 87000]
})

def average_salary_by_depart(df):
    dept_avg = df.groupby('Department')['Salary'].mean()
    return dept_avg.idxmax()

print(average_salary_by_depart(df))



class InventoryItem:
    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price

    def total_value(self):
        return self.price * self.quantity
    


def to_euros(usd_prices:dict):

    for key, value in usd_prices.items():
        usd_prices[key] = value * 0.85

    return usd_prices


usd_prices = {"apple": 1.00, "banana": 0.50, "cherry": 2.00}
print(to_euros(usd_prices))


def assign_groups(students, group_size):
    
    num_groups = math.ceil(len(students) / group_size)
    groups = []

    for i in range(num_groups):
        group = []
        s = 0
        while s < group_size:
            if len(students) == 0:
                break
            group.append(students.pop(0))
            s += 1

        groups.append(group)

    return(groups)

print(assign_groups(["A", "B", "C", "D", "E"], 2))