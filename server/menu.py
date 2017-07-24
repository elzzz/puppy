from PyQt4 import QtGui
import sys
import threading
import network
import menu_helper
import qt

from btn_classes.show_clients import btnShowClients
from btn_classes.send_cmd import btnSendCommand

sys.dont_write_bytecode = True


class MainMenu(QtGui.QMainWindow):

    def __init__(self):
        super(MainMenu, self).__init__()
        self.mainQWidget = QtGui.QWidget()
        self.mainLayout = QtGui.QFormLayout()
        self.mainLayout.setFieldGrowthPolicy(
            QtGui.QFormLayout.AllNonFixedFieldsGrow)

        self.label = QtGui.QLabel('Command: ')
        self.lineEdit = QtGui.QLineEdit()
        self.mainLayout.addRow(self.label, self.lineEdit)

        self.ButtonBox = QtGui.QGroupBox()
        self.ButtonsLayout = QtGui.QHBoxLayout()

        self.btnShowClnt = btnShowClients()
        self.btnSendCmd = btnSendCommand()

        self.ButtonsLayout.addWidget(self.btnShowClnt)
        self.ButtonsLayout.addWidget(self.btnSendCmd)
        # self.ButtonsLayout.addWidget(self.Button_03)
        # self.ButtonsLayout.addWidget(self.Button_04)

        self.ButtonBox.setLayout(self.ButtonsLayout)
        self.mainLayout.addRow(self.ButtonBox)

        self.mainQWidget.setLayout(self.mainLayout)
        self.setCentralWidget(self.mainQWidget)

        self.btnSendCmd.clicked.connect(self.send_commands)

    def send_commands(self):
        network.execute_commands(self.btnShowClnt.get_selected_agents(),
                                 str(self.lineEdit.text()))


def start_gui(gui_type):
    if gui_type == 'qt':
        start_qt()
    else:
        start_ncurses()


def start_qt():
    app = QtGui.QApplication(sys.argv)
    main_menu = qt.create_main_window()
    main_menu.show()
    app.exec_()


def start_ncurses():
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
