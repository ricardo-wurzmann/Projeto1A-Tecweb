import socket
from pathlib import Path
from utils import extract_route, read_file, build_response
from views import index, delete_note, edit_note, create_note

CUR_DIR = Path(__file__).parent
SERVER_HOST = 'localhost'
SERVER_PORT = 8080

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((SERVER_HOST, SERVER_PORT))
server_socket.listen()

print(f'Servidor escutando em (ctrl+click): http://{SERVER_HOST}:{SERVER_PORT}')

while True:
    client_connection, client_address = server_socket.accept()

    request = client_connection.recv(1024).decode()
    print('*'*100)
    print(request)

    route = extract_route(request)

    filepath = CUR_DIR / route
    if filepath.is_file():
        response = response = build_response() + read_file(filepath)
    elif route == '':
        response = index(request)
    elif route.startswith("delete"):
        response = delete_note(route)
    elif route.startswith("edit"):
        response = edit_note(route)
    else:
        response = build_response()
    
    def parse_request_method(request):
        return request.split()[0]

    request_method = parse_request_method(request)


    if route == 'POST /create':
        response = create_note(request)
    
    client_connection.sendall(response)

    client_connection.close()

server_socket.close()