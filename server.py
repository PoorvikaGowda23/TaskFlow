import socket
import threading
import json
import os

# In-memory data storage for users and their to-do lists
users_data = {}
data_file = "C:/Users/poorvika/Desktop/VSC Folder/CN_VSC/tasks1.json"

# Ensure the data file exists; if not, create an empty file
if not os.path.exists(data_file):
    with open(data_file, 'w') as file:
        json.dump({}, file)

# Load data from file if it exists
with open(data_file, 'r') as file:
    users_data = json.load(file)

# Save the current data to file
def save_data():
    with open(data_file, 'w') as file:
        json.dump(users_data, file)

# Function to handle client requests
def handle_client(client_socket):
    while True:
        try:
            request = client_socket.recv(1024).decode('utf-8')
            if not request:
                break

            request_data = json.loads(request)
            action = request_data.get('action')

            if action == "register":
                username = request_data.get("username")
                if username in users_data:
                    response = {"status": "error", "message": "User already exists"}
                else:
                    users_data[username] = []
                    save_data()
                    response = {"status": "success", "message": f"User {username} registered"}

            elif action == "login":
                username = request_data.get("username")
                if username in users_data:
                    response = {"status": "success", "message": f"Welcome {username}"}
                else:
                    response = {"status": "error", "message": "User not found"}

            elif action == "add_task":
                username = request_data.get("username")
                task = request_data.get("task")
                if username in users_data:
                    users_data[username].append(task)
                    save_data()
                    response = {"status": "success", "message": "Task added"}
                else:
                    response = {"status": "error", "message": "User not found"}

            elif action == "view_tasks":
                username = request_data.get("username")
                if username in users_data:
                    tasks = users_data.get(username, [])
                    response = {"status": "success", "tasks": tasks}
                else:
                    response = {"status": "error", "message": "User not found"}

            elif action == "delete_task":
                username = request_data.get("username")
                task_index = request_data.get("task_index")
                if task_index is None or not isinstance(task_index, int):
                    response = {"status": "error", "message": "Task index is missing or invalid"}
                else:
                    task_index = int(task_index)
                    if username in users_data and 0 <= task_index < len(users_data[username]):
                        deleted_task = users_data[username].pop(task_index)
                        save_data()
                        response = {"status": "success", "message": f"Task '{deleted_task['description']}' deleted"}
                    else:
                        response = {"status": "error", "message": "Invalid task index"}

            client_socket.send(json.dumps(response).encode('utf-8'))

        except Exception as e:
            print(f"Error handling client: {e}")
            response = {"status": "error", "message": "An error occurred on the server"}
            client_socket.send(json.dumps(response).encode('utf-8'))
            break

    client_socket.close()

# Main server function
def server_program():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', 12346))
    server_socket.listen(5)
    print("Server started. Waiting for connections...")

    try:
        while True:
            client_socket, addr = server_socket.accept()
            print(f"Connection from {addr}")
            client_handler = threading.Thread(target=handle_client, args=(client_socket,))
            client_handler.start()
    except KeyboardInterrupt:
        print("Server shutting down...")
    finally:
        save_data()
        server_socket.close()

if __name__ == "__main__":
    server_program()
