import machine
from machine import I2C, Pin
import ssd1306
from time import sleep, sleep_ms
from ds1307 import DS1307
from large_font import font as large_font
import math
import urandom
import os

# Constants
OLED_WIDTH = 128
OLED_HEIGHT = 32
BUTTON_DEBOUNCE_DELAY = 0.1
FIREWORK_DELAY = 1
MAX_RADIUS = int((OLED_WIDTH**2 + OLED_HEIGHT**2)**0.5)
LOG_FILE = 'button_presses.csv'

# Initialize OLED I2C
i2c_oled = machine.SoftI2C(scl=Pin(15), sda=Pin(14))
oled = ssd1306.SSD1306_I2C(OLED_WIDTH, OLED_HEIGHT, i2c_oled)

# Initialize the button
button = Pin(16, Pin.IN, Pin.PULL_UP)

# Initialize DS1307 RTC I2C
i2c_rtc = I2C(0, scl=Pin(1), sda=Pin(0))
rtc = DS1307(i2c_rtc)

# Check if the log file exists, if not, create it
if LOG_FILE not in os.listdir():
    with open(LOG_FILE, 'w') as f:
        f.write('Timestamp\n')

def log_button_press(timestamp):
    with open(LOG_FILE, 'a') as f:
        f.write('{}\n'.format(timestamp))

def get_today_button_presses(year, month, day):
    count = 0
    try:
        with open(LOG_FILE, 'r') as f:
            lines = f.readlines()
            for line in lines:
                if line.startswith("{:04}-{:02}-{:02}".format(year, month, day)):
                    count += 1
    except:
        pass
    return count


def draw_large_char(oled, char, x, y):
    for row in range(16):
        for col in range(16):
            pixel = (large_font[char]	[row] >> (15 - col)) & 1
            oled.pixel(x + col, y + row, pixel)

def draw_big_text(oled, text, x, y):
    for char in text:
        if char in large_font:
            draw_large_char(oled, char, x, y)
            x += 18

def display_partitioned_screen(num1, num2, time_str):
    oled.fill(0)
    for y in range(OLED_HEIGHT):
        oled.pixel(OLED_WIDTH // 2, y, 1)
    for x in range(OLED_WIDTH // 2, OLED_WIDTH):
        oled.pixel(x, OLED_HEIGHT // 2, 1)
    draw_big_text(oled, str(num1), 0, 8)
    oled.text(str(num2), 70, 2)
    oled.text(time_str, 70, 18)
    oled.show()

def firework_animation():
    def draw_firework(radius):
        for angle in range(0, 360, 5):
            random_angle = angle + urandom.randint(-10, 10)
            random_length = radius + urandom.randint(-5, 5)
            end_x = OLED_WIDTH // 2 + int(random_length * math.cos(math.radians(random_angle)))
            end_y = OLED_HEIGHT // 2 + int(random_length * math.sin(math.radians(random_angle)))
            oled.pixel(end_x, end_y, 1)

    selected_phrase = urandom.choice([
        "All set!", "Good as new!", "Fixed!", "Sorted!", "patched!", "It's done!"
    ])

    for radius in range(0, MAX_RADIUS + 1, 2):
        oled.fill(0)
        draw_firework(radius)
        if radius > 10:
            draw_firework(radius - 10)
        if radius > 20:
            oled.text(selected_phrase, (OLED_WIDTH - len(selected_phrase) * 8) // 2, OLED_HEIGHT // 2)
        oled.show()
        sleep_ms(FIREWORK_DELAY)
    sleep(0.1)

counter1 = 0
last_hour = None
button_presses_this_hour = 0
year, month, day, _, _, _, _, _ = rtc.datetime()
counter1 = get_today_button_presses(year, month, day)

while True:
    year, month, day, weekday, hour, minute, second, _ = rtc.datetime()
    time_str = "{:02}:{:02}:{:02}".format(hour, minute, second)

    if not button.value():
        firework_animation()
        counter1 += 1
        timestamp = "{:04}-{:02}-{:02} {:02}:{:02}:{:02}".format(year, month, day, hour, minute, second)
        log_button_press(timestamp)
        
        if last_hour is None or last_hour != hour:
            last_hour = hour
            button_presses_this_hour = 0
        
        button_presses_this_hour += 1
        sleep(BUTTON_DEBOUNCE_DELAY)

    display_partitioned_screen(counter1, button_presses_this_hour, time_str)
    counter1 %= 1000
    sleep(0.1)

