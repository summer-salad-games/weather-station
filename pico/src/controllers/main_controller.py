from src.configurations.config import WIFI_CONFIG
from src.modules.wifi import Wifi
from src.modules.led import Led
from src.modules.screen import Screen
from src.modules.humidity import Humidity
from src.modules.pressure import Pressure
from src.modules.button import Button
from src.modules.gaz import Gaz
import machine, time

class MainController:

    def __init__(self, scl_pin=5, sda_pin=4, init_period=15):
        self._i2c = machine.I2C(0, scl=machine.Pin(scl_pin), sda=machine.Pin(sda_pin), freq=400_000)
        print(f"I2C components {self._i2c.scan()}")

        self._screen = Screen(self._i2c)
        self._button = Button()
        self._wifi = Wifi(WIFI_CONFIG["ssid"], WIFI_CONFIG["password"])
        self._led = Led()
        self._humidity = Humidity()
        self._pressure = Pressure(self._i2c, sea_level=1016.5)
        self._gaz = Gaz(self._i2c)

        self._last_time_meaure = -1
        self._update_interval = 5000
        print("Setup MainController complete")

    def loop(self):
        self._screen.loop()
        self._button.loop()
        self._wifi.loop()
        self._led.loop()
        self._humidity.loop()
        self._pressure.loop()
        self._gaz.loop()

        if time.ticks_diff(time.ticks_ms(), self._last_time_meaure) > self._update_interval:
            print("--------------------------------- RAW DATA ---------------------------------")
            print(f"DHT22 (Temperature {self._humidity.temperature}, Humidity: {self._humidity.humidity})")
            print(f"BMP180 (Pressure {self._pressure.pressure}, Temperature: {self._pressure.temperature}, Altitude: {self._pressure.altitude})")
            print(f"SGP30 (Co2 Eq {self._gaz.co2eq}, TVOC: {self._gaz.tvoc})")
            ## print(f"LDR (Light {self._light.measurement})")
            print("----------------------------------------------------------------------------")
            self._last_time_meaure = time.ticks_ms()


