from hal import hal_input_switch as switch
from hal import hal_led as led
from hal import hal_buzzer as buzzer
import time

switch.init()
led.init()
buzzer.init()


def CarTheft():
    while True:
        if switch.read_slide_switch() == 1:
            print("Door is being manually Opened!")
            led.set_output(0, 1)
            time.sleep(1)
            buzzer.short_beep(1)
        elif switch.read_slide_switch() == 0:
            continue
