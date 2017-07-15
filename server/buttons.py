from PyQt4 import QtGui


def quit_button(self):
    btn = QtGui.QPushButton('Quit', self)
    btn.clicked.connect(self.close_application)
    btn.resize(btn.minimumSizeHint())
    btn.move(440, 275)
    self.show()


def show_clients(self):
    btn = QtGui.QPushButton('Show connections', self)
    # btn.clicked.connect(display_tcp_clients(get_enum_connections()))
    btn.resize(50, 50)
    btn.move(50, 50)
    self.show()


class MessageBox(QtGui.QCheckBox):
    def __init__(self):
        super(MessageBox, self).__init__()
        self.move(20, 20)
