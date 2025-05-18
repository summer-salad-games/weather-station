from src.configurations.config import WIFI_CONFIG
from src.modules.wifi import Wifi
from src.modules.led import Led
from src.modules.screen import Screen
from src.modules.ldr import Ldr

class MainController:

    def __init__(self):
        # self._wifi = Wifi(WIFI_CONFIG["ssid"], WIFI_CONFIG["password"])
        self._led = Led()
        self.screen = Screen()
        self._ldr = Ldr()
        print("Setup MainController complete")

    def loop(self):
        # self._wifi.loop()
        self._led.loop()
        self.screen.loop()
        self._ldr.loop()