# Traffic Light

A simple traffic light simulator using red, yellow, and green LEDs with realistic timing. Perfect for learning GPIO control and timing sequences.

## Features

- Realistic traffic light sequence: Green → Yellow → Red → (repeat)
- Configurable timing for each light phase
- Serial output showing current light state
- Clean startup/shutdown with all lights off
- Error handling with automatic LED shutoff

## Hardware Requirements

- RP2040 Development Board (Raspberry Pi Pico or compatible)
- 3x LEDs (Red, Yellow, Green - standard 5mm or 3mm)
- 3x 220Ω resistors (current limiting for LEDs)
- Jumper wires
- Breadboard
- USB cable for power and programming

## Wiring Diagram

### Red LED
- RP2040 GPIO6 → 220Ω resistor → LED Anode (+)
- LED Cathode (-) → GND

### Yellow LED
- RP2040 GPIO7 → 220Ω resistor → LED Anode (+)
- LED Cathode (-) → GND

### Green LED
- RP2040 GPIO8 → 220Ω resistor → LED Anode (+)
- LED Cathode (-) → GND

**Note:** The 220Ω resistors protect the LEDs from overcurrent. The RP2040 GPIO pins output 3.3V, and typical LEDs need 2-2.2V with 10-20mA current.

## Pin Summary
```
RP2040 GPIO Assignments:
├── GP6 → 220Ω → Red LED → GND
├── GP7 → 220Ω → Yellow LED → GND
└── GP8 → 220Ω → Green LED → GND
```

## LED Polarity
LEDs have polarity and must be connected correctly:
- **Anode (+)**: Longer leg, connects to resistor from GPIO
- **Cathode (-)**: Shorter leg, flat side of LED, connects to GND

## Software Setup

### 1. Install CircuitPython on RP2040

1. Download CircuitPython UF2 file for your RP2040 board from: https://circuitpython.org/
2. Hold BOOTSEL button while plugging in USB
3. Drag and drop UF2 file onto RPI-RP2 drive
4. Board reboots as CIRCUITPY drive

### 2. Upload the Code

Simply copy `code.py` to the CIRCUITPY drive. The program will automatically start running.

### 3. Required Libraries

No additional libraries required! This project uses only CircuitPython built-in modules:
- `board` - GPIO pin definitions
- `digitalio` - Digital I/O control
- `time` - Timing and delays

## Traffic Light Sequence

### Default Timing
- **Green Light**: 5 seconds (go)
- **Yellow Light**: 2 seconds (caution/slow down)
- **Red Light**: 5 seconds (stop)
- Total cycle time: 12 seconds

### Behavior
1. Green light turns ON (yellow and red OFF)
2. After 5 seconds, yellow light turns ON (green and red OFF)
3. After 2 seconds, red light turns ON (green and yellow OFF)
4. After 5 seconds, cycle repeats from step 1

The sequence loops continuously until stopped by user (Ctrl+C).

## Configuration

Edit timing constants at the top of `code.py`:

```python
# Timing in seconds
GREEN_DURATION = 5.0   # How long green light stays on
YELLOW_DURATION = 2.0  # How long yellow light stays on
RED_DURATION = 5.0     # How long red light stays on
```

### Pin Configuration

Change GPIO pins if needed:

```python
# Pin Configuration
RED_PIN = board.GP6
YELLOW_PIN = board.GP7
GREEN_PIN = board.GP8
```

**Note:** You can use any GPIO pins on the RP2040. Common choices are GP0-GP22.

## Usage

### Running the Traffic Light
1. Connect hardware according to wiring diagram
2. Copy `code.py` to CIRCUITPY drive
3. Watch LEDs cycle through the sequence
4. Check serial output for current state

### Stopping the Traffic Light
Press **Ctrl+C** in the serial console to stop. All LEDs will turn off cleanly.

## Serial Output

Connect via serial to see traffic light status:

```bash
screen /dev/ttyACM0 115200
# or
minicom -D /dev/ttyACM0 -b 115200
```

Example output:
```
==================================================
Traffic Light Controller
==================================================

Initializing LEDs...
✓ LEDs initialized
  Red:    GP6
  Yellow: GP7
  Green:  GP8

Traffic light sequence:
  Green:  5.0s
  Yellow: 2.0s
  Red:    5.0s

Starting traffic light cycle...
Press Ctrl+C to stop

--------------------------------------------------
GREEN  - Go!
YELLOW - Slow down!
RED    - Stop!
GREEN  - Go!
...
```

## Customization Ideas

### Add All-Red Phase
Insert a brief all-lights-off or all-red period:
```python
# After red phase, before green
time.sleep(0.5)  # Brief pause
```

### Flashing Yellow (Caution Mode)
```python
# Replace yellow phase with flashing
for i in range(4):
    yellow_led.value = True
    time.sleep(0.5)
    yellow_led.value = False
    time.sleep(0.5)
```

### Pedestrian Crossing
Add a button to trigger a pedestrian crossing sequence with extended red time.

### Night Mode
Implement a flashing yellow mode for nighttime operation.

## Troubleshooting

### LEDs Don't Light Up
- Check LED polarity (longer leg to resistor, shorter leg to GND)
- Verify resistor connections (220Ω between GPIO and LED)
- Test LEDs with a coin cell battery (3V) to confirm they work
- Check GPIO pin assignments match your wiring

### LEDs Are Too Dim
- Try lower value resistors (150Ω or 100Ω) for brighter LEDs
- Ensure good breadboard connections
- Some LEDs are naturally dimmer than others

### LEDs Are Too Bright
- Use higher value resistors (330Ω or 470Ω)
- Or reduce duty cycle using PWM (advanced)

### Wrong LED Lights Up
- Double-check pin assignments in code match physical wiring
- Verify breadboard connections

### All LEDs Stay On
- Code may have crashed - press Ctrl+C and restart
- Check for syntax errors in code
- Re-upload code.py to CIRCUITPY drive

### Code Doesn't Auto-Run
- Ensure file is named exactly `code.py` (lowercase)
- Check that file is in root of CIRCUITPY drive (not in a folder)
- Try pressing reset button on RP2040
- Re-flash CircuitPython if issues persist

## Educational Use

This project is great for teaching:
- **GPIO basics**: Digital output control
- **State machines**: Sequential state transitions
- **Timing**: Using delays and time-based logic
- **Real-world systems**: How actual traffic lights work
- **Safety**: Importance of yellow caution phase

### Discussion Questions
- Why is there a yellow light phase?
- What happens if yellow time is too short?
- How might traffic lights coordinate at intersections?
- What sensors might real traffic lights use?

## Next Steps / Enhancements

- Add a pedestrian crossing button and walk signal LED
- Implement traffic light coordination for multiple intersections
- Add light sensors to detect day/night and switch modes
- Use potentiometer to adjust timing dynamically
- Add sound effects (buzzer for pedestrian crossing)
- Create a 4-way intersection with multiple traffic lights
- Log traffic light states to a file for analysis

## Technical Details

### Current Draw per LED
- Typical LED forward voltage: ~2.0-2.2V
- GPIO output: 3.3V
- Voltage across 220Ω resistor: ~1.1V
- Current per LED: ~5mA (well within GPIO limit of 12mA)
- Total current (all 3 LEDs): ~15mA

### GPIO Safe Operating Limits
- Maximum current per pin: 12mA
- Absolute maximum: 16mA (avoid continuous operation at this level)
- With 220Ω resistors, each LED draws ~5mA (safe)

## References

- [CircuitPython Digital I/O Guide](https://learn.adafruit.com/circuitpython-essentials/circuitpython-digital-in-out)
- [RP2040 Datasheet](https://datasheets.raspberrypi.com/rp2040/rp2040-datasheet.pdf)
- [LED Resistor Calculator](https://www.digikey.com/en/resources/conversion-calculators/conversion-calculator-led-series-resistor)
