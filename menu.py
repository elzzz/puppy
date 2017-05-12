import sys
import threading
import network


def print_menu():
    print(30 * '-', 'MENU', 30 * '-')
    print('1. List of attached agents.')
    print('2. Send something to agent.')
    print('3. Quit.')
    print(67 * '-')

    while True:
        choice = int(input('Enter your choice: '))

        if choice == 1:
            network.display_tcp_clients()
        elif choice == 2:
            network.send_msg().send('Hey from server, my friend.\n')
        elif choice == 3:
            print('Bye!')
            print(threading.currentThread().getName())
            sys.exit(0)
        else:
            raw_input('Wrong option, enter again: ')
