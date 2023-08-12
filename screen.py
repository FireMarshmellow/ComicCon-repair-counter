import machine
from machine import I2C, Pin
import ssd1306
from time import sleep, localtime

i2c = machine.SoftI2C(scl=Pin(15), sda=Pin(14))

oled_width = 128
oled_height = 32
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)


while True:
    # For demonstration purposes, using static numbers and current time
    current_time = localtime()
    time_str = "{:02}:{:02}".format(current_time[3], current_time[4])
    display_partitioned_screen(123, 456, time_str)
    sleep(1)