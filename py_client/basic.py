import requests


endpoint = "http://localhost:8080/checks/"

get_response = requests.get(endpoint)


print(get_response.text)
print(get_response.status_code)
# print(get_response.json)