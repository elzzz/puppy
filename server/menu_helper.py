import sys
import menu
import network
sys.dont_write_bytecode = True


def get_target_server():

    conn_list = network.get_enum_connections()
    menu.display_tcp_clients(conn_list)
    choice = int(input('Choose server: '))
    for i, conn in conn_list.iteritems():
        if i == choice:
            return conn.values()[0]
    print('Server ID not found')


def get_command():

    return raw_input('Type command: ')


def send_command():
    target_server = get_target_server()
    command = get_command()
    target_server.send(command)
