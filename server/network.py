import sys
from socket import socket, AF_INET, SOCK_STREAM, SOL_SOCKET, SO_REUSEADDR
sys.path.insert(0, '..')
sys.dont_write_bytecode = True
try:
    from lib.log import get_logger
    from lib.config import get_config
except:
    raise

CONNECTIONS = {}
LOG = get_logger()
MAX_CONNECTIONS = get_config('../cfg/server.toml')['network']['max_connections']


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
        LOG.info('''Accepting the connection from: {}
                 '''.format(str(CONNECTIONS[addr[0]])))


def send_msg():
    for value in CONNECTIONS.itervalues():
        return value


def execute_commands(agents_list, cmd_line):
    for agent in agents_list:
        LOG.info('Command: {}'.format(cmd_line))
        agent.send(cmd_line)


def get_connections():
    return CONNECTIONS


def get_enum_connections():

    enum_dict = {}
    key_pair = {}
    i = 0
    for key, value in CONNECTIONS.iteritems():
        key_pair[key] = value
        enum_dict[i] = key_pair
        i += 1
    return enum_dict
