import network
import time
from umqtt.simple import MQTTClient

def wifi_connect(ssid, password):
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        sta_if.active(True)
        sta_if.connect(ssid,password)
    while not sta_if.isconnected():
        pass
    print("network config: " ,sta_if.ifconfig())
    return sta_if


def wifi_connected(sta_if):
    return sta_if.active

def mqtt_connect(host, clientid):
    client = MQTTClient(
        client_id = clientid,
        server = host,
        port = 1883,
        user = None,
        password = None,
        keepalive = 120)
    client.connect()
    return client

def send_mqtt_payload(client, topic, payload):
    client.publish(topic,payload)