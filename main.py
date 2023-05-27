from machine import Pin, SoftI2C
from vl53l1x import VL53L1X
import time

led = Pin(2,Pin.Out)
i2c = SoftI2C(scl=Pin(22), sda=Pin(21))
distance = VL53L1X(i2c)
led = Pin(2, Pin.OUT)

def blink(time, count):

while True:
    if distance.read()<500:
        led.value(1)
    else:
        led.value(0)
    time.sleep_ms(200)

