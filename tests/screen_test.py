import machine
from machine import I2C, Pin
import ssd1306
from time import sleep

i2c = machine.SoftI2C(scl=Pin(15), sda=Pin(14))

oled_width = 128
oled_height = 32
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)

def center_text(text, screen_width, char_width=8):
    text_width = len(text) * char_width
    return (screen_width - text_width) // 2

for i in range(100):
    # Clear the display
    oled.fill(0)
    meg = f"{'hello'} {i}"

    # Display centered text
    x = center_text(str(meg), oled_width)
    oled.text(str(meg), x, 0)

    # Update the display
    oled.show()
    sleep(1)
