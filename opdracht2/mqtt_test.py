from comms import connect, send_mqtt_payload
import time

# wifi credentials
iot_ssid = 'bvnetwerk'
iot_passwd = 'xLbCMeZtac'
mqtt_server = "10.20.226.113"

connect(iot_ssid, iot_passwd)

topic = "sensors/bas_esp"
payload = "hello"

#while(True):
send_mqtt_payload(mqtt_server, "esp_bas", topic, payload)
print(f"message sent to {mqtt_server} on topic {topic} with payload {payload}")
time.sleep(10)
