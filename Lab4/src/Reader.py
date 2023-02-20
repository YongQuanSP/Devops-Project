from hal import hal_rfid_reader as RFID
from hal import hal_lcd as LCD
import time
import RPi.GPIO as GPIO

lcd = LCD.lcd()
reader = RFID.SimpleMFRC522()
auth = []
counter = 0

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
        lcd.lcd_display_string('Card in Database', 1)
        lcd.lcd_display_string('Access Granted', 2)

    elif card_id not in auth:
        f.write(card_id)
        f.write('\n')
        counter += 1
        lcd.lcd_display_string('New Card Registered', 1)
        time.sleep()
        lcd.lcd_clear()

    else:
        lcd.lcd_display_string('Max Cards Reached', 1)
        lcd.lcd_display_string('Access Denied', 2)
        time.sleep(3)
        lcd.lcd_clear()
