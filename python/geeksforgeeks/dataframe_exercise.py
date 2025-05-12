'''

Selecting rows based on particular column value using '>', '=', '=', '<=', '!=' operator.

'''

import pandas as pd

record = {
    'Name': ['Ankit', 'Amit', 'Aishwarya', 'Priyanka', 'Priya', 'Shaurya' ],
    'Age': [21, 19, 20, 18, 17, 21],
    'Stream': ['Math', 'Commerce', 'Science', 'Math', 'Math', 'Science'],
    'Percentage': [88, 92, 95, 70, 65, 78]
}

df = pd.DataFrame(record, columns = ['Name', 'Age', 'Stream', 'Percentage'])

print(df)
print('\n')

#   Selecting all the rows from the given dataframe in which ‘Percentage’ is greater than 80 using basic method.
#print(df[df['Percentage'] > 80])

#   Selecting all the rows from the given dataframe in which ‘Percentage’ is greater than 80 using loc.
#print(df.loc[df['Percentage'] > 80])

#   Selecting all the rows from the given dataframe in which ‘Stream’ is present in the options list using basic method.
#options = ['Math', 'Commerce']
#print(df[df['Stream'].isin(options)])

#   Selecting all the rows from the given dataframe in which ‘Stream’ is not present in the options list using .loc[] .
options = ['Math', 'Science']
#print(df.loc[~df['Stream'].isin(options)])


'''

Selecting rows based on multiple column conditions using '&' operator.

'''

#   Selecting all the rows from the given dataframe in which ‘Age’ is equal to 21 and ‘Stream’ is present in the options list using basic method.
print(df[(df['Age'] == 21) & df['Stream'].isin(options)])