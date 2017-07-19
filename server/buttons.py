from PyQt4 import QtGui, QtCore
import menu
import network


class buttons(QtGui.QWidget):
    def __init__(self):
        super(buttons, self).__init__()
        self.textbox = QtGui.QLineEdit()
        self.msg = QtGui.QMessageBox()
        self.lst = menu.display_tcp_clients(network.get_enum_connections())
        self.hbox = QtGui.QHBoxLayout()
        self.vbox = QtGui.QVBoxLayout()
        self.vbox.addLayout(self.hbox)
        self.setLayout(self.vbox)

        quit = QtGui.QPushButton('Quit')
        self.connect(quit, QtCore.SIGNAL('clicked()'), QtGui.qApp,
                     QtCore.SLOT('quit()'))

        btn1 = QtGui.QPushButton('Show list')
        btn1.clicked.connect(self.show_messagebox)

        btn2 = QtGui.QPushButton('Send something to agent')
        btn2.clicked.connect(self.show_textbox)

        self.hbox.addStretch(1)
        self.hbox.addWidget(quit)

        self.vbox.addWidget(btn1)
        self.vbox.addWidget(btn2)
        self.vbox.addStretch(1)

    def show_messagebox(self):
        self.msg.exec_()

    def show_textbox(self):
        self.vbox.addWidget(self.textbox)
        print(self.lst)
