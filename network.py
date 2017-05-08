from socket import socket, AF_INET, SOCK_STREAM, SOL_SOCKET, SO_REUSEADDR
from log import get_logger


LOG = get_logger()
NUMBER_OF_CONNECTIONS = 4

def start_tcp_service(host, port):

    tcp_socket = socket(AF_INET, SOCK_STREAM)
    tcp_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    LOG.info('Set options SOL_SOCKET and SO_REUSEADDR.')
    tcp_socket.bind((host, port))
    LOG.info('Bind socket to the address: {}:{}'.format(str(host), str(port)))
    tcp_socket.listen(NUMBER_OF_CONNECTIONS)
    LOG.info('''Make number of the maximum connections equal variable
                                        \'NUMBER_OF_CONNECTIONS\'.''')

    tcp_dict = {}

    while True:
        print('\nListening for incoming connections...')
        LOG.info('Listening for incoming connections.')
        conn, addr = tcp_socket.accept()
        tcp_dict[addr[0]] = conn
        LOG.info('Accepting the connection from: {}'.format(str(tcp_dict)))
