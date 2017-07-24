from PyQt4 import QtGui
import sys
sys.dont_write_bytecode = True


class btnSendCommand(QtGui.QPushButton):
    def __init__(self, parent=None):
        super(btnSendCommand, self).__init__('Send Commands', parent)

        font = self.font()
        font.setPointSize(12)
        self.setFont(font)
        self.setWindowTitle('Commands')
