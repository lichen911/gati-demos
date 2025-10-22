"""
Traffic Light - CircuitPython
Simple traffic light controller using red, yellow, and green LEDs.
Button on GP2 controls speed - cycles through 9 speed levels (1x, 2x, 4x, 8x, 16x, 32x, 64x, 128x, 256x).

Wiring:
- Red LED    -> GP6 -> 220Ω resistor -> LED -> GND
- Yellow LED -> GP7 -> 220Ω resistor -> LED -> GND
- Green LED  -> GP8 -> 220Ω resistor -> LED -> GND
- Button     -> GP2 -> Button -> GND (internal pull-up enabled)
"""

import time
import board
import digitalio

# Configuration - Base timing in seconds (at speed level 0)
BASE_GREEN_DURATION = 5.0   # How long green light stays on
BASE_YELLOW_DURATION = 2.0  # How long yellow light stays on
BASE_RED_DURATION = 5.0     # How long red light stays on

# Pin Configuration
RED_PIN = board.GP6
YELLOW_PIN = board.GP7
GREEN_PIN = board.GP8
BUTTON_PIN = board.GP2

# Speed control
speed_level = 0  # 0-8, where each level doubles the speed
MAX_SPEED_LEVEL = 8

print("=" * 50)
print("Traffic Light Controller")
print("=" * 50)

# Helper function to get current durations based on speed level
def get_durations():
    """Calculate current durations based on speed level (each level is 2x faster)"""
    speed_multiplier = 2 ** speed_level
    return (
        BASE_GREEN_DURATION / speed_multiplier,
        BASE_YELLOW_DURATION / speed_multiplier,
        BASE_RED_DURATION / speed_multiplier
    )

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

# Initialize button input
try:
    print("\nInitializing button...")

    button = digitalio.DigitalInOut(BUTTON_PIN)
    button.direction = digitalio.Direction.INPUT
    button.pull = digitalio.Pull.UP  # Internal pull-up resistor

    print(f"✓ Button initialized on GP{BUTTON_PIN}")
    print("  Press button to cycle through speeds (1x -> 2x -> 4x -> 8x -> 16x -> 32x -> 64x -> 128x -> 256x -> 1x)")

except Exception as e:
    print(f"✗ Error initializing button: {e}")
    raise

# Button state tracking for debouncing
button_pressed = False
last_button_state = True  # True = not pressed (pull-up)

green_dur, yellow_dur, red_dur = get_durations()
print("\nTraffic light sequence:")
print(f"  Green:  {green_dur}s")
print(f"  Yellow: {yellow_dur}s")
print(f"  Red:    {red_dur}s")
print(f"\nCurrent speed: {2 ** speed_level}x (Level {speed_level}/{MAX_SPEED_LEVEL})")
print("\nStarting traffic light cycle...")
print("Press Ctrl+C to stop\n")
print("-" * 50)

# Helper function to sleep while checking for button presses
def smart_sleep(duration):
    """Sleep for duration while checking button presses every 50ms"""
    global speed_level, last_button_state

    elapsed = 0
    check_interval = 0.05  # Check button every 50ms

    while elapsed < duration:
        # Check button state
        current_button_state = button.value

        # Detect button press (transition from high to low with pull-up)
        if last_button_state and not current_button_state:
            # Button was just pressed
            speed_level = (speed_level + 1) % (MAX_SPEED_LEVEL + 1)
            green_dur, yellow_dur, red_dur = get_durations()
            print(f"\n[Speed changed to {2 ** speed_level}x (Level {speed_level}/{MAX_SPEED_LEVEL})]")
            print(f"  New timings - Green: {green_dur}s, Yellow: {yellow_dur}s, Red: {red_dur}s\n")

            # Wait for button release to avoid multiple triggers
            while not button.value:
                time.sleep(0.05)

        last_button_state = current_button_state

        # Sleep for a small interval
        time.sleep(check_interval)
        elapsed += check_interval

# Main loop
try:
    while True:
        # Get current durations based on speed level
        green_dur, yellow_dur, red_dur = get_durations()

        # GREEN LIGHT
        print("GREEN  - Go!")
        green_led.value = True
        red_led.value = False
        yellow_led.value = False
        smart_sleep(green_dur)

        # YELLOW LIGHT
        print("YELLOW - Slow down!")
        green_led.value = False
        yellow_led.value = True
        red_led.value = False
        smart_sleep(yellow_dur)

        # RED LIGHT
        print("RED    - Stop!")
        green_led.value = False
        yellow_led.value = False
        red_led.value = True
        smart_sleep(red_dur)

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
