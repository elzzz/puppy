#!/usr/bin/env python

import sys
import threading
from network import start_tcp_service
from menu import print_menu
from log import get_logger


HOST = '0.0.0.0'
PORT = 9999
LOG = get_logger()

if __name__ == '__main__':

    TCP_SERVICE_THREAD = threading.Thread(target=start_tcp_service,
                                          args=(HOST, PORT))
    MENU_THREAD = threading.Thread(target=print_menu)

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
