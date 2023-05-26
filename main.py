from machine import Pin, SoftI2C, PWM
from vl53l1x import VL53L1X
import time

LED_PIN = 2
OLD_DIST = 0
freq = 0

i2c = SoftI2C(scl=Pin(22), sda=Pin(21))
distance = VL53L1X(i2c)
led = PWM(Pin(LED_PIN), freq=1)

while True:
  dist = distance.read()
  if dist < 500 and dist > 10:
    freq = int((550/dist)**2)
    freq = min(max(freq, 0), 50)
    #if dist - OLD_DIST > 5:
    print(f'{dist} mm\t|\t{freq} Hz')
    led.freq(freq)
    led.duty(512)
  else:
    led.duty(0)
    #if dist - OLD_DIST > 5:
    #print(f'{dist} mm\t+\t{freq} Hz')
  OLD_DIST = dist
  freq = 0
  time.sleep_ms(5)
  

