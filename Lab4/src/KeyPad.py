from hal import hal_lcd as LCD
from hal import hal_keypad as KEY
import time

lcd = LCD.lcd()

def handle_key_press(key):
    while True:
        if key == 1:
            lcd.lcd_clear()
            lcd.lcd_display_string('Tap your Card', 1)
            lcd.lcd_display_string('To Power On', 2)
        elif key == 2:
            lcd.lcd_clear()
            lcd.lcd_display_string('Thank you', 1)
            lcd.lcd_display_string('Powering OFF', 2)
            time.sleep(3)
            lcd.lcd_clear()
            lcd.lcd_display_string('1. Power On Car', 1)
        time.sleep(0.1)
        break

KEY.init(handle_key_press)
while True:
    KEY.get_key()
