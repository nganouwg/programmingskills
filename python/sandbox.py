import pandas as pd

df = pd.DataFrame({
        "name": ["Alice", "Bob", "Charlie", "Diana"],
        "age": [25, 35, 30, 40],
        "score": [88, 70, 91, 95]
    })

#select * from my_table
print(df)

#Select name, score from my_table
print(df[["name", "score"]]) 