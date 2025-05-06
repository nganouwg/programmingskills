
#List Comprehension
sqr_list = []
for num in range(1, 21):
    if num % 2 == 0:
        sqr_list.append(num**2)

print(sqr_list)


#Dictionary comprehension
scores = {"Alice": 90, "Bob": 85, "Eve": 70}
for key in scores:
    scores[key] += 5

print(scores)


#String Parsing
domains = []
emails = ["alice@gmail.com", "bob@outlier.ai", "eve@example.org"]
for email in emails:
    domains.append(email.split("@")[1])

print(domains)
