from machine import Pin, SoftI2C, PWM
from vl53l1x import VL53L1X
import time

LED_PIN = 2
i2c = SoftI2C(scl=Pin(22), sda=Pin(21))
distance = VL53L1X(i2c)
led = PWM(Pin(LED_PIN), freq=1)

while True:
  dist = distance.read()
  if dist < 500 and dist > 1:
    freq = int((500/dist)**2)
    print(freq)
    freq = min(max(freq, 1), 40)
    led.freq(freq)
    led.duty(512)
  else:
    led.duty(0)
  print(f'{dist} mm')
  time.sleep_ms(200)
  