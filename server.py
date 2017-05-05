#!/usr/bin/env python

import threading
from socket import *
from network import start_tcp_service
from menu import print_menu

host = '0.0.0.0' 
port = 9999  

if __name__ == '__main__':
    threading.Thread(target = start_tcp_service).start() 
    threading.Thread(target = print_menu).start() 
