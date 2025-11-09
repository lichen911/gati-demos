"""
Traffic Light - CircuitPython
Simple traffic light controller using red, yellow, and green LEDs.
Press button to make it go faster!

Wiring:
- Red LED    -> GP6 -> 220Ω resistor -> LED -> GND
- Yellow LED -> GP7 -> 220Ω resistor -> LED -> GND
- Green LED  -> GP8 -> 220Ω resistor -> LED -> GND
- Button     -> GP2 -> Button -> GND
"""

import time
import board
import digitalio

# How long each light stays on (at normal speed)
BASE_DURATION = 3.0

# Speed level - starts at 0, goes up to 7
speed_level = 0

# Setup the red LED
red_led = digitalio.DigitalInOut(board.GP6)
red_led.direction = digitalio.Direction.OUTPUT

# Setup the yellow LED
yellow_led = digitalio.DigitalInOut(board.GP7)
yellow_led.direction = digitalio.Direction.OUTPUT

# Setup the green LED
green_led = digitalio.DigitalInOut(board.GP8)
green_led.direction = digitalio.Direction.OUTPUT

# Setup the button
button = digitalio.DigitalInOut(board.GP2)
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.UP

# Turn all LEDs off to start
red_led.value = False
yellow_led.value = False
green_led.value = False

# Remember the last button state
last_button_state = True

# Function to wait and check for button presses
def wait_and_check_button(duration):
    global speed_level, last_button_state

    elapsed = 0
    while elapsed < duration:
        # Check if button was pressed
        current_button_state = button.value
        if last_button_state and not current_button_state:
            # Button was just pressed!
            speed_level = (speed_level + 1) % 8

            # Wait for button release
            while not button.value:
                time.sleep(0.05)

        last_button_state = current_button_state
        time.sleep(0.05)
        elapsed += 0.05

# Main loop - repeat forever
while True:
    # Calculate how long to wait based on speed level
    # Each level is 2x faster: divide by 2^speed_level
    wait_time = BASE_DURATION / (2 ** speed_level)

    # Turn on green light
    green_led.value = True
    red_led.value = False
    yellow_led.value = False
    wait_and_check_button(wait_time)

    # Turn on yellow light
    green_led.value = False
    yellow_led.value = True
    red_led.value = False
    wait_and_check_button(wait_time)

    # Turn on red light
    green_led.value = False
    yellow_led.value = False
    red_led.value = True
    wait_and_check_button(wait_time)
