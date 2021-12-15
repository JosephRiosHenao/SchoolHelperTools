import requests 
import json

url = "https://api.coinstats.app/public/v1/coins"
params = "?skip=0&limit=5&currency=EUR"

urlFinal = url+params

response = requests.get(urlFinal)

jsonResponse = json.loads(response.content)

print(jsonResponse)