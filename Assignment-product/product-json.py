import requests
import json

resp = requests.get('https://dummyjson.com/products')

print(type(resp.json()))
print(type(resp.json()['products']))

fp = open('data.json', 'w')
new_Product_List = []

for product in resp.json()['products']:
    new_Product_List.append({"name": product['title'], "price": product['price'],
                            "brand": product['brand'], "stock": product['stock'], "avail": True})

# print(new_Product_List)
#json.dump(new_Product_List, fp)

# fp.close()
