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
        self.setGeometry(10, 10, 500, 300)
        self.setWindowTitle('MyLovelyServer')
        self.display_buttons()

    def display_buttons(self):
        # btn_clients = buttons.show_clients()
        # btn_quit = buttons.quit_button()
        btn_msg = buttons.MessageBox()
        btn_msg.show()

    def close_application(self):
        choice = QtGui.QMessageBox.question(self, 'Quit', 'Are you sure?',
                                            QtGui.QMessageBox.Yes |
                                            QtGui.QMessageBox.No)
        if choice == QtGui.QMessageBox.Yes:
            sys.exit()
        else:
            pass


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
