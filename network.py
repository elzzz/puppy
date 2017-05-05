def start_tcp_service():
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

