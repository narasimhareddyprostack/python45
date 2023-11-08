import pymongo

client = pymongo.MongoClient()

db = client['pro1']
col = db['user']

# print user first names

user_list = col.find({})

for user in user_list:
    print(user['first_name'])
