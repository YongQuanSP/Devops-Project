import time
from hal import hal_adc as adc

# Set up the GPIO pins
adc.init()


def CheckBatteryLevel():
    battery = adc.get_adc_value(0)
    while True:
        if battery < 205:
            print("Battery level is low")
        elif battery < 510:
            print("Battery level is at 20-49%")
        elif battery < 512:
            print("Battery level is at 50%")
        elif battery < 820:
            print("Battery level is at 51-79%")
        else:
            print("Battery level is at 80-100%")
        time.sleep(0.1)
