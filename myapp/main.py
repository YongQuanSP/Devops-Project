import RPi.GPIO as GPIO
import time
from hal import hal_usonic as sonic
from hal import hal_adc as adc
from hal import dht11 as dht
from hal import hal_temp_humidity_sensor as th
from flask import Blueprint, render_template
from flask_login import login_required, current_user
from . import db

main = Blueprint('main', __name__)

# Set up the GPIO pins
GPIO.setmode(GPIO.BCM)

# hal_usonic
sonic.init()
tails = sonic.get_distance()

# hal_adc
adc.init()
bat = adc.get_adc_value(0)

# hal_temp_humidity_sensor
th.init()

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', name=current_user.name)

@main.route('/dashboard')
@login_required
def dashboard():
    fuel = getFuel()
    battery = getBattery()
    humid = getHumid()
    return render_template('dashboard.html', name=current_user.name, fuel=fuel, battery=battery, humid=humid)

# Functions for readings
def getFuel():
    while True:
        if sonic.get_distance() < 20:
            print("The fuel level is still full")
        elif sonic.get_distance() < 50:
            print("The fuel level is more than half")
        elif sonic.get_distance() < 100:
            print("The fuel level is low")
        else:
            print("Low Fuel!")
        time.sleep(1)

def getBattery():
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

def getHumid():
    while True:
    if th.read_temp_humidity() is None: #if not working
        print("Unable to read car engine temperature.")
        time.sleep(5)  # Change this to the interval you want to output the readings
    else:
        print(th.read_temp_humidity())
        time.sleep(2)