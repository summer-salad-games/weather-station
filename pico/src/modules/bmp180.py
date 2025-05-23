import time
from lib.bmp085 import BMP180 as BMP180Sensor

class BMP180:
    def __init__(self, i2c, i2c_address=0x20, update_interval=1000, sea_level=1013.25):
        self._i2c_address = i2c_address
        self._sensor = BMP180Sensor(i2c)
        self._sensor.sealevel = sea_level
        self._update_interval = update_interval
        self._last_time_meaure = -1

        print("Setup BMP180 complete")

        pass

    def loop(self):
        pass

    @property
    def temperature(self):
        self._measure()
        return self._sensor.temperature

    @property
    def pressure(self):
        self._measure()
        return self._sensor.pressure

    @property
    def altitude(self):
        self._measure()
        return self._sensor.altitude

    def _measure(self):
        if time.ticks_diff(time.ticks_ms(), self._last_time_meaure) > self._update_interval:
            self._sensor.blocking_read()
            self._last_time_meaure = time.ticks_ms()
