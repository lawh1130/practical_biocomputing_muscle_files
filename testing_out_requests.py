#here I will test out "requests", which I think will make my life substantially easier


import requests
api_url = "https://jsonplaceholder.typicode.com/todos/1"
response = requests.get(api_url)
print(response.json())

#woo it works

#now to test out POST

api_url = "https://jsonplaceholder.typicode.com/todos"
todo = {"userId": 1, "title": "Buy milk", "completed": False}
response = requests.post(api_url, json=todo)
print(response.json())

print(response.status_code)

#excellent

#now maybe try with python?


