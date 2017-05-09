from socket import socket, AF_INET, SOCK_STREAM, SOL_SOCKET, SO_REUSEADDR
from lib.log import get_logger
from lib.config import get_config


LOG = get_logger()
MAX_CONNECTIONS = get_config('cfg/server.toml')['network']['max_connections']

def start_tcp_service(host, port):

    tcp_socket = socket(AF_INET, SOCK_STREAM)
    tcp_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    LOG.info('Set options SOL_SOCKET and SO_REUSEADDR.')
    tcp_socket.bind((host, port))
    LOG.info('Bind socket to the address: {}:{}'.format(str(host), str(port)))
    tcp_socket.listen(MAX_CONNECTIONS)
    LOG.info('''Make number of the maximum connections equal: {}
                             '''.format(str(MAX_CONNECTIONS)))

    tcp_dict = {}

    while True:
        LOG.info('Listening for incoming connections.')
        conn, addr = tcp_socket.accept()
        tcp_dict[addr[0]] = conn
        LOG.info('Accepting the connection from: {}'.format(str(tcp_dict)))
