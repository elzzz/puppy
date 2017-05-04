#!/usr/bin/env python

import threading
import socket

host = '0.0.0.0' 
port = 9999  

class FirstThread(threading.Thread): 
    
    def __init__(self, ip, port, socket): 
        threading.Thread.__init__(self)
	self.ip = ip 
	self.port = port
	self.socket = socket
	print('[+] New Thread Started For: ', ip, ':', str(port)) 

    def run(self): 
        print('Connection from: ', ip, ':', str(port)) 
	self.socket.send('\nWelcome to the server!\n\n') 
	data = 'mydata'
	
	while len(data):
	    data = self.socket.recv(2048) 
	    print('Client (%s:%s) sent : %s' %(self.ip, str(self.port), data)) 
	    self.socket.send('You sent me: ' + data) 
	print('Client at ', self.ip,  ' disconneted...') 



if __name__ == "__main__":
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    tcp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
    tcp_socket.bind((host, port)) 

    while True:
        tcp_socket.listen(4) 
        print('\nListening for incoming connections...') 
        (socket, (ip, port)) = tcp_socket.accept() 
    
        newthread = FirstThread(ip, port, socket) 
        newthread.start() 

    def print_menu():
        print(30 * '-', 'MENU', 30 * '-') 
        print('1. Menu Option 1') 
        print('2. Menu Option 2') 
        print('3. Menu Option 3') 
        print('4. Menu Option 4') 
        print('5. Exit')
        print(67 * '-')

    loop = True 

    while loop: 
        print_menu() 
        choice = int(raw_input('Enter your choice from 1 to 5: '))

        if choice==1: 
            print('Menu 1 has been selected')
        elif choice==2: 
            print('Menu 2 has been selected')
        elif choice==3: 
            print('Menu 3 has been selected')
        elif choice==4: 
            print('Menu 4 has been selected') 
        elif choice==5: 
            print('You selected \'Exit\'. Good Bye!')
            loop=False 
        else: 
            raw_input('Wrong option selection. Enter any key to try again..') 

    threading.Thread(target = print_menu).start() 
