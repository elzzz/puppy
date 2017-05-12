from socket import socket, AF_INET, SOCK_STREAM, SOL_SOCKET, SO_REUSEADDR
from lib.log import get_logger
from lib.config import get_config
from menu import sending_msg

CONNECTIONS = {}
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

    while True:
        LOG.info('Listening for incoming connections.')
        conn, addr = tcp_socket.accept()
        CONNECTIONS[addr[0]] = conn
        if sending_msg() == 2:
            conn.send('msg')
        LOG.info('''Accepting the connection from: {}
                 '''.format(str(CONNECTIONS[addr[0]])))


def display_tcp_clients():
    for conn in CONNECTIONS.iterkeys():
        print(conn)
