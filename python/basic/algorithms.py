
import pandas as pd
from collections import Counter

def factorial(num):

    total = 1
    for i in range(1, num+1):
        total *= i
    print(total)

def detect_duplicate(user_ids):

    counts = Counter(user_ids)
    dups = [id for id, count in counts.items() if count > 1]
    print(dups)


def csv_parsing(filepath):

    df = pd.read_csv(filepath)
    print(df)

    #return the top 5 rows where a column "score" is above x (e.g 3)
    #SQL: Select top 5 * from games where score > x order by score desc
    score_threshold = 3
    df_score_threshold = df[df['Home Goals'] > score_threshold]
    
    print(df_score_threshold)

    df_score_threshold_desc = df_score_threshold.sort_values(by='Home Goals', ascending=False)

    print(df_score_threshold_desc)

    #top 5
    print(df_score_threshold_desc.head(5))
    

if __name__ == "__main__":
    factorial(3)

    user_ids = [1001, 1002, 1003, 1002]
    detect_duplicate(user_ids)

    csv_parsing('/Users/georgesnganou/Documents/Projects/VS_Code/programming/sample_data/kagglehub/archive/world_cup_matches1.csv')

