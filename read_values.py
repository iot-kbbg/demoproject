import machine
import time
from machine import I2C
bus = I2C(1, scl = machine.Pin(22), sda = machine.Pin(21))
from bmp280 import *
bmp = BMP280(bus)
while (True):
    print(bmp.temperature)
    time.sleep (30)