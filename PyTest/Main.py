# from hal import hal_lcd as LCD
# from hal import hal_rfid_reader as RFID
# from hal import hal_keypad as KEY
# from hal import hal_input_switch as switch
# from hal import hal_led as led
# from hal import hal_adc as adc
# from hal import hal_buzzer as buzzer
# from hal import hal_servo as servo
# from hal import hal_dc_motor as dc
# from hal import hal_usonic as sonic
# from hal import hal_temp_humidity_sensor as th
from threading import Thread
import time
import telepot

# Initialize
# th.init()
# dc.init()
# led.init()
# adc.init()
# lcd = LCD.lcd()
# sonic.init()
# switch.init()
# servo.init()
# buzzer.init()
# reader = RFID.SimpleMFRC522()
counter = 0

bot = telepot.Bot('6084477926:AAEZevNrxh4TnXVsVrf-wwoZ5_ahN1fhfKE')
chat_id = 1248386917

'''
def Display():
    lcd.lcd_display_string('1. Power On Car', 1)
    lcd.lcd_display_string('2. Power OFF', 2)
    return 1


def StartEngine():
    dc.set_motor_speed(100)
    return 1


def CloseEngine():
    dc.set_motor_speed(0)
    return 1


def OpenDoor():
    servo.set_servo_position(100)
    return 1


def CloseDoor():
    servo.set_servo_position(0)
    return 1


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


def handle_key_press(key):
    while True:
        if key == 1:
            lcd.lcd_clear()
            lcd.lcd_display_string('Tap your Card', 1)
            lcd.lcd_display_string('To Power On', 2)
            if CardRead() in (0, 1):
                dc.set_motor_speed(100)
            else:
                dc.set_motor_speed(0)
        elif key == 2:
            lcd.lcd_clear()
            lcd.lcd_display_string('Thank you', 1)
            lcd.lcd_display_string('Powering OFF', 2)
            dc.set_motor_speed(0)
            time.sleep(3)
            lcd.lcd_clear()
            lcd.lcd_display_string('1. Power On Car', 1)
        time.sleep(0.1)
        break


def CarTheft():
    while True:
        if switch.read_slide_switch() == 1:
            bot.sendMessage(chat_id, "Door is being manually opened! ")
            blink_led(1)
            time.sleep(1)
            buzzer.short_beep(1)
        elif switch.read_slide_switch() == 0:
            continue
'''


def CheckBatteryLevel(battery):
    # battery = adc.get_adc_value(0)
    if battery < 205:
        bot.sendMessage(chat_id, "Battery level is low!")
        return 0
    elif battery < 510:
        bot.sendMessage(chat_id, "Battery level is at 20-49%!")
        return 1
    elif battery < 512:
        bot.sendMessage(chat_id, "Battery level is at 50%")
        return 2
    elif battery < 820:
        bot.sendMessage(chat_id, "Battery level is at 51-79%")
        return 3
    else:
        bot.sendMessage(chat_id, "Battery level is at 80-100%")
        return 4
    time.sleep(0.1)


def CheckFuelLevel(distance):
    # distance = sonic.get_distance()
    if distance < 20:
        bot.sendMessage(chat_id, "The fuel level is still full")
        return 0
    elif distance < 50:
        bot.sendMessage(chat_id, "The fuel level is more than half")
        return 1
    elif distance < 100:
        bot.sendMessage(chat_id, "The fuel level is low")
        return 2
    else:
        bot.sendMessage(chat_id, "The fuel level is low fuel")
        return 3
    time.sleep(1)


def CheckTempHumidity(temp):
    # if th.read_temp_humidity() is None:
    if temp is None:
        # bot.sendMessage(chat_id, "Unable to read car engine temperature!")
        # time.sleep(5)
        return 0
    else:
        # bot.sendMessage(chat_id, f'The temperature is {th.read_temp_humidity()}')
        # time.sleep(2)
        return 1


def Light(value):
    while True:
        # value = adc.get_adc_value(0)
        if value <= 700:
            bot.sendMessage(chat_id, "Possible Car Theft Attempt ")
            # blink_led(1)
            # time.sleep(1)
            # buzzer.short_beep(1)
            return 1
        else:
            return 0


'''
def blink_led(delay):
    led.set_output(0, 1)
    time.sleep(delay)

    led.set_output(0, 0)
    time.sleep(delay)
'''

'''
def handle_command(msg):
    command = msg['text']
    chat_id = msg['chat']['id']
    if command == 'Open':
        OpenDoor()
    elif command == 'Close':
        CloseDoor()
    elif command == 'Battery':
        CheckBatteryLevel()
    elif command == "Check Fuel Level":
        CheckFuelLevel()
    elif command == "Temp":
        CheckTempHumidity()
    elif command == "Start Engine" and CloseDoor():
        StartEngine()
    elif command == "Off Engine":
        CloseEngine()
    else:
        bot.sendMessage(chat_id, 'invalid command')


def handle_message(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    if content_type == 'text':
        handle_command(msg)


def main():
    Display()
    KEY.init(handle_key_press)
    # Initialize Thread
    key = Thread(target=CardRead, args=KEY.get_key())
    theft = Thread(target=CarTheft)
    light = Thread(target=Light)

    # Start Thread
    key.start()
    theft.start()
    light.start()

    # Telegram
    bot.message_loop(handle_message)
    while True:
        time.sleep(10)


if __name__ == '__Main__':
    main()
'''
