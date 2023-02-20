import RPi.GPIO as GPIO
import time
from hal import hal_adc as adc

# Set up the GPIO pins
adc.init()
bat = adc.get_adc_value(0)
GPIO.setmode(GPIO.BCM)
# Change this to the pin-number your potentiometer is connected to


while True:
    print(adc.get_adc_value(1))
    if adc.get_adc_value() < 205:
        print("Battery level is low")
    elif adc.get_adc_value() < 510:
        print("Battery level is at 20-49%")
    elif adc.get_adc_value() < 512:
        print("Battery level is at 50%")
    elif adc.get_adc_value() < 820:
        print("Battery level is at 51-79%")
    else:
        print("Battery level is at 80-100%")
    time.sleep(0.1)