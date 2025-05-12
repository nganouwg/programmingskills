
from collections import Counter
import pandas as pd 

def most_frequent_word(text):
    words = text.split()
    word_count = Counter(words)

    return max(word_count, key=word_count.get)

most_frequent_word("dog cat dog bird dog cat")


import pandas as pd

def get_average():
    df = pd.DataFrame({
        "Name": ["Alice", "Bob", "Charlie", "Diana"],
        "Math": [88, 70, 91, 95],
        "English": [85, 90, 78, 82]
    })

    df['Average'] = (df['Math'] + df['English']) / 2

    return df[df['Average'] >= 85]

print(get_average())


class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    def promote(self, percent):
        if self.salary < 100000:
            self.salary = (self.salary * percent / 100) + self.salary


def reverse_words_case(text):
    return ' '.join(text.split()[::-1])

print(reverse_words_case("Python is FUN"))