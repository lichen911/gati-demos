import board
import digitalio
import time

led = digitalio.DigitalInOut(board.GP2)
led.direction = digitalio.Direction.OUTPUT

while True:
    led.value = True  # Turn on
    time.sleep(0.5)
    led.value = False  # Turn off
    time.sleep(0.5)
