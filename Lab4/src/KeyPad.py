from hal import hal_lcd as LCD
from hal import hal_keypad as KEY
import time
import RPi.GPIO as GPIO


lcd = LCD.lcd()
lcd.lcd_display_string('1. Power On Car', 1)
lcd.lcd_display_string('2. Power OFF', 2)


def handle_key_press(key):
    if key == 1:
        lcd.lcd_clear()
        lcd.lcd_display_string('This Works', 1)
    elif key == 2:
        lcd.lcd_clear()
        lcd.lcd_display_string('Thank You', 1)
        lcd.lcd_display_string('Powering OFF', 2)
        time.sleep(3)
        lcd.lcd_clear()


KEY.init(handle_key_press)
while True:
    KEY.get_key()
