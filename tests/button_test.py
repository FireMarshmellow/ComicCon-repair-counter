from machine import I2C, Pin
from time import sleep

# Initialize the button
button = Pin(16, Pin.IN, Pin.PULL_UP)

while True:
    print(button.value())
    sleep(1)



