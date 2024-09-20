import json
import socket
import threading
from flask import Flask, request, jsonify, render_template
import os 

app = Flask(__name__)

# Load existing users from JSON file
if os.path.exists('users.json'):
    with open('users.json', 'r') as f:
        users = json.load(f)
else:
    users = {}

@app.route('/')
def home():
    return render_template('index.html')

# Route for user registration
@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    if username in users:
        return jsonify({'message': 'Username already exists!'}), 400
    users[username] = []  # Initialize an empty task list for the new user
    # Save users to a JSON file
    with open('users.json', 'w') as f:
        json.dump(users, f)
    return jsonify({'message': f'Registration successful for {username}!'})

# Route for user login
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    if username not in users:
        return jsonify({'message': 'Username not found, please register first!'}), 400
    return jsonify({'message': f'Login successful for {username}!', 'status': 'success'})

# Route to add a new task
@app.route('/add_task', methods=['POST'])
def add_task():
    data = request.get_json()
    username = data.get('username')
    task = data.get('task')
    if username in users:
        users[username].append(task)
        with open('users.json', 'w') as f:
            json.dump(users, f)
        # Broadcast the task update to all connected clients
        broadcast_task_update(username)
        return jsonify({'message': 'Task added successfully!'})
    return jsonify({'message': 'User not found!'}), 400

# Route to view tasks for a user
@app.route('/view_tasks', methods=['GET'])
def view_tasks():
    username = request.args.get('username')
    if username in users:
        return jsonify({'tasks': users[username]}), 200
    return jsonify({'message': 'User not found!'}), 400

# Route to delete a task
@app.route('/delete_task', methods=['POST'])
def delete_task():
    data = request.get_json()
    username = data.get('username')
    task_index = data.get('task_index')
    if username in users and 0 <= task_index < len(users[username]):
        del users[username][task_index]
        with open('users.json', 'w') as f:
            json.dump(users, f)
        # Broadcast the task update to all connected clients
        broadcast_task_update(username)
        return jsonify({'message': 'Task deleted successfully!'})
    return jsonify({'message': 'Invalid task or user!'}), 400

# Route to edit a task
@app.route('/edit_task', methods=['POST'])
def edit_task():
    data = request.get_json()
    username = data.get('username')
    task_index = data.get('task_index')
    new_task = data.get('new_task')
    if username in users and 0 <= task_index < len(users[username]):
        users[username][task_index] = new_task
        with open('users.json', 'w') as f:
            json.dump(users, f)
        # Broadcast the task update to all connected clients
        broadcast_task_update(username)
        return jsonify({'message': 'Task updated successfully!'})
    return jsonify({'message': 'Invalid task or user!'}), 400

# Function to broadcast task updates to all connected clients
def broadcast_task_update(username):
    message = f"Task update for {username}: {users[username]}"
    for client in clients:
        client.sendall(message.encode('utf-8'))

# List to hold connected clients
clients = []

# Socket server function
def socket_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 1017))
    server_socket.listen(5)
    print("Socket server started and listening...")

    while True:
        client_socket, addr = server_socket.accept()
        print(f"Client connected: {addr}")
        clients.append(client_socket)

        threading.Thread(target=handle_client, args=(client_socket,)).start()

def handle_client(client_socket):
    while True:
        try:
            data = client_socket.recv(1024)
            if not data:
                break
            print(f"Received data from client: {data.decode('utf-8')}")
        except Exception as e:
            print("Error:", e)
            break
    client_socket.close()
    clients.remove(client_socket)

if __name__ == '__main__':
    threading.Thread(target=socket_server, daemon=True).start()
    app.run(debug=True)
