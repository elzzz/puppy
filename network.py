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

    def TCP(self):
        if __name__ == '__main__':
            ADDR = (host, port)
    	    IDDR = (ip, port)
    	    tcp_socket = socket(AF_INET, SOCK_STREAM)
   	    tcp_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
  	    tcp_socket.bind(ADDR)
  	    tcp_socket.listen(4)
  	    tcp_list[]

            while True:
                print('\nListening for incoming connections...')
                tcp_list.append([socket, IDDR]) = tcp_socket.accept()

