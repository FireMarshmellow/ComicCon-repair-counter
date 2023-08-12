# ComicCon repair counter
 
1. **MicroPython Firmware for Raspberry Pi Pico**: 
   - You need to have MicroPython flashed onto your Raspberry Pi Pico. You can get the firmware and instructions from the official [MicroPython website](https://micropython.org/download/pico/).

2. **MicroPython Libraries**:
   - `machine`: This is a built-in library in MicroPython, so you don't need to install it separately. It provides functions to interact with the hardware.
   - `ssd1306`: This library is for the SSD1306 OLED display. You can find various versions of this library online, but [this one](https://github.com/micropython/micropython/blob/master/drivers/display/ssd1306.py) from the official MicroPython repository is commonly used.
   - `ds1307`: This library is for the DS1307 RTC module. There are different versions available online. Ensure you have one that's compatible with MicroPython and the Raspberry Pi Pico.

3. **Custom Font**:
   - `large_font`: This is a custom font module you've mentioned. If you've created it based on our earlier discussion, ensure it's available on the Pico's filesystem.

4. **Hardware**:
   - Raspberry Pi Pico board.
   - SSD1306 OLED display module.
   - DS1307 RTC module.
   - Necessary jumper wires, breadboard, and possibly pull-up resistors for I2C communication.

5. **Software Tools**:
   - **Thonny**: An integrated development environment (IDE) that supports MicroPython and allows for easy code upload and REPL interaction with the Raspberry Pi Pico. You can download it from the [official website](https://thonny.org/).
   - **rshell** or **ampy**: These are command-line tools that help in uploading scripts and managing files on MicroPython devices. They can be installed via pip.

6. **Optional**:
   - **mu-editor**: An alternative to Thonny, the [mu-editor](https://codewith.mu/) is another IDE that supports MicroPython and the Raspberry Pi Pico.

**Installation**:
For the libraries like `ssd1306` and `ds1307`, you'll need to download the `.py` files and upload them to your Raspberry Pi Pico. You can use Thonny, rshell, or ampy to manage and upload files to the Pico.

Remember, the exact steps and requirements might vary based on the specific versions of libraries and tools you're using. Always refer to the documentation or repository README files for the most accurate information.