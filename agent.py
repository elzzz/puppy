#!/usr/bin/env python

from socket import socket, AF_INET, SOCK_STREAM
from lib.log import get_logger
from lib.config import get_config

HOST = get_config('cfg/client.toml')['client']['interface']
PORT = get_config('cfg/client.toml')['client']['port']
LOG = get_logger()


def connect_agent():
    sock = socket(AF_INET, SOCK_STREAM)
    addr = (HOST, PORT)
    LOG.info('Connecting to {} port {}.'.format(str(HOST), str(PORT)))
    sock.connect(addr)

    try:

        message = 'Insane client msg.'
        LOG.info('Sending {}.'.format(message))
        sock.sendall(message)

        amount_received = 0
        amount_expected = len(message)
        while amount_received < amount_expected:
            data = sock.recv(16)
            amount_received += len(data)
            LOG.info('Received {}'.format(data))

    finally:
        sock.close()
