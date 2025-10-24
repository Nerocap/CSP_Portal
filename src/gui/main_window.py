from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui import QAction, QIcon
from PyQt6.QtWidgets import QMainWindow, QApplication, QToolBar, QStatusBar, QToolButton, QPushButton, QWidget, \
    QHBoxLayout, QVBoxLayout, QGroupBox, QLabel
from src import __version__
from src.controller.controller import MfiController, XpsController
from src.gui.resources.paths import ImgPath, FilePath
from PyQt6.QtCore import QFile, QTextStream
import sys
import requests


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # set class variable
        self.statusBar = None
        self.xps_controller = None
        self.mfi_controller = None
        self.btn_id2 = None
        self.btn_id1 = None

        # set window design
        self.setWindowTitle(f"portal version {__version__}")
        self.setGeometry(640, 320, 800, 600)
        self.setWindowIcon(QIcon(ImgPath.IMAGE_WINDOW_ICON))

        self.main_widget = QWidget(self)
        self.setCentralWidget(self.main_widget)
        self.main_widget.setLayout(QHBoxLayout())

        self.left_area = QWidget(self)
        self.left_area.setObjectName("left_area")

        self.right_area = QWidget(self)
        self.right_area.setObjectName("right_area")
        self.right_area.setLayout(QVBoxLayout())

        self.information = QGroupBox('information')
        self.information.setObjectName("information")
        self.information.setLayout(QVBoxLayout())

        self.right_area.layout().addWidget(self.information)
        self.right_area.layout().addStretch()



        self.main_widget.layout().addWidget(self.left_area)
        self.main_widget.layout().addWidget(self.right_area)

        # load class method
        self.load_controllers()
        self.create_toolbar()
        self.create_status_bar()






    def on_check_status(self) -> None:
        """
        check whether the device is connected or not
        """

        if self.btn_id1.isChecked():
            status_mfi = self.mfi_controller.device_status
            status_xps = self.xps_controller.device_status
            self.btn_id1.setIcon(QIcon(ImgPath.CONNECT_DEVICES_ON_ICON))
            self.btn_id2.setIcon(QIcon(ImgPath.SETTINGS_ENABLE))
            self.btn_id2.setEnabled(True)

            self.information.layout().addWidget(QLabel(f'Name: {status_mfi.json()[0]['name']}'))
            self.information.layout().addWidget(QLabel(f'Serial ID: {status_mfi.json()[0]['serial_id']}'))
            self.information.layout().addWidget(QLabel(f'Sensor type: {status_mfi.json()[0]['sensor_type']}'))

            if status_mfi.status_code == 200:
                self.statusBar.showMessage(f'Device MFI online')
            else:
                self.statusBar.showMessage(f'Device MFI offline')

        elif not self.btn_id1.isChecked():
            self.statusBar.showMessage(f'Device offline')
            self.btn_id1.setIcon(QIcon(ImgPath.CONNECT_DEVICES_OFF_ICON))
            self.btn_id2.setIcon(QIcon(ImgPath.SETTINGS_DISABLE))
            self.btn_id2.setEnabled(False)

    def open_settings(self):

        if self.btn_id2.isChecked():
            self.btn_id2.setIcon(QIcon(ImgPath.SETTINGS_ON))
        elif not self.btn_id2.isChecked():
            self.btn_id2.setIcon(QIcon(ImgPath.SETTINGS_ENABLE))

    def create_toolbar(self):
        # add toolbar
        toolbar: QToolBar = QToolBar('navigation')
        self.addToolBar(toolbar)

        # create toolbar-buttons
        self.btn_id1: ToolBarButton = ToolBarButton('btn_id1', ImgPath.CONNECT_DEVICES_OFF_ICON, self.on_check_status)
        self.btn_id2: ToolBarButton = ToolBarButton('btn_id2', ImgPath.SETTINGS_ENABLE, self.open_settings)

        self.btn_id1.setEnabled(True)

        # add buttons in toolbar
        toolbar.addWidget(self.btn_id1)
        toolbar.addSeparator()
        toolbar.addWidget(self.btn_id2)

        # set toolbar design

    def load_controllers(self):
        self.mfi_controller = MfiController('http://localhost:8090/')
        self.xps_controller = XpsController()

    def create_status_bar(self):
        # add statusbar
        status_bar: QStatusBar = QStatusBar(self)
        self.statusBar = status_bar
        self.setStatusBar(status_bar)


class ToolBarButton(QPushButton):
    def __init__(self,obj_name = None, icon_file = None, callback = None):
        super().__init__()
        self.setObjectName(obj_name)

        self.setIcon(QIcon(icon_file))
        self.setIconSize(QSize(62, 62))
        self.setFixedSize(QSize(64, 64))

        self.setCheckable(True)
        self.setChecked(False)
        self.setEnabled(False)

        self.clicked.connect(callback)










