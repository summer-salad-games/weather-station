import machine, time
from lib.bmp085 import BMP180 as BMP180Sensor

class BMP180:
    def __init__(self, scl_pin=5, sda_pin=4, i2c_address=0x20, update_interval=1000):
        self._scl_pin = scl_pin
        self._sda_pin = sda_pin
        self._i2c_address = i2c_address
        self._i2c = machine.I2C(0, scl=machine.Pin(self._scl_pin), sda=machine.Pin(self._sda_pin), freq=400_000)
        self._sensor = BMP180Sensor(self._i2c)
        self._update_interval = update_interval
        self._last_time_meaure = -1

        print("Setup BMP180 complete")

        pass

    def loop(self):
        pass

    def temperature(self):
        self._measure()
        self._sensor.temperature

    def pressure(self):
        self._measure()
        self._sensor.pressure

    def altitude(self):
        self._measure()
        self._sensor.altitude

    def _measure(self):
        if time.ticks_diff(time.ticks_ms(), self._last_time_meaure) > self._update_interval:
            self._sensor.blocking_read()
            self._last_time_meaure = time.ticks_ms()