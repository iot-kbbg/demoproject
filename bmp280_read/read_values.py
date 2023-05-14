import machine
import network
import time
from machine import I2C
from bmp280 import *
from utils import led_blink

# Define Led pins
LED_R = machine.Pin(16, machine.Pin.OUT)
LED_G = machine.Pin(17, machine.Pin.OUT)
LED_B = machine.Pin(18, machine.Pin.OUT)

# init I2C
bus = I2C(1, scl = machine.Pin(22), sda = machine.Pin(21))
bmp = BMP280(bus)

# wifi credentials
iot_ssid = 'bvnetwerk'
iot_passwd = 'xLbCMeZtac'

# Enable wifi
sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)

while (True):
    if sta_if.isconnected():
        print(sta_if.ifconfig())
        LED_R.value(1)
        print(bmp.temperature)
        led_blink(LED_G, 1)
        time.sleep (30)
    else:
        sta_if.connect(iot_ssid, iot_passwd)
        LED_R.value(0)
        while not sta_if.isconnected():
            pass