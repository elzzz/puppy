from socket import socket, AF_INET, SOCK_STREAM, SOL_SOCKET, SO_REUSEADDR
from log import get_logger


LOG = get_logger()

def start_tcp_service(host, port):

    LOG = get_logger()
    tcp_socket = socket(AF_INET, SOCK_STREAM)
    tcp_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    LOG.debug('Set options SOL_SOCKET and SO_REUSEADDR.')
    tcp_socket.bind((host, port))
    LOG.debug('Bind socket to the address.')
    tcp_socket.listen(4)
    LOG.debug('Make number of the maximum connections equal 4.')

    tcp_dict = {}

    while True:
        print('\nListening for incoming connections...')
        LOG.debug('Listening for incoming connections.')
        conn, addr = tcp_socket.accept()
        LOG.debug('Accepting the connection.')
        tcp_dict[addr[0]] = conn
        print(tcp_dict)
        LOG.debug('Successful connection.')

