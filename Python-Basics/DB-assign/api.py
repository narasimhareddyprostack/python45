import requests

response = requests.get('https://dummyjson.com/users')
user_dict = response.json()
users_list = user_dict['users']
data = []

for user in users_list:
    data.append((user['id'], user['firstName'], user['address']['city'],))


print(data)
