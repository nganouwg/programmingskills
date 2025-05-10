import pandas as pd

def is_anagram(my_str1, my_str2):

    my_str1_sorted = "".join(sorted(my_str1))
    my_str2_sorted = "".join(sorted(my_str2))

    if my_str1_sorted == my_str2_sorted:
        return True
    else:
        return False
    
def dataframe_filter():
    df = pd.DataFrame({
        "name": ["Alice", "Bob", "Charlie", "Diana"],
        "age": [25, 35, 30, 40],
        "score": [88, 70, 91, 95]
    })


    df_filtered = df[df["score"] > 85].copy()
    df_score = df_filtered['score'].sort_values(ascending=False)

    return df_score

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def is_valid_email(self):
        if self.email.find(".") and self.email.find("@"):
            return True
        else:
            False

def aggregate_purchases(purchases):
    pass

purchases = [
    {"user": "Alice", "amount": 50},
    {"user": "Bob", "amount": 30},
    {"user": "Alice", "amount": 25}
]

print(aggregate_purchases(purchases))