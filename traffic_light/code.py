"""
Traffic Light - CircuitPython
Simple traffic light controller using red, yellow, and green LEDs.

Wiring:
- Red LED    -> GP6 -> 220Ω resistor -> LED -> GND
- Yellow LED -> GP7 -> 220Ω resistor -> LED -> GND
- Green LED  -> GP8 -> 220Ω resistor -> LED -> GND
"""

import time
import board
import digitalio

# Configuration - Timing in seconds
GREEN_DURATION = 5.0   # How long green light stays on
YELLOW_DURATION = 2.0  # How long yellow light stays on
RED_DURATION = 5.0     # How long red light stays on

# Pin Configuration
RED_PIN = board.GP6
YELLOW_PIN = board.GP7
GREEN_PIN = board.GP8

print("=" * 50)
print("Traffic Light Controller")
print("=" * 50)

# Initialize LED outputs
try:
    print("\nInitializing LEDs...")

    red_led = digitalio.DigitalInOut(RED_PIN)
    red_led.direction = digitalio.Direction.OUTPUT

    yellow_led = digitalio.DigitalInOut(YELLOW_PIN)
    yellow_led.direction = digitalio.Direction.OUTPUT

    green_led = digitalio.DigitalInOut(GREEN_PIN)
    green_led.direction = digitalio.Direction.OUTPUT

    # Turn all LEDs off initially
    red_led.value = False
    yellow_led.value = False
    green_led.value = False

    print("✓ LEDs initialized")
    print(f"  Red:    GP{RED_PIN}")
    print(f"  Yellow: GP{YELLOW_PIN}")
    print(f"  Green:  GP{GREEN_PIN}")

except Exception as e:
    print(f"✗ Error initializing LEDs: {e}")
    raise

print("\nTraffic light sequence:")
print(f"  Green:  {GREEN_DURATION}s")
print(f"  Yellow: {YELLOW_DURATION}s")
print(f"  Red:    {RED_DURATION}s")
print("\nStarting traffic light cycle...")
print("Press Ctrl+C to stop\n")
print("-" * 50)

# Main loop
try:
    while True:
        # GREEN LIGHT
        print("GREEN  - Go!")
        green_led.value = True
        red_led.value = False
        yellow_led.value = False
        time.sleep(GREEN_DURATION)

        # YELLOW LIGHT
        print("YELLOW - Slow down!")
        green_led.value = False
        yellow_led.value = True
        red_led.value = False
        time.sleep(YELLOW_DURATION)

        # RED LIGHT
        print("RED    - Stop!")
        green_led.value = False
        yellow_led.value = False
        red_led.value = True
        time.sleep(RED_DURATION)

except KeyboardInterrupt:
    print("\n\nTraffic light stopped by user")

    # Turn all LEDs off
    red_led.value = False
    yellow_led.value = False
    green_led.value = False

    print("All lights turned off")

except Exception as e:
    print(f"\n\nError: {e}")
    # Turn all LEDs off on error
    red_led.value = False
    yellow_led.value = False
    green_led.value = False
    raise
