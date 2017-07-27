import sys
import network

from PyQt4 import QtGui
from btn_classes.show_clients import btnShowClients
from btn_classes.send_cmd import btnSendCommand

sys.path.insert(0, '..')
sys.dont_write_bytecode = True

try:
    from lib.config import get_config
except:
    raise


def create_main_window():
    wnd = MainMenu()
    wnd.resize(get_config('../cfg/server.toml')['window']['height'],
               get_config('../cfg/server.toml')['window']['width'])
    wnd.setWindowTitle('MyLovelyServer')

    return wnd


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

        self.ButtonBox.setLayout(self.ButtonsLayout)
        self.mainLayout.addRow(self.ButtonBox)

        self.mainQWidget.setLayout(self.mainLayout)
        self.setCentralWidget(self.mainQWidget)

        self.btnSendCmd.clicked.connect(self.send_commands)

    def send_commands(self):
        network.execute_commands(self.btnShowClnt.get_selected_agents(),
                                 str(self.lineEdit.text()))
