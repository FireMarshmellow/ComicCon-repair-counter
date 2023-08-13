import machine
from machine import I2C, Pin
import ssd1306
from time import sleep
from ds1307 import DS1307
from large_font import font as large_font

# Initialize OLED I2C
i2c_oled = machine.SoftI2C(scl=Pin(15), sda=Pin(14))
oled_width = 128
oled_height = 32
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c_oled)

# Initialize the button
button = Pin(16, Pin.IN, Pin.PULL_UP)

# Initialize DS1307 RTC I2C
i2c_rtc = I2C(0, scl=Pin(1), sda=Pin(0))
rtc = DS1307(i2c_rtc)

def draw_large_char(oled, char, x, y):
    for row in range(16):
        for col in range(16):
            pixel = (large_font[char][row] >> (15 - col)) & 1
            oled.pixel(x + col, y + row, pixel)

def draw_big_text(oled, text, x, y):
    for char in text:
        if char in large_font:
            draw_large_char(oled, char, x, y)
            x += 18  # Move to the next character position with a small gap

def display_partitioned_screen(num1, num2, time_str):
    oled.fill(0)
    
    # Draw vertical line to separate left and right partitions
    for y in range(oled_height):
        oled.pixel(64, y, 1)
    
    # Draw horizontal line to separate top right and bottom right partitions
    for x in range(64, oled_width):
        oled.pixel(x, 16, 1)
    
    # Display numbers and time
    draw_big_text(oled, str(num1), 0, 8)  # Adjust x, y to center the number in partition 1
    oled.text(str(num2), 70, 2)  # Adjust x, y to center the number in partition 2
    oled.text(time_str, 70, 18)  # Adjust x, y to center the time in partition 3
    
    oled.show()

counter1 = 0
counter2 = 23

while True:
    # Check if the button is pressed
    if not button.value():  # Button is pressed when value is LOW (or False)
        counter1 += 1
        sleep(0.2)  # Debounce delay to avoid multiple increments for a single press

    # Get the current time from the DS1307 RTC
    year, month, day, weekday, hour, minute, second, _ = rtc.datetime()
    time_str = "{:02}:{:02}:{:02}".format(hour, minute, second)
    
    display_partitioned_screen(str(counter1), str(counter2), time_str)
    
    counter2 += 1
    
    if counter1 > 999:
        counter1 = 0

    if counter2 > 999:
        counter2 = 0

    sleep(1)



