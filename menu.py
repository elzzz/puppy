import sys
import threading
import network
import menu_helper

CONNECTIONS = network.get_connection()


def print_menu():
    print(30 * '-', 'MENU', 30 * '-')
    print('1. List of attached agents.')
    print('2. Send something to agent.')
    print('3. Quit.')
    print(67 * '-')

    while True:
        choice = int(input('Enter your choice: '))

        if choice == 1:
            display_tcp_clients()
        elif choice == 2:
            menu_helper.send_command()
        elif choice == 3:
            print('Bye!')
            print(threading.currentThread().getName())
            sys.exit(0)
        else:
            raw_input('Wrong option, enter again: ')


def display_tcp_clients():
    for i, conn in CONNECTIONS:
        print('{}: {}'.format(i, conn[0]))
