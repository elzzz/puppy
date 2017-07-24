from PyQt4.QtGui import *
from PyQt4.QtCore import QTimer, QString
from network import get_connections

connections_map = {}


class btnShowClients(QTableWidget):
    def __init__(self, parent=None):
        super(btnShowClients, self).__init__(parent)

        font = self.font()
        font.setPointSize(12)
        self.setFont(font)
        self.setColumnCount(1)
        self.get_agents()
        self.setHorizontalHeaderLabels(str(QString('Agent ip')))
        self.setSelectionMode(QAbstractItemView.MultiSelection)

    def get_agents(self):
        curr_agents = get_connections()

        self.setRowCount(len(curr_agents))

        i = 0
        for conn in curr_agents.items():
            self.setItem(i, 0, QTableWidgetItem(conn[0]))
            connections_map[i] = conn[1]
            i += 1

        QTimer.singleShot(300, self.get_agents)

    def get_selected_agents(self):
        items_list = self.selectedIndexes()
        agents_list = []
        for selected_item in items_list:
            agents_list.append(connections_map[selected_item.row()])
        return agents_list
