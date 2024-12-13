import PySide6.QtCore
import PySide6.QtWidgets
from PySide6.QtWidgets import QWidget, QTableWidgetItem, QDialog

from repositories.base import Repository
from widgets.accept_reject import AcceptRejectDialog
from widgets.form_dialog import FormDialog
from widgets.repotab_ui import Ui_Form


class RepoTab(QWidget):
    def __init__(self, repository: Repository, parent=None) -> None:
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.__repository = repository
        self.__values = []

        # Прячем вставку, если DTO вставки пустой
        if self.__repository.generator.insert() is None:
            self.ui.pushButton.setVisible(False)

        # Прячем обновление, если нечего обновляьт или нельзя идентифицировать запись
        if self.__repository.generator.identifier() is None or self.__repository.generator.update() is None:
            self.ui.pushButton_2.setVisible(False)

        # Прячем удаление, если нельзя идентифицировать запись
        if self.__repository.generator.identifier() is None:
            self.ui.pushButton_3.setVisible(False)

        self.ui.pushButton_3.clicked.connect(self.__delete_clicked)
        self.ui.pushButton_2.clicked.connect(self.__update_clicked)
        self.ui.pushButton.clicked.connect(self.__create_clicked)
        self.refetch_table()

    def refetch_table(self):
        self.__values = self.__repository.select()
        self.__redraw_table()

    def __redraw_table(self):
        translations = self.__repository.generator.translations()
        select_keys = list(self.__repository.generator.select().model_fields.keys())
        self.ui.tableWidget.setColumnCount(len(select_keys))
        self.ui.tableWidget.setRowCount(len(self.__values))
        self.ui.tableWidget.setHorizontalHeaderLabels(list(map(lambda x: translations[x], select_keys)))

        i = 0
        for value in self.__values:
            j = 0
            show_model = value.model_dump()
            for key in select_keys:
                self.ui.tableWidget.setItem(i, j, QTableWidgetItem("Пусто" if show_model[key] is None else str(show_model[key])))

                j += 1

            i += 1

        self.ui.tableWidget.resizeColumnsToContents()

    def __create_clicked_callback(self, parent_dialog, data):
        try:
            self.__repository.insert(data)
            self.refetch_table()
            return True
        except Exception as e:
            whoops = AcceptRejectDialog(parent=parent_dialog,
                                        title="Произошла ошибка",
                                        text=repr(e))
            whoops.show()
            return False

    def __create_clicked(self):
        form_dialog = FormDialog("Создать",
                                 list(self.__repository.generator.insert().model_fields.keys()),
                                 self.__repository.generator.translations(),
                                 self,
                                 self.__create_clicked_callback)
        form_dialog.exec()

    def __delete_clicked(self):
        should_delete = AcceptRejectDialog(parent=self,
                                           title="Удалить?",
                                           text=f"Вы собираетесь удалить записи ({len(self.ui.tableWidget.selectionModel().selectedRows())})")
        if should_delete.exec() == 1:
            for row_index in self.ui.tableWidget.selectionModel().selectedRows():
                select_keys = self.__repository.generator.select().model_fields.keys()
                selected_value: dict = {}

                for key, val in self.__values[row_index.row()].__dict__.items():
                    if key in select_keys:
                        selected_value[key] = val

                selected_value_identififer_keys = list(self.__repository.generator.identifier().model_fields.keys())
                selected_value_identififer: dict = {}

                select_keys = list(self.__repository.generator.select().model_fields.keys())
                for key_index in range(0, len(select_keys)):
                    if select_keys[key_index] in selected_value_identififer_keys:
                        selected_value_identififer[select_keys[key_index]] = selected_value[select_keys[key_index]]
                try:
                    self.__repository.delete(selected_value_identififer)
                except Exception as e:
                    whoops = AcceptRejectDialog(parent=self,
                                                title="Произошла ошибка",
                                                text=repr(e))
                    whoops.show()

            self.refetch_table()

    def __update_clicked_callback(self, parent_dialog, data):
        row_index = self.ui.tableWidget.selectionModel().selectedRows()[0]
        select_keys = self.__repository.generator.select().model_fields.keys()
        selected_value: dict = {}

        for key, val in self.__values[row_index.row()].__dict__.items():
            if key in select_keys:
                selected_value[key] = val

        selected_value_identififer_keys = list(self.__repository.generator.identifier().model_fields.keys())
        selected_value_identififer: dict = {}

        select_keys = list(self.__repository.generator.select().model_fields.keys())
        for key_index in range(0, len(select_keys)):
            if select_keys[key_index] in selected_value_identififer_keys:
                selected_value_identififer[select_keys[key_index]] = selected_value[select_keys[key_index]]

        try:
            self.__repository.update(data, selected_value_identififer)
            self.refetch_table()
            return True
        except Exception as e:
            whoops = AcceptRejectDialog(parent=parent_dialog,
                                        title="Произошла ошибка",
                                        text=repr(e))
            whoops.show()
            return False

    def __update_clicked(self):
        if len(self.ui.tableWidget.selectionModel().selectedRows()) == 0:
            no_update = AcceptRejectDialog(parent=self,
                                           title="Нечего обновлять",
                                           text=f"Выберите один ряд для обновления")
            no_update.exec()
            return

        row_index = self.ui.tableWidget.selectionModel().selectedRows()[0]
        select_keys = self.__repository.generator.select().model_fields.keys()
        selected_value: dict = {}

        for key, val in self.__values[row_index.row()].__dict__.items():
            if key in select_keys:
                selected_value[key] = val

        selected_value_identififer_keys = list(self.__repository.generator.identifier().model_fields.keys())
        selected_value_identififer: dict = {}

        select_keys = list(self.__repository.generator.select().model_fields.keys())
        for key_index in range(0, len(select_keys)):
            if select_keys[key_index] in selected_value_identififer_keys:
                selected_value_identififer[select_keys[key_index]] = selected_value[select_keys[key_index]]

        form_dialog = FormDialog("Обновить",
                                 list(self.__repository.generator.update().model_fields.keys()),
                                 self.__repository.generator.translations(),
                                 self,
                                 self.__update_clicked_callback,
                                 selected_value)
        form_dialog.exec()
