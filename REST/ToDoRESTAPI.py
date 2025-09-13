import requests

# Base URL for the REST API
BASE_URL = "https://jsonplaceholder.typicode.com/todos"

# 1. Get a list of to-dos
response = requests.get(BASE_URL)
todos = response.json()
print("First 3 to-dos:")
for todo in todos[:3]:
    print(f"ID: {todo['id']} - Task: {todo['title']} - Done: {todo['completed']}")

# 2. Get a specific to-do
todo_id = 1
response = requests.get(f"{BASE_URL}/{todo_id}")
todo = response.json()
print("\nSpecific to-do (ID 1):")
print(todo)

# 3. Create a new to-do (POST)
new_todo = {
    "userId": 1,
    "title": "Learn REST APIs with Python",
    "completed": False
}
response = requests.post(BASE_URL, json=new_todo)
print("\nCreated to-do:")
print(response.json())

# 4. Update a to-do (PUT)
updated_todo = {
    "userId": 1,
    "title": "Learn REST APIs with Python (Updated)",
    "completed": True
}
response = requests.put(f"{BASE_URL}/{todo_id}", json=updated_todo)
print("\nUpdated to-do:")
print(response.json())

# 5. Delete a to-do (DELETE)
response = requests.delete(f"{BASE_URL}/{todo_id}")
print("\nDeleted to-do status code:", response.status_code)
