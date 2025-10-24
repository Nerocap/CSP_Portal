import os

BASE_DIR = os.path.dirname(__file__)  # path zu resources/



class ImgPath:
    ICON_DIR = os.path.join(BASE_DIR, "icons")

    CONNECT_DEVICES_ON_ICON = os.path.join(ICON_DIR, "connect_on_id1.png")
    CONNECT_DEVICES_OFF_ICON = os.path.join(ICON_DIR, "connect_off_id1.png")
    SETTINGS_DISABLE = os.path.join(ICON_DIR, "list_disable_id1.png")
    SETTINGS_ENABLE = os.path.join(ICON_DIR, "list_enable_id1.png")
    SETTINGS_ON = os.path.join(ICON_DIR, "list_on_id1.png")

    STOP_ICON = os.path.join(ICON_DIR, "stop.png")
    HOME_ICON = os.path.join(ICON_DIR, "home.png")
    IMAGE_WINDOW_ICON = os.path.join(ICON_DIR, "csp_logo_1.png")

class FilePath:
    STYLESHEET = os.path.join(BASE_DIR, "styles/styles.qss")
