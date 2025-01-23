import requests

BASE_URL = "http://127.0.0.1:8000/rest_apis/profile/"

# payload = {
# 	"username": "Samarth",
# 	"email": "samarthsjavalkoti@gmail.com",
# 	"password": "Pratham@2707"
# }

# headers = {
# 	"Content-Type":"application/json"
# }

test_username = input("Enter the username: ")

url = f"{BASE_URL}?username={test_username}"

response = requests.get(url)

print(response.status_code)

print(response.json())