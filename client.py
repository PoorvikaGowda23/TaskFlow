import socket
import json

# Function to send a request to the server
def send_request(request):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('127.0.0.1', 12346))
    client_socket.send(json.dumps(request).encode('utf-8'))
    response = client_socket.recv(1024).decode('utf-8')
    client_socket.close()
    return json.loads(response)
