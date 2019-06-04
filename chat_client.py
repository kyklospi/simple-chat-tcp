import socket

print("-----Setting up client server -----")

host = socket.gethostname()
print("host: ", host)
ip = socket.gethostbyname(host)
print("ip: ", ip)
PORT = 8081

server_ip = input("Enter IP address of chat server: ")

server_address_pair = (server_ip, PORT)
client_socket = socket.socket()
client_socket.connect(server_address_pair)
print("Connected to server")
name = input("Enter your name: ")
client_socket.send(name.encode())

server_name = client_socket.recv(1024).decode()
print("User " + server_name + " is connected")

print("Type quit to leave the chat room")
message = None

while message != "quit":
    print("waiting for answer...")
    server_message = client_socket.recv(1024).decode()
    print(server_name + " wrote " + server_message)
    message = input(name + " writes ")
    client_socket.send(message.encode())

if message == "quit":
    quit_message = "User " + name + " has left the chat room"
    client_socket.send(quit_message.encode())
    print("\n")
