from machine import Pin
import time

# TODO Synchronize _ready state

class Button:

    def __init__(self, pin=8, debounce=250):
        self._pin = pin
        self._debounce = debounce
        self._callback = None
        self._button_pin = Pin(pin, Pin.IN, Pin.PULL_UP)
        self._ready = True
        self._last_check = -1

        self._button_pin.irq(trigger=Pin.IRQ_RISING, handler=self._update_ready)
        self._button_pin.irq(trigger=Pin.IRQ_FALLING, handler=self._debounce_handler)

        print("Setup Buttton complete")

    @property
    def is_pressed(self):
        if not self._ready:
            return False

        if self._button_pin.value() == 0 and time.ticks_diff(time.ticks_ms(), self._last_check) >= self._debounce:
            self._last_check = time.ticks_ms()
            self._ready = False
            return True

        return False

    def _debounce_handler(self, pin):
        current_time = time.ticks_ms()
        if time.ticks_diff(current_time, self._last_check) >= self._debounce:
            self._last_check = current_time
            self._ready = False
            if self._callback:
                self._callback()

    def on_press(self, callback):
        self._callback = callback

    def _update_ready(self, pin):
        self._ready = True
