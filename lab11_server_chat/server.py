import socket
import threading

# Dictionary to store the mapping of usernames to sockets
clients = {}

# Function to handle messages from clients
def handle_client(client_socket, username):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                client_socket.close()
                del clients[username]
                send_message_to_all(f"{username} left the chat")
                send_user_list_to_all()
                break
            send_message_to_all(f"{username}: {message}")
        except:
            client_socket.close()
            del clients[username]
            send_message_to_all(f"{username} left the chat")
            send_user_list_to_all()
            break

# Function to send a message to all clients
def send_message_to_all(message):
    for client in clients.values():
        client.send(bytes(message, 'utf-8'))

# Function to send the list of usernames to all clients
def send_user_list_to_all():
    user_list = ", ".join(clients.keys())
    for client in clients.values():
        client.send(bytes(f"Users online: {user_list}", 'utf-8'))

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('127.0.0.1', 5555))
    server_socket.listen(5)

    while True:
        client_socket, addr = server_socket.accept()
        print(f"Connection from {addr}")
        username = client_socket.recv(1024).decode('utf-8')
        if username in clients:
            client_socket.send("Username already taken. Please choose another one.".encode('utf-8'))
            client_socket.close()
        else:
            clients[username] = client_socket
            send_message_to_all(f"{username} joined the chat")
            send_user_list_to_all()
            client_thread = threading.Thread(target=handle_client, args=(client_socket, username))
            client_thread.start()

if __name__ == "__main__":
    main()
