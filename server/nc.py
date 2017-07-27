import curses
import os
import time

from network import get_connections

connections_map = {}


def runmenu(menu, parent):

    screen = curses.initscr()
    curses.curs_set(0)
    curses.noecho()
    curses.cbreak()
    curses.start_color()
    screen.keypad(1)
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_WHITE)

    if parent is None:
        lastoption = 'Exit'
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
            textstyle = curses.A_NORMAL
            if pos == index:
                textstyle = curses.color_pair(1)
            screen.addstr(5+index, 4,
                          '{}. {}'.format(index+1,
                                          menu['options'][index]['title']),
                          textstyle)
            textstyle = curses.A_NORMAL
            if pos == options_count:
                textstyle = curses.color_pair(1)
            screen.addstr(5+options_count, 4,
                          '{}. {}'.format(options_count+1, lastoption),
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


def show_menu(menu, parent=None):

    options_count = len(menu['options'])
    screen = curses.initscr()
    exitmenu = False

    while not exitmenu:

        getin = runmenu(menu, parent)

        if getin == options_count:
            exitmenu = True
        elif menu['options'][getin]['type'] == 'command':
            curses.def_prog_mode()
            os.system('reset')
            screen.clear()
            choice = input_data(screen, 0, 0, 'Type your command to send:')
            screen.addstr(0, 27, choice)
            connections_map[getin].send(choice)
            screen.refresh()
            time.sleep(2)
            screen.clear()
            curses.reset_prog_mode()
            curses.curs_set(1)
            curses.curs_set(0)
        elif menu['options'][getin]['type'] == 'menu':
            screen.clear()
            get_agents(menu)
            show_menu(menu['options'][getin], menu)
            screen.clear()
        elif menu['options'][getin]['type'] == 'exitmenu':
            exitmenu = True


def input_data(screen, raw, column, promt_string):

    curses.noecho()
    screen.addstr(raw, column, promt_string)
    screen.refresh()
    data = screen.getstr(raw + 1, column, 20)
    return data


def get_agents(menu):

    i = 0
    curr_agents = get_connections()

    for conn in curr_agents.items():
        agnt_print = {'title': conn[0], 'type': 'print'}
        agnt_cmd = {'title': conn[0], 'type': 'command'}
        connections_map[i] = conn[1]
        i += 1
        if menu['options'][0]['options'].count(dict(agnt_print)) == 0:
            menu['options'][0]['options'].insert(0, dict(agnt_print))
        if menu['options'][1]['options'].count(dict(agnt_cmd)) == 0:
            menu['options'][1]['options'].insert(0, dict(agnt_cmd))
