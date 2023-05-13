import time
def led_blink(led, interval):
    led.value(1)
    time.sleep(interval)
    led.value(0)
    time.sleep(interval)