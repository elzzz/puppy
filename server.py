#!/usr/bin/env python

import threading
import socket
import network
from menu import print_menu

host = '0.0.0.0' 
port = 9999  


if __name__ == "__main__":

    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    tcp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
    tcp_socket.bind((host, port)) 

    while True:
        tcp_socket.listen(4) 
        print('\nListening for incoming connections...') 
        (socket, (ip, port)) = tcp_socket.accept() 
    
        newthread = network.FirstThread(ip, port, socket) 
        newthread.start() 



    threading.Thread(target = print_menu).start() 
