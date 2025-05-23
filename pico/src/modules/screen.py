import machine
from lib.sh1106 import SH1106_I2C

class Screen:
    def __init__(self, i2c, width=128, height=64, i2c_address=0x3c):
        self._width = width
        self._height = height
        self._i2c_address = i2c_address
        self._display = SH1106_I2C(width, height, i2c, rotate=180, addr=i2c_address)
        self._display.init_display()
        self._display.poweroff()

        print("Setup Screen complete")

    def loop(self):
        pass   