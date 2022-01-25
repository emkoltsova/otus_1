import json
from csv import DictReader

with open("./data/users.json", "r") as f:
    users = json.loads(f.read())

res = [{'name': user['name'],
        'gender': user['gender'],
        'address': user['address'],
        'age': user['age'],
        'books': []} for user in users]

i = 0
users_qty = len(users)

with open('./data/books.csv', newline='') as f:
    reader = DictReader(f)

    for row in reader:
        res[i % users_qty]['books'].append(
            {'title': row['Title'], 'author': row['Author'], 'pages': row['Pages'], 'genre': row['Genre']})
        i += 1

with open("./data/result.json", "w") as f:
    s = json.dumps(res, indent=4)
    f.write(s)
