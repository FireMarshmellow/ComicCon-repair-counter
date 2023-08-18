from machine import I2C, Pin
from time import sleep
from ds1307 import DS1307


# Initialize DS1307 RTC I2C
i2c_rtc = I2C(0, scl=Pin(1), sda=Pin(0))
rtc = DS1307(i2c_rtc)

while True:
    # Get the current time from the DS1307 RTC
    print(rtc.datetime())
    sleep(2)
