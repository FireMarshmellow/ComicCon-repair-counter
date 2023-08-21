# ComicCon Repair Counter

This project provides a visual representation of the number of repairs done at a ComicCon event. It uses an OLED display connected to a microcontroller to show the repair count in real-time. Additionally, every button press (indicating a repair) is logged with its timestamp in a CSV file. This data can later be visualized using a Python script.

#Video
https://youtu.be/GgCQQEq_J6w

## Features

- **Real-time Display**: The OLED display shows the current repair count, hourly count, and the current time.
- **Button Interaction**: Every button press increments the repair count. There's also a secondary button to decrement the count if needed.
- **Firework Animation**: A firework animation is displayed on the OLED screen upon every button press.
- **Data Logging**: Every button press is logged with its timestamp in a CSV file.
- **Data Visualization**: A Python script is provided to visualize the hourly repair count for each day using bar graphs.

## Hardware Requirements

- Microcontroller (e.g., Raspberry Pi Pico)
- OLED Display (128x32)
- DS1307 RTC Module
- 2x Push Buttons

## Software Requirements

- MicroPython
- Required Python Libraries:
  - `machine`
  - `ssd1306`
  - `ds1307`
  - `time`
  - `urandom`
  - `os`
  - `utime`

## Setup

1. Connect the OLED display and DS1307 RTC module to the microcontroller.
2. Upload the main script to the microcontroller.
3. Connect the button to the specified GPIO pin.
4. Run the script to start the counter.

## Data Visualization

To visualize the repair count data:

1. Ensure you have Python installed on your machine.
2. Install the required Python libraries:
   ```
   pip install pandas matplotlib
   ```
3. Run the provided Python script:
   ```python
   python visualize_data.py
   ```

This script reads the `button_presses.csv` file, processes the data, and displays bar graphs showing the hourly repair count for each day.
