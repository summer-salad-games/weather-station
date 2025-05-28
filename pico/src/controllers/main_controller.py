from src.configurations.config import WIFI_CONFIG
from src.modules.wifi import Wifi
from src.modules.led import Led
from src.modules.screen import Screen
from src.modules.ldr import LDR
from pico.src.modules.dht import DHT
from src.modules.bmp180 import BMP180
from src.modules.button import Button
import machine

class MainController:

    def __init__(self, scl_pin=5, sda_pin=4):
        self._i2c = machine.I2C(0, scl=machine.Pin(scl_pin), sda=machine.Pin(sda_pin), freq=400_000)
        self.screen = Screen(self._i2c)
        self._button = Button()
        self._wifi = Wifi(WIFI_CONFIG["ssid"], WIFI_CONFIG["password"])
        self._led = Led()
        self._ldr = LDR()
        self._dht11 = DHT()
        self._bmp180 = BMP180(self._i2c, sea_level=1016.5)

        print("Setup MainController complete")

    def loop(self):
        self.screen.loop()
        self._button.loop()
        self._wifi.loop()
        self._led.loop()
        self._ldr.loop()
        self._dht11.loop()
        self._bmp180.loop()