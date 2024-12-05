import datetime

from PySide6.QtWidgets import QDialog, QGroupBox, QVBoxLayout, QDialogButtonBox, QLineEdit, QFormLayout, QLabel


class FormDialog(QDialog):

    # constructor
    def __init__(self, title, values, translations, parent, default_values=None):
        super(FormDialog, self).__init__(parent=parent)
        self.setWindowTitle(title)
        self.setGeometry(100, 100, 300, 400)
        self.formGroupBox = QGroupBox(title)
        self.formValues = []
        self._values = values
        self._translations = translations
        self._default_values = default_values
        for value in translations:
            self.formValues.append(QLineEdit())
        self.createForm()
        self.buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)
        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.formGroupBox)
        mainLayout.addWidget(self.buttonBox)
        self.setLayout(mainLayout)

    def getInfo(self):
        answer = {}

        for i in range(0, len(self._values)):
            # Это просто ужасно, мы отнимаем у юзера возможность ввести None...
            answer[self._values[i]] = None if self.formValues[i].text() == "None" else self.formValues[i].text()

        return answer

    def createForm(self):
        layout = QFormLayout()

        for i in range(0, len(self._values)):
            layout.addRow(QLabel(self._translations[self._values[i]]), self.formValues[i])

            if self._default_values and self._values[i] in self._default_values:
                if type(self._default_values[self._values[i]]) is None:
                    self.formValues[i].setText("None")
                elif type(self._default_values[self._values[i]]) is datetime.date:
                    self.formValues[i].setText(self._default_values[self._values[i]].isoformat())
                else:
                    self.formValues[i].setText(str(self._default_values[self._values[i]]))

        self.formGroupBox.setLayout(layout)
