from PySide6.QtWidgets import QDialog, QGroupBox, QVBoxLayout, QDialogButtonBox, QLineEdit, QFormLayout, QLabel


class AcceptRejectDialog(QDialog):

    # constructor
    def __init__(self, title, text, parent=None):
        super(AcceptRejectDialog, self).__init__(parent=parent)

        # setting window title
        self.setWindowTitle(title)

        # setting geometry to the window
        self.setGeometry(100, 100, 300, 200)

        # creating a dialog button for ok and cancel
        self.buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)

        # adding action when form is accepted
        self.buttonBox.accepted.connect(self.accept)

        # adding action when form is rejected
        self.buttonBox.rejected.connect(self.reject)

        # creating a vertical layout
        mainLayout = QVBoxLayout()

        mainLayout.addWidget(QLabel(text))

        # adding button box to the layout
        mainLayout.addWidget(self.buttonBox)

        # setting lay out
        self.setLayout(mainLayout)
