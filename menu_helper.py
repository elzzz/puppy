import menu
import network


def get_target_server():

    conn_list = network.get_enum_connections()
    menu.display_tcp_clients(conn_list)
    choice = int(input('Choose server: '))
    for i, conn in conn_list.iteritems():
        if i == choice:
            return conn.values()[0]
    print('Server ID not found')


def get_command():
    return 'ls -l'


def send_command():
    target_server = get_target_server()
    command = get_command()
    print(target_server)
    print(command)
