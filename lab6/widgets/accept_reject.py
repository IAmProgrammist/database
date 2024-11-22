from PySide6.QtWidgets import QDialog, QGroupBox, QVBoxLayout, QDialogButtonBox, QLineEdit, QFormLayout, QLabel


class AcceptRejectDialog(QDialog):

    # constructor
    def __init__(self, title, text, parent=None):
        super(AcceptRejectDialog, self).__init__(parent=parent)
        self.setWindowTitle(title)
        self.setGeometry(100, 100, 300, 200)
        self.buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)
        mainLayout = QVBoxLayout()
        mainLayout.addWidget(QLabel(text))
        mainLayout.addWidget(self.buttonBox)
        self.setLayout(mainLayout)
