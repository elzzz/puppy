#!/usr/bin/env python

import sys
import threading
from network import start_tcp_service
from menu import print_menu
sys.path.insert(0, '..')
sys.dont_write_bytecode = True
try:
    from lib.log import get_logger
    from lib.config import get_config
except:
    raise

HOST = get_config('../cfg/server.toml')['network']['interface']
PORT = get_config('../cfg/server.toml')['network']['port']
LOG = get_logger()

if __name__ == '__main__':

    TCP_SERVICE_THREAD = threading.Thread(name='tcpserver',
                                          target=start_tcp_service,
                                          args=(HOST, PORT))
    MENU_THREAD = threading.Thread(name='menu',
                                   target=print_menu)

    TCP_SERVICE_THREAD.daemon = True
    LOG.info('Daemonizing thread with TCP SERVICE.')
    MENU_THREAD.daemon = True
    LOG.info('Daemonizing thread with menu.')

    TCP_SERVICE_THREAD.start()
    LOG.info('Starting thread with TCP SERVICE.')
    MENU_THREAD.start()
    LOG.info('Starting thread with menu.')

    try:
        while True:
            pass
    except (KeyboardInterrupt, SystemExit):
        LOG.info('Exit')
        sys.exit(0)
