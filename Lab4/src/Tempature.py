from hal import hal_temp_humidity_sensor as th
import time

th.init()


def CheckTempHumidity():
    if th.read_temp_humidity() is None:
        print("Unable to read car engine temperature.")
        time.sleep(5)  # Change this to the interval you want to output the readings
    else:
        print(th.read_temp_humidity())
        time.sleep(2)
