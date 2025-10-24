import sys

from PyQt6.QtWidgets import QApplication
from src.gui.main_window import MainWindow
from src.gui.resources.paths import FilePath

if __name__ == "__main__":


    app = QApplication(sys.argv)

    with open(FilePath.STYLESHEET, 'r') as file:
        stylesheet = file.read()
        app.setStyleSheet(stylesheet)

    window = MainWindow()
    window.show()
    sys.exit(app.exec())

