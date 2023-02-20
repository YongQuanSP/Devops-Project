import RPi.GPIO as GPIO
from hal import dht11 as dht
from hal import hal_temp_humidity_sensor as th
import time

GPIO.setmode(GPIO.BCM)

th.init()

while True:
    if th.read_temp_humidity() is None: #if not working
        print("Unable to read car engine temperature.")
        time.sleep(5)  # Change this to the interval you want to output the readings
    else:
        print(th.read_temp_humidity())
        time.sleep(2)