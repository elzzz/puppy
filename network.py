from socket import socket, AF_INET, SOCK_STREAM, SOL_SOCKET, SO_REUSEADDR


def start_tcp_service(host, port):

    tcp_socket = socket(AF_INET, SOCK_STREAM)
    tcp_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    tcp_socket.bind((host, port))
    tcp_socket.listen(4)

    tcp_dict = {}

    while True:
        print('\nListening for incoming connections...')
        conn, addr = tcp_socket.accept()
        tcp_dict[addr[0]]= conn
        print(tcp_dict)

