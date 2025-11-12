import requests
API_KEY = "b96dc44f21b4a86575bc5037fa6e0aec45affa8f5e3c2f44c90c6e1bc2e53469"

bitcoin = float(input("How many bitcoins do you want to buy? "))

response = requests.get("https://rest.coincap.io/v3/assets/bitcoin")