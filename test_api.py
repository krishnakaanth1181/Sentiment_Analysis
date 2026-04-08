import requests

url = "http://127.0.0.1:5000/predict"
data = {"reviews": "Worst nightmare. Brilliant direction !! Thrilling !!!"}

response = requests.post(url, json=data)
print(response.json())