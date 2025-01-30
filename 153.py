import requests

name = 'Michael Jordan'
api_url = 'https://api.api-ninjas.com/v1/celebrity?name={}'.format(name)
response = requests.get(api_url, headers={'X-Api-Key': 'YOUR_API_KEY'})
if response.status_code == requests.codes.ok:
    print(response.text)
else:
    print("Error:", response.status_code, response.text)
