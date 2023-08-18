import time
from machine import I2C, Pin
from ds1307 import DS1307
from time import sleep
# Initialize I2C
i2c = I2C(0, scl=Pin(1), sda=Pin(0))  # Using GP1 for SCL and GP0 for SDA

# Initialize DS1307 RTC
rtc = DS1307(i2c)

while True:
    # Get the current time from the DS1307 RTC
    print(rtc.datetime())
    sleep(2)

