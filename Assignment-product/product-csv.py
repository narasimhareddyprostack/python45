import requests
import csv

resp = requests.get('https://dummyjson.com/products')

print(type(resp.json()))
print(type(resp.json()['products']))


fp = open('data.csv', 'w', newline='')
csvwriteobj = csv.writer(fp)
csvwriteobj.writerow(['Name', 'Price', 'Brand', 'Stock'])

for product in resp.json()['products']:
    # print(product['title'])
    csvwriteobj.writerow(
        [product['title'], product['price'], product['brand'], product['stock']])


fp.close()
