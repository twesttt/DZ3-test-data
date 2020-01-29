import json
import pandas as pd


with open("users.json", "r") as read_file:
    users_data = json.load(read_file)

users_list = []

for user in users_data:
    users_list.append({'name': user['name'], 'gender': user['gender'], 'address': user['address']})


books = pd.read_csv('books.csv', delimiter=',')

books_info = books[['Title', 'Author', 'Height']]
books_dict = books_info.to_dict('records')


x = 0
for i in users_list:
    i['books'] = books_dict[x]
    x += 1


result = json.dumps(users_list, indent=4)
print(result)




