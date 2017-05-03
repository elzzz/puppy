#!/usr/bin/env python

import threading, socket

# Number one (binding one thread to TCP-socket).
class FirstThread(threading.Thread): #Class for my first thread.
    
    def __init__(self, ip, port, socket): #Class constructor with attributes: main 'self' and 'ip, port, socket'
        threading.Thread.__init__(self)
	self.ip = ip 
	self.port = port
	self.socket = socket
	print '[+] New Thread Started For: ' + ip + ':' + str(port) #Print where the thread is starting.

    def run(self): #My function 'run'
        print 'Connection from: ' + ip + ':' + str(port) #Print from where somebody is connected.
	self.socket.send('\nWelcome to the server!\n\n') # Sending a message to the client.
	data = 'mydata'
	
	while len(data):
	    data = self.socket.recv(2048) #Buffer Size '2 KiB'
	    print 'Client (%s:%s) sent : %s' %(self.ip, str(self.port), data) # Print how much did client with this address send me.
	    self.socket.send('You sent me: ' + data) # Print for client how much did he send me.
	print 'Client at ' + self.ip +  ' disconneted...' # While not len(data) printing that client at that ip disconnected.

host = '0.0.0.0' # host with ip '0.0.0.0', so we can listen all interfaces.
port = 9999  # and port '9999' TELNET control

tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Creating an INET and STREAMing socket in variable 'tcp_socket'
tcp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # Many applications can listen socket.
tcp_socket.bind((host, port)) # Bind socket to this adress.

while True:
    tcp_socket.listen(4) # Become a server socket.
    print '\nListening for incoming connections...' # Print that we are waiting for incoming connection.
    (socket, (ip, port)) = tcp_socket.accept() #Accept connections from outside.
    
    newthread = FirstThread(ip, port, socket) # Pass socket to the FirstThread thread object being created.
    newthread.start() # Start thread for a new client.

# Number two (Thread display console menu with any text).
def print_menu():
    print 30 * '-', 'MENU', 30 * '-' # Lines with MENU at the edge.
    print '1. Menu Option 1' # 1st menu.
    print '2. Menu Option 2' # 2nd menu.
    print '3. Menu Option 3' # 3rd menu.
    print '4. Menu Option 4' # 4th menu.
    print '5. Exit' # Exit menu.
    print 67 * '-' # Lines

loop = True # Variable Loop for while.

while loop: # While loop = True
    print_menu() # Display our quite primitive menu.
    choice = int(raw_input('Enter your choice from 1 to 5: ')) # Choice the number of menu paragraph.

    if choice==1: # If you choice equal 1
        print 'Menu 1 has been selected' # Print selected paragraph.
    elif choice==2: # If you choice equal 2
        print 'Menu 2 has been selected' # Print selected paragraph.
    elif choice==3: # If you choice equal 3
        print 'Menu 3 has been selected' # Print selected paragraph.
    elif choice==4: # If you choice equal 4
        print 'Menu 4 has been selected' # Print selected paragraph.
    elif choice==5: # If you choice equal 5
        print 'You selected \'Exit\'. Good Bye!' # Print selected paragraph.
        loop=False # This will make the while loop to end as not value of loop is set to False.
    else: 
        raw_input('Wrong option selection. Enter any key to try again..') # Your choice was not from 1 to 5.

threading.Thread(target = print_menu).start() # Start our menu in threading.
