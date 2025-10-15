"""
Weather Station - CircuitPython
Displays temperature, humidity, and pressure from BME280 sensor
on a TM1637 4-digit 7-segment display in rotating mode.
"""

import time
import board
import busio
from adafruit_bme280 import basic as adafruit_bme280
from tm1637_display import TM1637Display

# Configuration
DISPLAY_CYCLE_TIME = 10    # Seconds to show each reading
SENSOR_READ_INTERVAL = 2   # Seconds between sensor readings
DISPLAY_BRIGHTNESS = 6     # 0-6, with 6 being brightest
USE_FAHRENHEIT = True      # True for °F, False for °C

# BME280 Configuration
I2C_ADDRESS = 0x76         # BME280 address
I2C_SDA_PIN = board.GP4    # I2C0 SDA
I2C_SCL_PIN = board.GP5    # I2C0 SCL

# TM1637 Configuration
TM1637_CLK_PIN = board.GP2
TM1637_DIO_PIN = board.GP3

# Display modes
MODE_TEMPERATURE = 0
MODE_HUMIDITY = 1
MODE_PRESSURE = 2

print("=" * 50)
print("Weather Station")
print("=" * 50)

# Initialize BME280 sensor
try:
    print(f"\nInitializing BME280 at 0x{I2C_ADDRESS:02X}...")
    i2c = busio.I2C(I2C_SCL_PIN, I2C_SDA_PIN)
    bme280 = adafruit_bme280.Adafruit_BME280_I2C(i2c, address=I2C_ADDRESS)
    print("✓ BME280 sensor initialized")
except Exception as e:
    print(f"✗ Error initializing BME280: {e}")
    raise

# Initialize TM1637 display
try:
    print(f"Initializing TM1637 display...")
    display = TM1637Display(TM1637_CLK_PIN, TM1637_DIO_PIN)
    display.brightness = DISPLAY_BRIGHTNESS
    print("✓ TM1637 display initialized")

    # Show startup pattern
    display.print("----")
    time.sleep(1)
    display.clear()

except Exception as e:
    print(f"✗ Error initializing TM1637: {e}")
    raise

print("\nWeather Station ready!")
print(f"Display cycles every {DISPLAY_CYCLE_TIME}s")
print(f"Sensor reads every {SENSOR_READ_INTERVAL}s")
print("-" * 50)

# State variables
current_mode = MODE_TEMPERATURE
last_mode_change = time.monotonic()
last_sensor_read = 0

# Sensor readings
temperature = 0
humidity = 0
pressure = 0

# Mode names for logging
mode_names = ["TEMPERATURE", "HUMIDITY", "PRESSURE"]

try:
    # Initial sensor read
    temp_c = bme280.temperature
    temperature = int((temp_c * 9/5) + 32) if USE_FAHRENHEIT else int(temp_c)
    humidity = int(bme280.relative_humidity)
    pressure = int(bme280.pressure)

    print(f"\nInitial readings:")
    print(f"  Temp: {temperature}{'°F' if USE_FAHRENHEIT else '°C'}")
    print(f"  Humidity: {humidity}%")
    print(f"  Pressure: {pressure} hPa")
    print(f"\n→ Display mode: {mode_names[current_mode]}")

    # Display initial value
    display.print(f"{temperature:3d}F")

    # Main loop
    while True:
        current_time = time.monotonic()

        # Read sensors at interval
        if current_time - last_sensor_read >= SENSOR_READ_INTERVAL:
            try:
                temp_c = bme280.temperature
                temperature = int((temp_c * 9/5) + 32) if USE_FAHRENHEIT else int(temp_c)
                humidity = int(bme280.relative_humidity)
                pressure = int(bme280.pressure)

                # Update display with current mode's value
                if current_mode == MODE_TEMPERATURE:
                    display.print(f"{temperature:3d}F")
                elif current_mode == MODE_HUMIDITY:
                    display.print(f"H{humidity:3d}")
                elif current_mode == MODE_PRESSURE:
                    display.print(f"{pressure:4d}")

                last_sensor_read = current_time

            except Exception as e:
                print(f"Error reading sensor: {e}")
                display.print("Err ")

        # Cycle display mode at interval
        if current_time - last_mode_change >= DISPLAY_CYCLE_TIME:
            # Move to next mode
            current_mode = (current_mode + 1) % 3
            print(f"\n→ Display mode: {mode_names[current_mode]}")

            # Display appropriate value
            if current_mode == MODE_TEMPERATURE:
                display.print(f"{temperature:3d}F")
                print(f"  Showing: {temperature}{'°F' if USE_FAHRENHEIT else '°C'}")
            elif current_mode == MODE_HUMIDITY:
                display.print(f"H{humidity:3d}")
                print(f"  Showing: {humidity}%")
            elif current_mode == MODE_PRESSURE:
                display.print(f"{pressure:4d}")
                print(f"  Showing: {pressure} hPa")

            last_mode_change = current_time

        # Small delay to prevent busy-waiting
        time.sleep(0.1)

except KeyboardInterrupt:
    print("\n\nWeather Station stopped by user")
    display.print("----")
    time.sleep(0.5)
    display.clear()

except Exception as e:
    print(f"\n\nFatal error: {e}")
    display.print("Err ")
    raise
