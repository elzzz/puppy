from PyQt4 import QtGui
import buttons
import sys
import threading
import network
import menu_helper
sys.dont_write_bytecode = True


class MainMenu(QtGui.QMainWindow):

    def __init__(self):
        super(MainMenu, self).__init__()
        self.resize(500, 300)
        self.setWindowTitle('MyLovelyServer')
        self.btn = buttons.buttons()
        self.setCentralWidget(self.btn)


def start_gui():
    app = QtGui.QApplication(sys.argv)
    main_menu = MainMenu()
    main_menu.show()
    sys.exit(app.exec_())


def print_menu():
    print(30 * '-', 'MENU', 30 * '-')
    print('1. List of attached agents.')
    print('2. Send something to agent.')
    print('3. Quit.')
    print(67 * '-')

    while True:
        choice = int(input('Enter your choice: '))

        if choice == 1:
            display_tcp_clients(network.get_enum_connections())
        elif choice == 2:
            menu_helper.send_command()
        elif choice == 3:
            print('Bye!')
            print(threading.currentThread().getName())
            sys.exit(0)
        else:
            raw_input('Wrong option, enter again: ')


def display_tcp_clients(enum_dict):

    for i, conn in enum_dict.iteritems():
        print('{}: {}'.format(i, conn.keys()[0]))
