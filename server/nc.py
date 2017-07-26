import curses
import os
import time

from network import get_connections

screen = curses.initscr()
curses.curs_set(0)
curses.noecho()
curses.cbreak()
curses.start_color()
screen.keypad(1)

curses.init_pair(1, curses.COLOR_RED, curses.COLOR_WHITE)
h = curses.color_pair(1)
n = curses.A_NORMAL

MENU = "menu"
COMMAND = "command"
EXITMENU = "exitmenu"
PRINT = 'print'


def runmenu(menu, parent):

    if parent is None:
        lastoption = "Exit"
    else:
        lastoption = 'Return to {} menu'.format(parent['title'])

    options_count = len(menu['options'])

    pos = 0
    oldpos = None
    x = None

    while x != ord('\n'):
        if pos != oldpos:
            oldpos = pos
            screen.border(0)
            screen.addstr(2, 2, menu['title'], curses.A_STANDOUT)
            screen.addstr(4, 2, menu['subtitle'], curses.A_BOLD)

        for index in range(options_count):
            textstyle = n
            if pos == index:
                textstyle = h
            screen.addstr(5+index, 4,
                          "{}. {}".format(index+1,
                                          menu['options'][index]['title']),
                          textstyle)
            textstyle = n
            if pos == options_count:
                textstyle = h
            screen.addstr(5+options_count, 4,
                          "{}. {}".format(options_count+1, lastoption),
                          textstyle)
            screen.refresh()

        x = screen.getch()

        if x >= ord('1') and x <= ord(str(options_count+1)):
            pos = x - ord('0') - 1
        elif x == 258:
            if pos < options_count:
                pos += 1
            else:
                pos = 0
        elif x == 259:
            if pos > 0:
                pos += -1
            else:
                pos = options_count

    return pos


def processmenu(menu, parent=None):
    options_count = len(menu['options'])
    exitmenu = False
    while not exitmenu:
        getin = runmenu(menu, parent)
        if getin == options_count:
            exitmenu = True
        elif menu['options'][getin]['type'] == COMMAND:
            curses.def_prog_mode()
            os.system('reset')
            screen.clear()
            os.system(menu['options'][getin]['command'])
            time.sleep(3)
            screen.clear()
            curses.reset_prog_mode()
            curses.curs_set(1)
            curses.curs_set(0)
        elif menu['options'][getin]['type'] == MENU:
            screen.clear()
            processmenu(menu['options'][getin], menu)
            screen.clear()
        elif menu['options'][getin]['type'] == EXITMENU:
            exitmenu = True
        elif menu['options'][getin]['type'] == PRINT:
            get_agents()


def get_agents():
    curr_agents = get_connections()

    i = 6
    j = 1
    for conn in curr_agents.items():
        screen.addstr(i, 4, '{}. {}'.format(j+1, conn[0]), curses.A_NORMAL)
        screen.refresh()
        i += 1
