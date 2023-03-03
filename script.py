import requests

url = 'https://www.latestind.com'
response = requests.get(url)
print(response.text)
