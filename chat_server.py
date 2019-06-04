import socket

print("-----Setting up chat server-----")

host = socket.gethostname()
print("host: ", host)
ip = socket.gethostbyname(host)
print("ip: ", ip)
PORT = 8081
socket_address_pair = (host, PORT)

server_socket = socket.socket()
server_socket.bind(socket_address_pair)

name = input("Enter your name: ")
print("Waiting for connection...")
server_socket.listen()
client_conn, client_address_pair = server_socket.accept()
print("Connection established from ")
print("client host: ", client_address_pair[0])
print("client_port: ", client_address_pair[1])

client_name = client_conn.recv(1024).decode()
print("User " + client_name + " has joined")

client_conn.send(name.encode())
print("Type quit to leave the chat room")
message = input(name + " writes ")

while message != "quit":
    client_conn.send(message.encode())
    print("waiting for answer...")
    client_message = client_conn.recv(1024).decode()
    print(client_name + " wrote " + client_message)
    message = input(name + " writes ")
    client_conn.send(message.encode())

if message == "quit":
    quit_message = "User " + name + " has left the chat room"
    client_conn.send(quit_message.encode())
    print("\n")
