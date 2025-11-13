import requests

url = "https://real-time-amazon-data.p.rapidapi.com/search"

querystring = {"query":"shovel","page":"1","country":"US","sort_by":"RELEVANCE","product_condition":"ALL","is_prime":"false","deals_and_discounts":"NONE"}

headers = {
	"x-rapidapi-key": "c552623fe7mshd9712a58ac46689p1250c4jsne1ea665b16d2",
	"x-rapidapi-host": "real-time-amazon-data.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json()["data"]["product_price"])