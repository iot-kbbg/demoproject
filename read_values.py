import machine
import network
import time
from machine import I2C
from bmp280 import *
from utils import led_blink
from umqtt import MQTTClient
import ubinascii

# Define Led pins
LED_R = machine.Pin(16, machine.Pin.OUT)
LED_G = machine.Pin(17, machine.Pin.OUT)
LED_B = machine.Pin(18, machine.Pin.OUT)

# init I2C
bus = I2C(1, scl = machine.Pin(22), sda = machine.Pin(21))
bmp = BMP280(bus)

# credentials
#iot_ssid = 'bvnetwerk'
#iot_passwd = 'xLbCMeZtac'
#mqtt_server
iot_ssid = "Bas&Sanja"
iot_passwd = "0499619079"
mqtt_server = "192.168.0.212"
client_id = ubinascii.hexlify(machine.unique_id())
# Enable wifi
sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)

# MQTT callback function for receiving messages
def sub_cb(topic, msg):
  print((topic, msg))
  
# client connect function
def client_connect(client_id, mqtt_server):
    client=MQTTClient(client_id, mqtt_server)
    client.set_callback(sub_cb)
    client.connect()
    return client

while (True):
    if sta_if.isconnected():
        try:
            #client=client_connect(client_id, mqtt_server)
            client=MQTTClient(
                client_id = client_id,
                server = mqtt_server,
                port = 1883,
                user=None,
                password=None,
                keepalive = 120)
            client.set_callback(sub_cb)
            client.connect()
            
            LED_B.value(1)
            print(sta_if.ifconfig())
            LED_R.value(1)
            print(bmp.temperature)
            client.publish('test/bmp', str(bmp.temperature))
            led_blink(LED_G, 1)
            time.sleep (30)
        except OSError as e:
            print('Failed to connect to MQTT broker. Reconnecting...')
            time.sleep(10)
            machine.reset()
    else:
        sta_if.connect(iot_ssid, iot_passwd)
        LED_R.value(0)
        while not sta_if.isconnected():
            pass