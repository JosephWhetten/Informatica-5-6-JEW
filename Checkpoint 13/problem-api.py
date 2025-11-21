import requests
import json

item = input("What item do you want to get the cost of? ")


url = "https://real-time-amazon-data.p.rapidapi.com/search"
querystring = {"query":item,"page":"1","country":"US","sort_by":"RELEVANCE","product_condition":"ALL","is_prime":"false","deals_and_discounts":"NONE"}
headers = {
	"x-rapidapi-key": "c552623fe7mshd9712a58ac46689p1250c4jsne1ea665b16d2",
	"x-rapidapi-host": "real-time-amazon-data.p.rapidapi.com"
}
response = requests.get(url, headers=headers, params=querystring)

# print(response.json())
# for price in response.json()["data"]["products"]:
#     print(price["produce_price"])

prices = []
for price in response.json()["data"]["products"]:
    prices.append(float(price["product_price"].replace("$","").replace(",","")))
    
print(f"The max price is: ${max(prices)}")
print(f"The minimum price is: ${min(prices)}")
total = 0
for money in prices:
    total += money
print(f"The average price is: ${total/len(prices):.2f}")