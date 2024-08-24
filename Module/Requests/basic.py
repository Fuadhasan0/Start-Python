import requests

url = "https://www.w3schools.com/"

response_main = requests.get(url)
response_ok = response_main.ok
response_status_code = response_main.status_code
response_reason = response_main.reason

print(response_main)
print(response_ok)
print(response_status_code)
print(response_reason)

url = "https://www.w3schools.com/abc.html"

response_main = requests.get(url)
response_ok = response_main.ok
response_status_code = response_main.status_code
response_reason = response_main.reason

print(response_main)
print(response_ok)
print(response_status_code)
print(response_reason)