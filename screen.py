import machine
from machine import I2C, Pin
import ssd1306
from time import sleep, localtime

i2c = machine.SoftI2C(scl=Pin(15), sda=Pin(14))

oled_width = 128
oled_height = 32
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)

def display_partitioned_screen(num1, num2, time_str):
    oled.fill(0)
    
    # Draw vertical line to separate left and right partitions
    for y in range(oled_height):
        oled.pixel(64, y, 1)
    
    # Draw horizontal line to separate top right and bottom right partitions
    for x in range(64, oled_width):
        oled.pixel(x, 16, 1)
    
    # Display numbers and time
    oled.text(str(num1), 5, 10)  # Adjust x, y to center the number in partition 1
    oled.text(str(num2), 70, 2)  # Adjust x, y to center the number in partition 2
    oled.text(time_str, 70, 18)  # Adjust x, y to center the time in partition 3
    
    oled.show()

while True:
    # For demonstration purposes, using static numbers and current time
    current_time = localtime()
    time_str = "{:02}:{:02}".format(current_time[3], current_time[4])
    display_partitioned_screen(123, 456, time_str)
    sleep(1)

