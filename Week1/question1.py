import requests
x = requests.get("--Write your URL--")
print(x.text)
print(x.status_code)
print(x.headers)
print(x.request)
print(x.encoding)
print(x.apparent_encoding)
print(x.history)
