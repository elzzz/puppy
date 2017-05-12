import menu
import network


def get_target_server():

    menu.display_tcp_clients()
    conn_list = network.get_connection()
    choice = int(input('Choose server: '))
    ip = conn_list[choice][0]
    print(ip)


def get_command():
    return 'ls -l'


def send_command():
    target_server = get_target_server()
    command = get_command()
    print(target_server)
    print(command)
