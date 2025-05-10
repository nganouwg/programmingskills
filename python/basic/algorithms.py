
'''
    Factorial:
        Make the code more Pythonic, using recursive function to make it more concise, 
        and add error-checking for negative values

    dectect duplites:
        Use sets. Compare the number of items in the set and number of items in the list. 

    csv parsing:
        Introduce a reusable function
'''

import pandas as pd
from collections import Counter

def factorial(num):
    if num < 0:
        raise ValueError("Factorial is undefined for negative numbers")
    return 1 if num == 0 else num * factorial(num - 1)

def detect_duplicate(ids):
    return len(ids) != len(set(ids))


def csv_parsing(filepath):

    df = pd.read_csv(filepath)

    #return the top 5 rows where a column "score" is above x (e.g 3)
    #SQL: Select top 5 * from games where score > x order by score desc
    top_n = 5
    score_threshold = 3
    column_name = 'Home Goals'

    def top_scores(df, column="Home Goals", threshold=3, top_n=5):
        return df[df[column] > threshold].sort_values(by=column, ascending=False).head(top_n)

    df_top_scores = top_scores(df, column_name, score_threshold, top_n)
    print(df_top_scores)


if __name__ == "__main__":
    print(factorial(3))

    user_ids = [1001, 1002, 1003, 1002]
    print(user_ids)
    print("Has Duplicates : ", detect_duplicate(user_ids))

    csv_parsing('/Users/georgesnganou/Documents/Projects/VS_Code/programming/sample_data/kagglehub/archive/world_cup_matches1.csv')

