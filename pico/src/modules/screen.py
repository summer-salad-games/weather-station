import machine
from lib.sh1106 import SH1106_I2C

class Screen:
    def __init__(self, width=128, height=64, scl_pin=5, sda_pin=4, i2c_address=0x3c):
        self._width = width
        self._height = height
        self._scl_pin = scl_pin
        self._sda_pin = sda_pin
        self._i2c_address = i2c_address
        self._i2c = machine.I2C(0, scl=machine.Pin(self._scl_pin), sda=machine.Pin(self._sda_pin), freq=400_000)
        self._display = SH1106_I2C(width, height, self._i2c, rotate=180, addr=i2c_address)

        self._display.init_display()
        self._display.poweroff()

        print("Setup Screen complete")

    def loop(self):
        pass   