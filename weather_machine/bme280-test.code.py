"""
BME280 Sensor Test - CircuitPython
Simple test to verify BME280 sensor connectivity and read temperature.
"""

import time
import board
import busio
from adafruit_bme280 import basic as adafruit_bme280

# Configuration
I2C_ADDRESS = 0x76         # BME280 address (try 0x76 if this doesn't work)
I2C_SDA_PIN = board.GP4    # I2C0 SDA
I2C_SCL_PIN = board.GP5    # I2C0 SCL
USE_FAHRENHEIT = True      # True for °F, False for °C

print("=" * 50)
print("BME280 Sensor Test")
print("=" * 50)

# Initialize I2C and BME280
try:
    print(f"\nInitializing I2C on SDA={I2C_SDA_PIN}, SCL={I2C_SCL_PIN}...")
    i2c = busio.I2C(I2C_SCL_PIN, I2C_SDA_PIN)

    print(f"Connecting to BME280 at address 0x{I2C_ADDRESS:02X}...")
    bme280 = adafruit_bme280.Adafruit_BME280_I2C(i2c, address=I2C_ADDRESS)

    print("✓ BME280 sensor initialized successfully!")
    print("\nReading temperature every 2 seconds...")
    print("Press Ctrl+C to stop\n")
    print("-" * 50)

except Exception as e:
    print(f"\n✗ Error initializing BME280: {e}")
    print(f"\nTroubleshooting:")
    print(f"  1. Check wiring:")
    print(f"     - VCC to 3.3V")
    print(f"     - GND to GND")
    print(f"     - SDA to GP{I2C_SDA_PIN}")
    print(f"     - SCL to GP{I2C_SCL_PIN}")
    print(f"  2. Try changing I2C_ADDRESS to 0x76 if using 0x77")
    print(f"  3. Verify BME280 is powered on")
    raise

# Main loop - read and display all sensor data
try:
    reading_count = 0
    while True:
        reading_count += 1

        # Read all sensor values
        temp_c = bme280.temperature
        temp_f = (temp_c * 9/5) + 32
        humidity = bme280.relative_humidity
        pressure = bme280.pressure

        # Print to console
        print(f"\nReading #{reading_count}:")
        if USE_FAHRENHEIT:
            print(f"  Temperature: {temp_f:.2f}°F ({temp_c:.2f}°C)")
        else:
            print(f"  Temperature: {temp_c:.2f}°C ({temp_f:.2f}°F)")

        print(f"  Humidity:    {humidity:.2f}%")
        print(f"  Pressure:    {pressure:.2f} hPa")

        # Wait before next reading
        time.sleep(2)

except KeyboardInterrupt:
    print("\n\nTest stopped by user")
    print(f"Total readings: {reading_count}")
    print("BME280 sensor test complete!")
except Exception as e:
    print(f"\n\nError reading sensor: {e}")
    raise
