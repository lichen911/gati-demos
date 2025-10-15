"""
TM1637 Display Test - CircuitPython
Simple test to verify TM1637 4-digit 7-segment display and count up.
"""

import time
import board
from tm1637_display import TM1637Display

# Configuration
TM1637_CLK_PIN = board.GP2
TM1637_DIO_PIN = board.GP3
DISPLAY_BRIGHTNESS = 6     # 0-6, with 6 being brightest
COUNT_DELAY = 0.5          # Seconds between count updates

print("=" * 50)
print("TM1637 Display Test")
print("=" * 50)

# Initialize TM1637 display
try:
    print(f"\nInitializing TM1637 on CLK={TM1637_CLK_PIN}, DIO={TM1637_DIO_PIN}...")
    display = TM1637Display(TM1637_CLK_PIN, TM1637_DIO_PIN)
    display.brightness = DISPLAY_BRIGHTNESS

    print("✓ TM1637 display initialized successfully!")
    print(f"  Brightness: {DISPLAY_BRIGHTNESS}/6")

    # Show startup pattern
    display.print("----")
    time.sleep(0.5)
    display.clear()

    print("\nStarting count test (0-9999)...")
    print("Press Ctrl+C to stop\n")
    print("-" * 50)

except Exception as e:
    print(f"\n✗ Error initializing TM1637: {e}")
    print(f"\nTroubleshooting:")
    print(f"  1. Check wiring:")
    print(f"     - VCC to 5V (or 3.3V)")
    print(f"     - GND to GND")
    print(f"     - CLK to {TM1637_CLK_PIN}")
    print(f"     - DIO to {TM1637_DIO_PIN}")
    print(f"  2. Verify display module is powered on")
    print(f"  3. Check for loose connections")
    raise

# Main loop - count from 0 to 9999
try:
    counter = 0

    while True:
        # Display the current count (4 digits with leading zeros)
        display.print(f"{counter:04d}")

        # Print to console
        print(f"Count: {counter:04d}")

        # Increment counter (wrap at 10000)
        counter = (counter + 1) % 10000

        # Wait before next count
        time.sleep(COUNT_DELAY)

except KeyboardInterrupt:
    print("\n\nTest stopped by user")
    print("TM1637 display test complete!")

    # Show end pattern
    display.print("----")
    time.sleep(0.5)
    display.clear()

except Exception as e:
    print(f"\n\nError during test: {e}")
    raise
