'''
    Here are some improvement or recommended adjustments. 

    1. When converting the score datatype to int, it can trigger a SettingWithCopyWarning, because clean_df may be a view of the original df.
       So, the copy() method ensures you're working on a copy, not a view — avoiding unexpected bugs in more complex pipelines.
    2. Use dropna, instead of notna to make the code expressive and concise

'''

import pandas as pd

#pd_list = dir(pd)
#print(pd_list)

#Pandas DataFrame Cleanup
df = pd.DataFrame({
    "id": [1, 2, 3, 4],
    "name": ["Alice", "Bob", None, "Eve"],
    "score": [88, None, 91, 70]
})

#SQL: Delete from myTable where name is null or score is null
#SQL Update myTable set score = Cast(score as int)

#print(df)

clean_df = df.dropna(subset=["name", "score"]).copy()
clean_df['score'] = clean_df['score'].astype(int)

print(clean_df)

#JSON Flattening
data = {
    "user": {
        "name": "Alice",
        "profile": {"age": 30, "city": "NY"}
    }
}

df = pd.json_normalize(data, sep="_")
print(df)

data2 = [
    {
        "user": {
            "name": "Alice",
            "profile": {"age": 30, "city": "NY"}
        }
    },
    {
        "user": {
            "name": "Bob",
            "profile": {"age": 25, "city": "LA"}
        }
    }
]

df2 = pd.json_normalize(data2, sep="_")
print(df2)