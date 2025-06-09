import time
from lib.uSGP30 import SGP30

class Gaz:
    def __init__(self, i2c, update_interval=1000):
        self._sensor = SGP30(i2c)
        self._co2eq = None
        self._tvoc = None
        self._update_interval = update_interval
        self._last_time_measure = -1

        print("Setup SGP30 complete")

    def loop(self):
        pass

    @property
    def co2eq(self):
        self._measure()
        return self._co2eq

    @property
    def tvoc(self):
        self._measure()
        return self._tvoc

    def _measure(self):
        if time.ticks_diff(time.ticks_ms(), self._last_time_measure) > self._update_interval:
            result = self._sensor.measure_iaq()
            if result is not None:
                self._co2eq, self._tvoc = result
            else:
                self._co2eq = None
                self._tvoc = None
            self._last_time_measure = time.ticks_ms()
