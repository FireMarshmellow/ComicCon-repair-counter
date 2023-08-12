from machine import I2C, Pin
from ds1307 import DS1307

# Initialize I2C
i2c = I2C(0, scl=Pin(1), sda=Pin(0))  # Using GP1 for SCL and GP0 for SDA

# Initialize DS1307 RTC
rtc = DS1307(i2c)

# Set the time: (year, month, day, weekday, hour, minute, second, subsecond)
# For example, to set the time to August 12, 2023, 15:30:00 (3:30 PM):
rtc.datetime((2023, 8, 12, 6, 20, 45, 0, 0))

print("Time set successfully!")