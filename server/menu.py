from PyQt4 import QtGui
import sys
import os
import curses

import qt
import cons
import nc
import nc_menu

sys.dont_write_bytecode = True


def start_gui(gui_type):
    if gui_type == 'qt':
        start_qt()
    elif gui_type == 'nc':
        start_ncurses()
    else:
        start_menu()


def start_qt():
    app = QtGui.QApplication(sys.argv)
    main_menu = qt.create_main_window()
    main_menu.show()
    app.exec_()


def start_menu():
    cons.run_console_menu()


def start_ncurses():
    nc.show_menu(nc_menu.menu_data)
    curses.endwin()
    os.system('clear')
