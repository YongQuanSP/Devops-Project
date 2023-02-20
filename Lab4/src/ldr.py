from hal import hal_buzzer as buzzer
from hal import hal_led as led
from hal import hal_adc as adc
import time

# Initialize
buzzer.init()
led.init()
adc.init()


while True:
    print("Ldr Value:")
    value = adc.get_adc_value(0)
    print(value)
    if value <= 10000:
        print("Lights are ON")
        led.set_output(0, 1)
        buzzer.short_beep(4)
    elif value > 10000:
        print("Lights are OFF")