import dht
import time

class DHT11:
    def __init__(self, pin=22, update_interval=1000):
        self._sensor = dht.DHT11(pin)
        self._update_interval = update_interval
        self._last_time_meaure = -1

        print("Setup DHT11 complete")

    def loop(self):
        pass

    def temperature(self):
        self._measure()
        return self._sensor.temperature()

    def humidity(self):
        self._measure()
        return self._sensor.humidity()
    
    def _measure(self):
        if time.ticks_diff(time.ticks_ms(), self._last_time_meaure) > self._update_interval:
            self._sensor.measure()
            self._last_time_meaure = time.ticks_ms()