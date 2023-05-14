import comms
import time

# wifi credentials
#iot_ssid = 'bvnetwerk'
#iot_passwd = 'xLbCMeZtac'
#mqtt_server = "10.20.226.113"
iot_ssid = "pi4desk"
iot_passwd = "sensornetwork"
mqtt_server = "192.168.220.1"

sta_if = comms.wifi_connect(iot_ssid, iot_passwd)

if comms.wifi_connected(sta_if):
    mqtt_client=comms.mqtt_connect(mqtt_server, "esp_bas")
else:
    sta_if = comms.wifi_connect(iot_ssid, iot_passwd)

topic = "sensors/bas_esp"
payload = "hello"

#while(True):

comms.send_mqtt_payload(mqtt_client, topic, payload)
print(f"message sent to {mqtt_server} on topic {topic} with payload {payload}")

