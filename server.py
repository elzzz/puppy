#!/usr/bin/env python

import threading
from socket import *
from network import FirstThread
from menu import print_menu

host = '0.0.0.0' 
port = 9999  

FirstThread(target = TCP).start() 
threading.Thread(target = print_menu).start() 
