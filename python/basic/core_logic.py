'''
 let's make the code more Pythonic by following the pattern below:
 
 expression, Interate over an iterable, Condition to be met
 This makes the code:
    1. More concise and readable 
    2. Clearly expressing that we are transforming one list into another. 
'''

#List Comprehension
sqr_list = [num**2 for num in range(1, 21) if num % 2 == 0]
print(sqr_list)


#Dictionary comprehension
scores = {"Alice": 90, "Bob": 85, "Eve": 70}
scores = {key: value + 5 for key, value in scores.items()}
print(scores)


#String Parsing
emails = ["alice@gmail.com", "bob@outlier.ai", "eve@example.org"]
domains = [email.split("@")[1] for email in emails]
print(domains)
