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

clean_df = df[pd.notna(df['name']) & pd.notna(df['score'])]
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