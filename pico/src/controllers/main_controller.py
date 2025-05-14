from src.configurations.config import WIFI_CONFIG
from src.modules.wifi import Wifi
from src.modules.led import Led

class MainController:

    def __init__(self):
        self._wifi = Wifi(WIFI_CONFIG["ssid"], WIFI_CONFIG["password"])
        self._led = Led()

    def setup(self):
        print("Setup MainController")
        self._wifi.setup()
        self._led.setup()

    def loop(self):
        self._wifi.loop()
        self._led.loop()