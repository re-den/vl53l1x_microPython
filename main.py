from machine import Pin, SoftI2C, PWM
from vl53l1x import VL53L1X
import time

LED_PIN = 2
OLD_DIST = 0
freq = 0
start_range = 2000
stop_range = int(start_range * 0.05)

i2c = SoftI2C(scl=Pin(22), sda=Pin(21))
distance = VL53L1X(i2c)
led = PWM(Pin(LED_PIN), freq=1000)

OldMax = stop_range
OldMin = start_range
NewMax = 1023
NewMin = 200

OldRange = (OldMax - OldMin)  
NewRange = (NewMax - NewMin)  

while True:
  dist = distance.read()

  
  if dist < start_range and dist > stop_range:
    freq = int((start_range/dist)**3)
    freq = min(max(freq, 0), 50)
    pwm = int((((dist - OldMin) * NewRange) / OldRange) + NewMin)
    #if dist - OLD_DIST > 5:
    print(f'{dist} mm  |  {freq} Hz  |  {pwm}')
    led.freq(freq)
    led.duty(pwm)
  else:
    led.duty(0)
    #if dist - OLD_DIST > 10:
    print(f'{dist}')
  OLD_DIST = dist
  freq = 0
  time.sleep_ms(100)
