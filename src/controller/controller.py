from PyQt6.QtWidgets import QMainWindow

from src.hardware.mfi_device import MfiDevice
from src.hardware.xps_device import XpsDevice


class MfiController:
    def __init__(self, device_url: str):

        self.sensor: MfiDevice
        self.sensor = MfiDevice(device_url)
        #self.url_task = 'http://localhost:8090/tasks'

    @property
    def device_status(self):
        return self.sensor.get_status()

class XpsController:
    def __init__(self):
        self.linear_unit: XpsDevice
        self.linear_unit = XpsDevice()

    @property
    def device_status(self):
        return True

