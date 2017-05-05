#!/usr/bin/env python

import sys
import threading
from network import start_tcp_service
from menu import print_menu

HOST = '0.0.0.0'
PORT = 9999

if __name__ == '__main__':

    TCP_SERVICE_THREAD = threading.Thread(target=start_tcp_service,
                                          args=(HOST, PORT))
    MENU_THREAD = threading.Thread(target=print_menu)

    TCP_SERVICE_THREAD.daemon = True
    MENU_THREAD.daemon = True

    TCP_SERVICE_THREAD.start()
    MENU_THREAD.start()

    try:
        while True:
            pass
    except (KeyboardInterrupt, SystemExit):
        sys.exit(0)
