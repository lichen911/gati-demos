"""
Weather Station - CircuitPython
Shows temperature, humidity, and pressure on a display.
Press button to switch between them!
"""

import time
import board
import busio
import digitalio
from adafruit_bme280 import basic as adafruit_bme280
from tm1637_display import TM1637Display

# Configuration
SENSOR_UPDATE_TIME = 2     # Seconds between sensor readings
DISPLAY_BRIGHTNESS = 6     # 0-6, with 6 being brightest
I2C_ADDRESS = 0x76         # BME280 sensor address

# Pin Configuration
I2C_SDA_PIN = board.GP4
I2C_SCL_PIN = board.GP5
DISPLAY_CLK_PIN = board.GP2
DISPLAY_DIO_PIN = board.GP3
BUTTON_PIN = board.GP6

# Display modes
MODE_TEMPERATURE = 0
MODE_HUMIDITY = 1
MODE_PRESSURE = 2

# Initialize BME280 sensor
i2c = busio.I2C(I2C_SCL_PIN, I2C_SDA_PIN)
bme280 = adafruit_bme280.Adafruit_BME280_I2C(i2c, address=I2C_ADDRESS)

# Initialize display
display = TM1637Display(DISPLAY_CLK_PIN, DISPLAY_DIO_PIN)
display.brightness = DISPLAY_BRIGHTNESS

# Initialize button
button = digitalio.DigitalInOut(BUTTON_PIN)
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.UP

# Track which mode we're in: 0=temp, 1=humidity, 2=pressure
current_mode = 0

# Track button state
last_button_state = True

# Track when we last read the sensor
last_sensor_read_time = time.monotonic()

# Main loop
while True:
    current_time = time.monotonic()

    # Check if it's time to read the sensor (every 2 seconds)
    if current_time - last_sensor_read_time >= SENSOR_UPDATE_TIME:
        # Read sensor data
        temp_f = int((bme280.temperature * 9/5) + 32)
        humidity = int(bme280.relative_humidity)
        pressure = int(bme280.pressure)

        # Show current mode on display
        if current_mode == 0:
            display.print(f"{temp_f:3d}F")
        elif current_mode == 1:
            display.print(f"H{humidity:3d}")
        elif current_mode == 2:
            display.print(f"{pressure:4d}")

        # Remember when we read the sensor
        last_sensor_read_time = current_time

    # Check if button was pressed
    current_button_state = button.value
    if last_button_state and not current_button_state:
        # Button pressed - go to next mode
        current_mode = (current_mode + 1) % 3

        # Wait for button release
        while not button.value:
            time.sleep(0.05)

    last_button_state = current_button_state

    # Small sleep to avoid burning CPU
    time.sleep(0.05)
