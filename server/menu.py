from PyQt4 import QtGui
import sys

import qt
from nc import run_ncurses

sys.dont_write_bytecode = True


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
    run_ncurses()
