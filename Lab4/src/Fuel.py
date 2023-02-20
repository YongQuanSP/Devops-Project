import RPi.GPIO as GPIO
import time
from hal import hal_usonic as sonic

# Set up the GPIO pins
GPIO.setmode(GPIO.BCM)
sonic.init()
tails = sonic.get_distance()

while True:
    print(sonic.get_distance())

    if sonic.get_distance() < 20:
        print("The fuel level is still full")
    elif sonic.get_distance() < 50:
        print("The fuel level is more than half")
    elif sonic.get_distance() < 100:
        print("The fuel level is low")
    else:
        print("Low Fuel!")
    time.sleep(1)