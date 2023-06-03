import comms
import time
import machine
from bmp280 import *

# wifi credentials
#iot_ssid = 'bvnetwerk'
#iot_passwd = 'xLbCMeZtac'
#mqtt_server = "10.20.226.113"
iot_ssid = "pi4desk"
iot_passwd = "sensornetwork"
mqtt_server = "192.168.220.1"

# init I2C
bus = machine.I2C(1, scl = machine.Pin(22), sda = machine.Pin(21))
bmp = BMP280(bus)

sta_if = comms.wifi_connect(iot_ssid, iot_passwd)
print("connecting to WiFi...")

while not comms.wifi_connected(sta_if):
    time.sleep(1)
    print(".")

mqtt_client=comms.mqtt_connect(mqtt_server, "esp_bas")

topic = "sensors/bas_esp"
payload = "hello"

while(True):
    temp = bmp.temperature
    payload_temp = '{"temperature": ' + str(bmp.temperature) + '}'
    comms.send_mqtt_payload(mqtt_client, topic, payload_temp)
    print(payload_temp)
    time.sleep(30)
    

print(f"message sent to {mqtt_server} on topic {topic} with payload {payload}")

