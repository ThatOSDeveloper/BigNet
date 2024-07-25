import socket

def read_index_bnet(file_path):
    # Read content from the index.bnet file
    with open(file_path, 'r') as file:
        return file.read()

def handle_request():
    # Read content from index.bnet
    return read_index_bnet('index.bnet')

def start_server(host='0.0.0.0', port=8080):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)
    print(f"Server listening on {host}:{port}")

    while True:
        client_socket, addr = server_socket.accept()
        print(f"Connection from {addr}")
        request = client_socket.recv(1024).decode()
        print(f"Request received:\n{request}")

        # Handle request and send the raw content
        content = handle_request()
        client_socket.sendall(content.encode())
        client_socket.close()

if __name__ == "__main__":
    start_server()
