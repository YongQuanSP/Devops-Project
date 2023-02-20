from hal import hal_rfid_reader as RFID
from hal import hal_lcd as LCD
import time

lcd = LCD.lcd()
reader = RFID.SimpleMFRC522()
counter = 0


def CardRead():
    auth = []
    global counter
    card_id = reader.read()
    card_id = str(card_id)
    f = open('AuthList.txt', 'a+')
    f = open('AuthList.txt', 'r+')

    if f.mode == 'r+':
        auth = f.read()

    if counter < 3:
        if card_id in auth:
            number = auth.split('\n')
            pos = number.index(card_id)
            lcd.lcd_display_string('Card in Database', 1, pos)
            lcd.lcd_display_string('Access Granted', 2)
            lcd.lcd_clear()
            lcd.lcd_display_string('Car Power ON', 1)
            lcd.lcd_display_string('Drive Safely', 2)
            return 1

        elif card_id not in auth:
            f.write(card_id)
            f.write('\n')
            counter += 1
            lcd.lcd_display_string('New Card', 1)
            lcd.lcd_display_string('Registered', 2)
            time.sleep(3)
            lcd.lcd_clear()
            lcd.lcd_display_string('Car Power ON', 1)
            lcd.lcd_display_string('Drive Safely', 2)
            lcd.lcd_clear()
            return 0

    elif counter >= 3:
        lcd.lcd_display_string('Max Cards Reached', 1)
        lcd.lcd_display_string('Access Denied', 2)
        time.sleep(3)
        lcd.lcd_clear()
        lcd.lcd_display_string('Try Again', 1)
        CardRead()
