# Joke Machine Setup Guide

## Hardware Requirements

- ESP32-C3 Super Mini microcontroller
- 0.96" OLED display (SSD1306, 128x64 pixels, I2C interface)
- 6x6mm tactile button
- Jumper wires
- Breadboard (optional)

## Wiring Diagram

### OLED Display (I2C)
- VCC → 3.3V
- GND → GND
- SDA → GPIO8
- SCL → GPIO9

### Button
- One side → GPIO10
- Other side → GND
(Internal pull-up resistor is enabled in code)

## Software Setup

### 1. Install MicroPython on ESP32-C3

Download the latest ESP32-C3 MicroPython firmware from:
https://micropython.org/download/ESP32_GENERIC_C3/

Flash the firmware using esptool:

```bash
# Erase flash
esptool.py --chip esp32c3 --port /dev/ttyUSB0 erase_flash

# Flash MicroPython
esptool.py --chip esp32c3 --port /dev/ttyUSB0 write_flash -z 0x0 ESP32_GENERIC_C3-*.bin
```

### 2. Upload the Code

You can use various tools to upload the code to your ESP32-C3:

#### Option A: Using ampy (Adafruit MicroPython Tool)

```bash
# Install ampy
pip install adafruit-ampy

# Upload files
ampy --port /dev/ttyUSB0 put ssd1306.py
ampy --port /dev/ttyUSB0 put main.py
```

#### Option B: Using rshell

```bash
# Install rshell
pip install rshell

# Connect and copy files
rshell --port /dev/ttyUSB0
> cp ssd1306.py /pyboard/
> cp main.py /pyboard/
> repl
```

#### Option C: Using Thonny IDE

1. Install Thonny: https://thonny.org/
2. Configure interpreter: Tools → Options → Interpreter → MicroPython (ESP32)
3. Select your port
4. Open each file and save it to the device

### 3. Run the Program

The program will automatically start when you reset the ESP32-C3, or you can run it manually:

```python
import main
```

## Usage

1. **Power on**: The first joke question will appear on the display
2. **Press button**: Reveals the answer to the current joke
3. **Press button again**: Shows the next joke question
4. **Cycles through**: After the last joke, it wraps back to the first

## Customizing Jokes

Edit the `JOKES` list in `main.py`:

```python
JOKES = [
    ("Your question here?",
     "Your punchline here!"),
    # Add more jokes...
]
```

Tips for formatting:
- Keep text short for readability
- Use `\n` for manual line breaks
- Text auto-wraps at ~16 characters per line
- Display shows up to 6 lines

## Troubleshooting

### Display shows nothing
- Check I2C wiring (SDA/SCL)
- Verify I2C address (default 0x3C, some displays use 0x3D)
- Check display power (3.3V, not 5V)

### Button not responding
- Verify button wiring to GPIO10 and GND
- Check for loose connections
- Try adjusting debounce time in code (default 200ms)

### I2C address issues
If your display uses address 0x3D, modify `main.py`:

```python
self.display = SSD1306_I2C(DISPLAY_WIDTH, DISPLAY_HEIGHT, self.i2c, addr=0x3D)
```

### Check I2C devices
Use this snippet to scan for I2C devices:

```python
from machine import Pin, SoftI2C
i2c = SoftI2C(scl=Pin(9), sda=Pin(8))
print(i2c.scan())  # Should show [60] for 0x3C or [61] for 0x3D
```

## GPIO Pin Configuration

You can modify the GPIO pins in `main.py` if needed:

```python
I2C_SDA_PIN = 8   # Change as needed
I2C_SCL_PIN = 9   # Change as needed
BUTTON_PIN = 10   # Change as needed
```

## Serial Debugging

Connect via serial to see debug messages:

```bash
screen /dev/ttyUSB0 115200
# or
minicom -D /dev/ttyUSB0 -b 115200
```

Press Ctrl+C to stop the program and access the MicroPython REPL.
