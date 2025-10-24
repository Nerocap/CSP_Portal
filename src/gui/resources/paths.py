import os

BASE_DIR = os.path.dirname(__file__)  # path zu resources/



class ImgPath:
    ICON_DIR = os.path.join(BASE_DIR, "icons")

    ENABLE_DEVICES = os.path.join(ICON_DIR, 'connect_on.png')
    DISABLE_DEVICES = os.path.join(ICON_DIR, 'connect_off.png')

    CONNECT_MFI_DEVICE_ON = os.path.join(ICON_DIR, "mfi_on.png")
    CONNECT_MFI_DEVICE_OFF = os.path.join(ICON_DIR, "mfi_off.png")

    SETTINGS_OFF = os.path.join(ICON_DIR, "setting_off.png")
    SETTINGS_ON = os.path.join(ICON_DIR, "setting_on.png")

    STOP_ICON = os.path.join(ICON_DIR, "stop.png")
    HOME_ICON = os.path.join(ICON_DIR, "home.png")
    IMAGE_WINDOW_ICON = os.path.join(ICON_DIR, "csp_logo_1.png")

class FilePath:
    STYLESHEET = os.path.join(BASE_DIR, "styles/styles.qss")
