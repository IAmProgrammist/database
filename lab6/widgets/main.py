from PySide6.QtWidgets import QMainWindow

from lab6.repositories.repositories import all_repos
from lab6.widgets.main_ui import Ui_MainWindow
from lab6.widgets.repotab import RepoTab


class MainDialog(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.__tabs = []

        for repo_item in all_repos:
            tab_test = RepoTab(repo_item["repo"])
            self.__tabs.append(tab_test)
            self.ui.tabs.addTab(tab_test, repo_item["name"])

        self.ui.tabs.tabBarClicked.connect(self.__upadte_tab_on_select)

    def __upadte_tab_on_select(self, index):
        self.__tabs[index].refetch_table()
