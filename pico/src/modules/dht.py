import dht
import time
from enum import Enum

class SensorType(Enum):
    DHT11 = 1
    DHT22 = 2

class DHT:
    def __init__(self, pin=22, update_interval=1000, type=SensorType.DHT22):
        self._sensor = dht.DHT11(pin) if type == SensorType.DHT11 else dht.DHT22(pin)
        self._update_interval = update_interval
        self._last_time_meaure = -1

        print("Setup DHT11 complete")

    def loop(self):
        pass

    @property
    def temperature(self):
        self._measure()
        return self._sensor.temperature()

    @property
    def humidity(self):
        self._measure()
        return self._sensor.humidity()
    
    def _measure(self):
        if time.ticks_diff(time.ticks_ms(), self._last_time_meaure) > self._update_interval:
            self._sensor.measure()
            self._last_time_meaure = time.ticks_ms()