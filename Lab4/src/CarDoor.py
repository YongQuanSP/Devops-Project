from hal import hal_input_switch as switch
from hal import hal_led as led
from hal import hal_buzzer as buzzer
from hal import hal_servo as servo
from hal import hal_lcd as LCD
import time
import RPi.GPIO as GPIO

# Initialize All Components
lcd = LCD.lcd()
led.init()
buzzer.init()
switch.init()
servo.init()
led.set_output(0, 0)
# Set 50Hz PWM output at Servo Motor
PWM = GPIO.PWM(26, 50)

while True:
    # If Switch is Open
    if switch.read_slide_switch() == 1:
        lcd.lcd_display_string('Hello World', 1)
        PWM.start(3)
        time.sleep(4)
        PWM.start(12)
        time.sleep(4)

    else:
        led.set_output(0, 1)
        buzzer.short_beep(1)
        break
