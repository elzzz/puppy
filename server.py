#!/usr/bin/env python

import sys
import threading
from network import start_tcp_service
from menu import print_menu
from logbook import Logger, StreamHandler

HOST = '0.0.0.0'
PORT = 9999
StreamHandler(sys.stdout).push_application()
log = Logger('Test Logger')

if __name__ == '__main__':

    TCP_SERVICE_THREAD = threading.Thread(target=start_tcp_service,
                                          args=(HOST, PORT))
    MENU_THREAD = threading.Thread(target=print_menu)

    TCP_SERVICE_THREAD.daemon = True
    log.debug('Daemoning thread with TCP SERVICE.')
    MENU_THREAD.daemon = True
    log.debug('Daemoning thread with menu.')

    TCP_SERVICE_THREAD.start()
    log.debug('Starting thread with TCP SERVICE.')
    MENU_THREAD.start()
    log.debug('Starting thread with menu.')

    try:
        while True:
            pass
    except (KeyboardInterrupt, SystemExit):
        log.debug('Exit')
        sys.exit(0)
