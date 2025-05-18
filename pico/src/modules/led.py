import machine

class Led:
    def __init__(self, pin="LED"):
        self._pin = pin
        self._led = machine.Pin(self._pin, machine.Pin.OUT)
        self._timer = machine.Timer() # type: ignore
        
        self._timer.init(period=1000, mode=machine.Timer.PERIODIC, callback=self._toggle_led)
        print("Setup LED complete")

    def loop(self):
        pass

    def _toggle_led(self, timer):
        self._led.toggle()