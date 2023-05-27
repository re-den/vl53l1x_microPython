from machine import Pin, SoftI2C, PWM
from vl53l1x import VL53L1X
import time

LED_PIN = 2
OLD_DIST = 0
freq = 0
start_range = 1000
stop_range = start_range * 0.1

i2c = SoftI2C(scl=Pin(22), sda=Pin(21))
distance = VL53L1X(i2c)
led = PWM(Pin(LED_PIN), freq=10000)

while True:
  dist = distance.read()
  if dist < start_range and dist > stop_range:
    freq = int((start_range/dist)**3)
    freq = min(max(freq, 0), int(start_range))
    #if dist - OLD_DIST > 5:
    print(f'{dist} mm\t|\t{freq} Hz')
    led.freq(freq)
    led.duty(512)
  else:
    led.duty(0)
    if dist - OLD_DIST > 10:
      print(f'{dist}')
  OLD_DIST = dist
  freq = 0
  time.sleep_ms(5)
  