import sys

from PySide6.QtWidgets import QApplication

from lab6.widgets.main import MainDialog

if __name__ == "__main__":
    app = QApplication(sys.argv)
    dialog = MainDialog()
    dialog.show()
    sys.exit(app.exec())
