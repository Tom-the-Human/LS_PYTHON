# NEVER USE CTRL+Z to end programs that bind ports! Only CTRL+C!

import socket
import random

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(('localhost', 3003))
server_socket.listen()

print("Server is running on localhost:3003")

def parse_query(request_line):
    # this works, but clumsy as hell, could refactor to split on '?', 
    # and make dict of key, val pairs via subsequent splits on '&' and '='
    rolls = 1
    sides = 6

    method, path, version = request_line.split()
    path = path.strip('/?')
    if path == '/':
        return rolls, sides
    elif '&' in path:
        params = path.split('&')
    else:
        if 'rolls' in path:
            rolls = path[6:]
        elif 'sides' in path:
            sides = path[6:]
        return int(rolls), int(sides)
    
    for param in params:
        if 'rolls=' in param:
            rolls = param[6:]
        if 'sides=' in param:
            sides = param[6:]

    return int(rolls), int(sides)

server_socket.bind(('localhost', 3002))
server_socket.listen()

print("Server is running on localhost:3002")

while True:
    client_socket, addr = server_socket.accept()
    print(f"Connection from {addr}")

    request = client_socket.recv(1024).decode()
    if not request or 'favicon.ico' in request:
        client_socket.close()
        continue

    request_line = request.splitlines()[0]
    print(request_line)

    rolls, sides = parse_query(request_line)

    response_body = f"<html><head><title>{request_line}</title></head><body><ul>"
    for roll in range(0, rolls):
        roll = random.randint(1, sides)
        response_body += f"<li>Roll: {roll}</li>"

    response = ("<p>HTTP/1.1 200 OK\r\n"
                "Content-Type: text/html\r\n"
                f"Content-Length: {len(response_body)}\r\n"
                "\r\n"
                f"{response_body}</ul></body></html>")

    client_socket.sendall(response.encode())
    client_socket.close()