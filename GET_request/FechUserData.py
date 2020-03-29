import requests
# API url

url = "https://reqres.in/api/users?page=2"

#send get request

response =requests.get(url)
#display response content
print(response.content)
print(response.headers)

